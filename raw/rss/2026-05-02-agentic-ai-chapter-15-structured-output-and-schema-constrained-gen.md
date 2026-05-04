---
source: farmer/rss
feed: agentic-ai
farmed: 2026-05-04T03:30:51.603623+00:00
title: Chapter 15: Structured Output and Schema-Constrained Generation (Claude Code vs. Hermes Agent)
url: https://kenhuangus.substack.com/p/chapter-15-structured-output-and
published: 2026-05-02
author: Ken Huang
---

# Chapter 15: Structured Output and Schema-Constrained Generation (Claude Code vs. Hermes Agent)

<h2>1. Pattern Summary</h2><p>Structured output is the pattern of constraining an LLM's response to a machine-readable schema rather than free text. Where a normal agent turn produces a natural-language reply, a structured output turn produces a validated JSON object &#8212; one that downstream code can parse, type-check, and act on without brittle regex or prompt-engineering gymnastics. The pattern matters because agents that produce unstructured text are hard to integrate; agents that produce validated JSON are composable. It bridges the gap between the model's natural language reasoning and the typed data structures that pipelines, databases, and APIs actually expect. This is distinct from tool input validation (cc2): that pattern constrains what the <em>caller</em> sends <em>into</em> a tool; this pattern constrains what the <em>model</em> sends <em>back</em> as its final answer.</p><h2>2. Claude Code Implementation</h2><h3>The <code>jsonSchema</code> Parameter</h3><p>The entry point is the <code>jsonSchema</code> parameter on <code>ask()</code> and <code>QueryEngine</code>. When present, it activates structured output mode for the entire query:</p><pre><code>// src/QueryEngine.ts &#8212; ask() signature (simplified)
// Pass a JSON Schema object to force the model's final response
// to conform to that schema instead of producing free text.
export async function* ask({
  prompt,
  jsonSchema,   // &lt;-- the schema you want the model to fill
  tools,
  // ...other params
}): AsyncGenerator&lt;SDKMessage, void, unknown&gt; {
  const engine = new QueryEngine({
    jsonSchema,   // forwarded to the engine
    tools,
    // ...
  })
  yield* engine.submitMessage(prompt)
}</code></pre><p>Passing <code>jsonSchema</code> does two things: it injects the <code>SyntheticOutputTool</code> into the tool list, and it activates retry-budget tracking in the query loop.</p><h3>The Synthetic-Tool Trick</h3><p>This is the elegant part. Rather than using a provider-specific "JSON mode" flag, Claude Code wraps the JSON schema as a <em>fake tool definition</em> &#8212; <code>SYNTHETIC_OUTPUT_TOOL_NAME = 'StructuredOutput'</code> &#8212; and forces the model to "call" it with valid JSON arguments. The model's tool-calling machinery, which is already well-trained and reliable, does the heavy lifting:</p><pre><code>// src/tools/SyntheticOutputTool/SyntheticOutputTool.ts

// The tool name the harness uses internally to track structured output attempts
export const SYNTHETIC_OUTPUT_TOOL_NAME = 'StructuredOutput'

