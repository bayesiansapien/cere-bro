---
source: farmer/rss
feed: agentic-ai
farmed: 2026-04-19T04:40:12.897803+00:00
title: "Chapter 1: The Harness Paradigm (Claude Code vs. Hermes Agent)"
url: https://kenhuangus.substack.com/p/chapter-1-the-harness-paradigm-claude
published: 2026-04-18
author: "Ken Huang"
---

# Chapter 1: The Harness Paradigm (Claude Code vs. Hermes Agent)

<h2>1. Pattern Summary</h2><p>The harness paradigm is the foundational insight of production AI engineering: the model provides intelligence, but the harness provides control. A raw language model is a text generator &#8212; powerful but undirected, capable but unsafe. The harness is the infrastructure layer that wraps the model and transforms it into a controllable, auditable, production-ready agent. It constrains the action space through typed tools, manages conversation state across turns, enforces safety through a permission system, handles failures gracefully, and tracks resource consumption. Without a harness, deploying an LLM into production is like wiring a jet engine directly to a steering wheel &#8212; the power is there, but the control system is missing.</p><h2>2. Claude Code Implementation</h2><p>Claude Code implements the harness as a TypeScript class called <code>QueryEngine</code>. This class is the single owner of all mutable state in a conversation session, and every agent interaction flows through it.</p><h3>The QueryEngine as harness core</h3><pre><code>// src/QueryEngine.ts
// The QueryEngine is the harness core &#8212; it owns all mutable state for a session.
export class QueryEngine {
  private config: QueryEngineConfig
  private mutableMessages: Message[]       // Full conversation history, append-only
  private abortController: AbortController // User can cancel mid-execution at any time
  private permissionDenials: SDKPermissionDenial[] // Audit trail of every blocked action
  private totalUsage: NonNullableUsage     // Cumulative token + cost tracking</code></pre><p>Each field maps to a core harness responsibility. <code>mutableMessages</code> is the agent's memory &#8212; every user message, assistant response, and tool result is appended here. <code>abortController</code> is the emergency stop &#8212; the user can always regain control. <code>permissionDenials</code> is the audit trail &#8212; every blocked action is recorded for review. <code>totalUsage</code> is the budget tracker &#8212; the harness knows exactly what the session has cost.</p><h3>submitMessage() as async generator</h3><p>The QueryEngine exposes its functionality through a single async generator method:</p><pre><code>// src/QueryEngine.ts
// submitMessage is an async generator &#8212; it yields results incrementally.
// This enables real-time streaming: the user sees text as it's generated,
// and tool executions are reported as they complete, not after the full turn.
async *submitMessage(
  prompt: string | ContentBlockParam[],
  options?: { uuid?: string; isMeta?: boolean },
): AsyncGenerator&lt;SDKMessage, void, unknown&gt;</code></pre><p>The async generator pattern is a deliberate design choice. Instead of blocking until the entire conversation turn is complete, <code>submitMessage</code> yields events as they happen &#8212; a token arrives, a tool starts, a tool finishes. This makes the system feel responsive and allows the UI layer to update in real time. It also means the harness can be interrupted mid-stream without losing the work already done.</p><h3>The Tool interface as fundamental abstraction</h3><p>Every action the model can take is expressed as a <code>Tool</code>. The interface is comprehensive by design &#8212; it forces every tool to declare not just what it does, but how it behaves:</p><pre><code>// src/Tool.ts
// The Tool interface is the contract between the harness and every action.
// Tools must declare their identity, execution logic, input schema,
// concurrency safety, read/write/destructive behavior, and permission rules.
export type Tool&lt;Input extends AnyObject = AnyObject, Output = unknown&gt; = {
  readonly name: string                          // How the model addresses this tool
  call(args, context, canUseTool, ...): Promise&lt;ToolResult&lt;Output&gt;&gt;  // Execution
  readonly inputSchema: Input                    // Zod schema &#8212; validated before call()
  isConcurrencySafe(input): boolean              // Can this run in parallel?
  isReadOnly(input): boolean                     // Safe to auto-approve?
  isDestructive?(input): boolean                 // Requires explicit user consent?
  checkPermissions(input, context): Promise&lt;PermissionResult&gt;  // Tool-specific safety
  maxResultSizeChars: number                     // Prevents context window explosions
}</code></pre><p>The <code>inputSchema</code> is a Zod schema &#8212; it provides both compile-time type safety and runtime validation. When the model produces a <code>tool_use</code> block, the harness validates the input against this schema before ever calling the tool. Malformed input never reaches tool code. The behavioral declarations (<code>isReadOnly</code>, <code>isDestructive</code>, <code>isConcurrencySafe</code>) let the harness make intelligent decisions about permissions and execution order without needing to understand what each tool actually does.</p><h2>3. Hermes Agent Implementation</h2><p>Hermes implements the harness as a Python class called <code>AIAgent</code> in <code>run_agent.py</code>. The design philosophy is similar &#8212; one class owns the session state &#8212; but the execution model is synchronous and the tool system uses a registry pattern rather than a typed interface.</p><h3>AIAgent class structure</h3><pre><code># run_agent.py
# AIAgent is the harness core in Hermes &#8212; it owns model, budget, callbacks, and platform context.
class AIAgent:
    def __init__(
        self,
        model: str = "anthropic/claude-opus-4.6",
        max_iterations: int = 90,        # Hard cap on LLM turns
        enabled_toolsets: List[str] = None,
        disabled_toolsets: List[str] = None,
        platform: str = None,            # "cli", "telegram", "discord", etc.
        iteration_budget: "IterationBudget" = None,  # Shared across parent + subagents
        tool_progress_callback: callable = None,     # Real-time tool status updates
        clarify_callback: callable = None,           # Human-in-the-loop questions
        session_id: str = None,
        # ... plus provider, routing, memory, and checkpoint params
    ):
        self.model = model
        self.max_iterations = max_iterations
        # IterationBudget is thread-safe and shared with subagents.
        # Parent creates it; children inherit it. This caps total work
        # across the entire agent tree, not just the root agent.
        self.iteration_budget = iteration_budget or IterationBudget(max_iterations)
        self.platform = platform</code></pre><h3>IterationBudget: the Hermes safety valve</h3><pre><code># run_agent.py
# IterationBudget is a thread-safe counter that caps runaway agent loops.
# It's shared across parent and all subagents &#8212; total iterations are bounded
# at the tree level, not per-agent. consume() returns False when the budget
# is exhausted, which breaks the agent loop cleanly.
class IterationBudget:
    def __init__(self, max_total: int):
        self.max_total = max_total
        self._used = 0
        self._lock = threading.Lock()   # Thread-safe for parallel subagents