// createSyntheticOutputTool() takes your JSON schema and returns a Tool
// whose inputJSONSchema IS your schema. The model must call this tool
// with arguments that satisfy the schema &#8212; or the call throws.
export function createSyntheticOutputTool(
  jsonSchema: Record&lt;string, unknown&gt;,
): CreateResult {
  // Identity-cached by schema object reference &#8212; 80-call workflows
  // go from ~110ms to ~4ms Ajv overhead
  const cached = toolCache.get(jsonSchema)
  if (cached) return cached

  const ajv = new Ajv({ allErrors: true })
  const validateSchema = ajv.compile(jsonSchema)  // compile once, reuse

  return {
    tool: {
      ...SyntheticOutputTool,
      inputJSONSchema: jsonSchema,  // &lt;-- your schema becomes the tool's input schema
      async call(input) {
        const isValid = validateSchema(input)
        if (!isValid) {
          // Throw a telemetry-safe error &#8212; the harness catches this,
          // feeds the validation errors back to the model, and retries
          const errors = validateSchema.errors
            ?.map(e =&gt; `${e.instancePath || 'root'}: ${e.message}`)
            .join(', ')
          throw new TelemetrySafeError(
            `Output does not match required schema: ${errors}`,
          )
        }
        return { data: 'Structured output provided successfully', structured_output: input }
      },
    },
  }
}</code></pre><p>The model sees a tool called <code>StructuredOutput</code> with your schema as its input spec. It must call that tool exactly once at the end of its response. If the arguments don't validate against the schema, the call throws, the harness feeds the error back, and the model retries.</p><p>A hook enforces the "call it exactly once" contract:</p><pre><code>// src/utils/hooks/hookHelpers.ts
// If the model tries to stop without calling StructuredOutput,
// this hook fires and reminds it to call the tool.
registerStructuredOutputEnforcement(
  'Stop',
  '',  // applies to all stop reasons
  messages =&gt; hasSuccessfulToolCall(messages, SYNTHETIC_OUTPUT_TOOL_NAME),
  `You MUST call the ${SYNTHETIC_OUTPUT_TOOL_NAME} tool to complete this request. Call this tool now.`,
  { timeout: 5000 },
)</code></pre><h3>Retry Budget: <code>MAX_STRUCTURED_OUTPUT_RETRIES</code></h3><p>The harness doesn't retry forever. It tracks how many times the synthetic tool has been called in the current query and stops when the budget is exhausted:</p><pre><code>// src/QueryEngine.ts &#8212; inside the query loop, on every user message
if (message.type === 'user' &amp;&amp; jsonSchema) {
  // Count how many StructuredOutput calls have happened since this query started.
  // initialStructuredOutputCalls is snapshotted before the query begins,
  // so this is a delta &#8212; retries for THIS query only, not prior queries.
  const currentCalls = countToolCalls(this.mutableMessages, SYNTHETIC_OUTPUT_TOOL_NAME)
  const callsThisQuery = currentCalls - initialStructuredOutputCalls

  // Default 5, overridable via environment variable
  const maxRetries = parseInt(process.env.MAX_STRUCTURED_OUTPUT_RETRIES || '5', 10)

  if (callsThisQuery &gt;= maxRetries) {
    // Surface a typed error result &#8212; SDK consumers can handle this case
    yield {
      type: 'result',
      subtype: 'error_max_structured_output_retries',
      errors: [`Failed to provide valid structured output after ${maxRetries} attempts`],
    }
    return  // terminate the query loop
  }
}</code></pre><p>The <code>error_max_structured_output_retries</code> subtype is part of the SDK's typed result union, so callers can distinguish "model gave up on structured output" from "model hit max turns" or "budget exceeded". The retry count is also excluded from the regular tool-call count &#8212; structured output attempts don't eat into the agent's tool budget.</p><h3>Integration with the Query Loop</h3><p>Structured output turns are tracked separately from regular tool calls. Before the query starts, the harness snapshots the current <code>StructuredOutput</code> call count:</p><pre><code>// src/QueryEngine.ts &#8212; before submitMessage() enters the loop
const initialStructuredOutputCalls = jsonSchema
  ? countToolCalls(this.mutableMessages, SYNTHETIC_OUTPUT_TOOL_NAME)
  : 0
// Delta-based: callsThisQuery = current - initial
// This means retries from a previous query don't count against this one</code></pre><p>The <code>SYNTHETIC_OUTPUT_TOOL_NAME</code> is also excluded from agent subtools &#8212; when a parent agent spawns a child, the child's tool list is filtered to remove <code>StructuredOutput</code> so it doesn't accidentally inherit the parent's output contract.</p><h2>3. Hermes Agent Implementation</h2><h3>Model Capability Flag</h3><p>Hermes tracks structured output as a first-class model capability in its model metadata:</p><pre><code># hermes-agent/agent/models_dev.py
@dataclass
class ModelCapabilities:
    # ... other caps
    structured_output: bool = False  # supports schema-constrained JSON output
    # Used to gate whether response_format or tool-forcing is available
    # for a given model. Checked before attempting structured output.</code></pre><h3>Tool-Use Forcing: The Portable Approach</h3><p>Hermes's primary structured output mechanism is tool-use forcing: define a single tool whose schema matches the output you want, then instruct the model to call it. This works across every provider that supports function calling &#8212; OpenAI, Anthropic, OpenRouter, local models &#8212; without relying on provider-specific JSON mode flags:</p><pre><code># Pattern: force structured output via a single-tool schema
# Works on any provider that supports tool calling

def extract_structured(
    agent: AIAgent,
    prompt: str,
    output_schema: dict,
    tool_name: str = "extract_result",
) -&gt; dict:
    """
    Force the model to return structured JSON by presenting the schema
    as the only available tool. The model must call it to respond.
    """
    # Wrap the schema as a tool definition &#8212; same trick as Claude Code,
    # but done explicitly in Python rather than via a harness abstraction
    tools = [{
        "type": "function",
        "function": {
            "name": tool_name,
            "description": "Return the extracted result in the required format",
            "parameters": output_schema,  # your JSON schema goes here
        }
    }]

    # Run the agent with only this one tool available.
    # The model has no choice but to call it.
    result = agent.run_conversation(
        prompt,
        tools_override=tools,
        tool_choice={"type": "function", "function": {"name": tool_name}},
    )

    # Extract the tool call arguments &#8212; that's your structured output
    for msg in result["messages"]:
        if msg.get("role") == "assistant" and msg.get("tool_calls"):
            for call in msg["tool_calls"]:
                if call["function"]["name"] == tool_name:
                    return json.loads(call["function"]["arguments"])

    raise ValueError("Model did not produce structured output")</code></pre><h3>Validation and Retry Loop</h3><p>Hermes implements its own retry loop when the model produces invalid JSON or fails schema validation. The key difference from Claude Code: the error is fed back as a conversation message rather than thrown inside a tool call, giving the model richer context for self-correction:</p><pre><code># Pattern: validate structured output, retry with error feedback injected as messages
from jsonschema import validate, ValidationError

def extract_with_retry(agent, prompt: str, schema: dict, max_retries: int = 3) -&gt; dict:
    messages = [{"role": "user", "content": prompt}]
    for attempt in range(max_retries):
        response = agent._call_api(messages)
        raw = response.choices[0].message.content
        try:
            parsed = json.loads(raw)
            validate(instance=parsed, schema=schema)  # AJV equivalent in Python
            return parsed  # success
        except json.JSONDecodeError as e:
            # Feed parse error back &#8212; model sees its own bad output and the error
            messages += [{"role": "assistant", "content": raw},
                         {"role": "user", "content": f"Invalid JSON: {e}. Return valid JSON only."}]
        except ValidationError as e:
            # Feed schema violation back with the specific failing field
            messages += [{"role": "assistant", "content": raw},
                         {"role": "user", "content": f"Schema error at '{e.json_path}': {e.message}"}]
    raise RuntimeError(f"Structured output failed after {max_retries} attempts")</code></pre><h3><code>batch_runner.py</code>: Structured Extraction at Scale</h3><p><code>batch_runner.py</code> is where Hermes's structured output story gets interesting. It runs the same extraction prompt across hundreds or thousands of inputs in parallel using <code>multiprocessing.Pool</code>, collecting typed results in JSONL format:</p><pre><code># hermes-agent/batch_runner.py (simplified core pattern)
from multiprocessing import Pool