    def consume(self) -&gt; bool:
        """Try to consume one iteration. Returns True if allowed."""
        with self._lock:
            if self._used &gt;= self.max_total:
                return False
            self._used += 1
            return True

    def refund(self) -&gt; None:
        """Give back one iteration (e.g. for programmatic tool calls)."""
        with self._lock:
            if self._used &gt; 0:
                self._used -= 1</code></pre><h3>run_conversation() as synchronous loop</h3><pre><code># run_agent.py (simplified from AGENTS.md)
# run_conversation() is the harness loop &#8212; entirely synchronous.
# It calls the LLM, executes tools, and repeats until the model stops
# requesting tools or the iteration budget is exhausted.
def run_conversation(self, user_message: str, ...) -&gt; dict:
    while api_call_count &lt; self.max_iterations and self.iteration_budget.remaining &gt; 0:
        response = client.chat.completions.create(
            model=model, messages=messages, tools=tool_schemas
        )
        if response.tool_calls:
            # Execute each tool call and append results to message history
            for tool_call in response.tool_calls:
                result = handle_function_call(tool_call.name, tool_call.args, task_id)
                messages.append(tool_result_message(result))
            api_call_count += 1
        else:
            # No more tool calls &#8212; model is done
            return {"final_response": response.content, "messages": messages}</code></pre><h3>Tool registry pattern</h3><p>Where Claude Code uses a typed <code>Tool</code> interface, Hermes uses a central registry. Tools register themselves at import time:</p><pre><code># tools/registry.py (pattern from AGENTS.md)
# Tools self-register at import time. The registry collects schemas for the
# LLM's tool list and routes function_call events to the right handler.
# No interface to implement &#8212; just call registry.register() with a schema,
# a handler lambda, and an optional availability check function.
registry.register(
    name="port_scan",
    toolset="security",
    schema={
        "name": "port_scan",
        "description": "Scan open ports on a target host",
        "parameters": {"type": "object", "properties": {"host": {"type": "string"}}}
    },
    handler=lambda args, **kw: port_scan(host=args["host"], task_id=kw.get("task_id")),
    check_fn=lambda: bool(os.getenv("NMAP_AVAILABLE")),  # Availability guard
)</code></pre><p>The registry pattern trades compile-time safety for runtime flexibility. Tools can be added, removed, or conditionally enabled without changing any interface &#8212; just import the file and the tool appears. The <code>check_fn</code> provides the availability guard that Claude Code's <code>checkPermissions</code> handles at the interface level.</p><h2>4. Side-by-Side Comparison</h2><div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" href="https://substackcdn.com/image/fetch/$s_!Bsr1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F60e73a92-ac70-49e9-8bdc-1c69fd388a06_997x571.png" target="_blank"><div class="image2-inset"><source type="image/webp" /><img alt="Comparison table" class="sizing-normal" height="571" src="https://substackcdn.com/image/fetch/$s_!Bsr1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F60e73a92-ac70-49e9-8bdc-1c69fd388a06_997x571.png" title="Comparison table" width="997" /><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset"><button class="pencraft pc-reset pencraft icon-container restack-image" tabindex="0" type="button"><svg fill="none" height="20" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><g><title></title><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button class="pencraft pc-reset pencraft icon-container view-image" tabindex="0" type="button"><svg class="lucide lucide-maximize2 lucide-maximize-2" fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button></div></div></div></a></figure></div><h2>5. When to Use Which</h2><p></p>
      <p>
          <a href="https://kenhuangus.substack.com/p/chapter-1-the-harness-paradigm-claude">
              Read more
          </a>
      </p>