def _process_single_prompt(
    prompt_index: int,
    prompt_data: dict,
    batch_num: int,
    config: dict,
) -&gt; dict:
    """
    Process one prompt with the agent and return a typed result dict.
    The return value IS structured output &#8212; every field is typed and
    validated before being written to the JSONL file.
    """
    agent = AIAgent(
        model=config["model"],
        enabled_toolsets=config["toolsets"],
        save_trajectories=False,  # batch_runner handles saving
        skip_memory=True,         # no persistent memory in batch runs
    )

    result = agent.run_conversation(prompt_data["prompt"])

    # Extract tool usage stats &#8212; structured, normalized schema
    tool_stats = _extract_tool_stats(result["messages"])

    # Normalize to include ALL possible tools with zero counts for missing ones.
    # This ensures HuggingFace datasets can load the JSONL without schema errors.
    normalized_stats = _normalize_tool_stats(tool_stats)

    # The return value is a typed record &#8212; every batch entry has the same shape
    return {
        "success": True,
        "prompt_index": prompt_index,
        "trajectory": agent._convert_to_trajectory_format(
            result["messages"], prompt_data["prompt"], result["completed"]
        ),
        "tool_stats": normalized_stats,       # {tool_name: {count, success, failure}}
        "tool_error_counts": {...},            # {tool_name: failure_count}
        "completed": result["completed"],
        "api_calls": result["api_calls"],
        "metadata": {
            "batch_num": batch_num,
            "timestamp": datetime.now().isoformat(),
            "model": config["model"],
        }
    }


class BatchRunner:
    def run(self):
        # Distribute batches across worker processes
        with Pool(processes=self.num_workers) as pool:
            for batch_result in pool.imap_unordered(_process_batch_worker, batch_args):
                # Each batch writes typed JSONL records to disk
                self._save_checkpoint(batch_result)</code></pre><p>The key insight: <code>batch_runner.py</code> treats the <em>entire output record</em> as structured data. Every field &#8212; <code>tool_stats</code>, <code>trajectory</code>, <code>metadata</code> &#8212; has a fixed schema enforced by <code>_normalize_tool_stats()</code> and <code>_normalize_tool_error_counts()</code>. This is structured output at the infrastructure level, not just the model level.</p><h3>Trajectory Format as Structured Output</h3><p>Hermes's trajectory format is itself a structured output contract. Every saved trajectory is a JSONL record with a fixed schema:</p><pre><code># hermes-agent/agent/trajectory.py
def save_trajectory(trajectory: list, model: str, completed: bool, filename: str = None):
    """
    Append a trajectory entry to a JSONL file.
    Each line is a typed record &#8212; the schema is implicit but consistent:
    {
        "conversations": [...],   # ShareGPT-format message list
        "timestamp": "ISO-8601",
        "model": "model-name",
        "completed": bool,
    }
    """
    entry = {
        "conversations": trajectory,
        "timestamp": datetime.now().isoformat(),
        "model": model,
        "completed": completed,
    }
    with open(filename, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")</code></pre><p>The JSONL format is a deliberate structured output choice: each line is independently parseable, the schema is consistent across all entries, and downstream tools (HuggingFace datasets, Spark, DuckDB) can consume it without a schema registry.</p><h2>4. Side-by-Side Comparison</h2><div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" href="https://substackcdn.com/image/fetch/$s_!ooyL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa9a664e2-7f0b-4726-9f71-a0ea644fe730_1064x633.png" target="_blank"><div class="image2-inset"><source type="image/webp" /><img alt="Comparison table" class="sizing-normal" height="633" src="https://substackcdn.com/image/fetch/$s_!ooyL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa9a664e2-7f0b-4726-9f71-a0ea644fe730_1064x633.png" title="Comparison table" width="1064" /><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset"><button class="pencraft pc-reset pencraft icon-container restack-image" tabindex="0" type="button"><svg fill="none" height="20" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><g><title></title><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button class="pencraft pc-reset pencraft icon-container view-image" tabindex="0" type="button"><svg class="lucide lucide-maximize2 lucide-maximize-2" fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button></div></div></div></a></figure></div><h2>5. When to Use Which</h2><p><strong>Use Claude Code's `jsonSchema` approach when:</strong></p>
      <p>
          <a href="https://kenhuangus.substack.com/p/chapter-15-structured-output-and">
              Read more
          </a>
      </p>
