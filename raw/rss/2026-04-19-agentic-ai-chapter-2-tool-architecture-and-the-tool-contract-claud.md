---
source: farmer/rss
feed: agentic-ai
farmed: 2026-04-20T09:02:04.518956+00:00
title: Chapter 2: Tool Architecture and the Tool Contract (Claude Code vs. Hermes Agent)
url: https://kenhuangus.substack.com/p/chapter-2-tool-architecture-and-the
published: 2026-04-19
author: Ken Huang
---

# Chapter 2: Tool Architecture and the Tool Contract (Claude Code vs. Hermes Agent)

<h2>1. Pattern Summary</h2><p>Every action an agent can take must be defined, validated, and declared safe or dangerous before it executes. This is the tool contract &#8212; the boundary between model reasoning and real-world consequences. A language model produces text; tools are what turn that text into file writes, network calls, shell commands, and system changes. The contract forces every tool to answer three questions before the harness will run it: <em>Is the input valid?</em> <em>Is the caller permitted?</em> <em>Can this run alongside other tools, or must it run alone?</em> Without this contract, the harness is blind to tool semantics and must treat every invocation as potentially catastrophic. With it, the harness can optimize concurrency, automate approvals for safe operations, and gate destructive actions behind explicit confirmation &#8212; all without the model needing to know any of this is happening.</p><h2>2. Claude Code Implementation</h2><p>Claude Code defines the tool contract in TypeScript using the <code>Tool</code> type and the <code>buildTool</code> factory. The design is opinionated: defaults are conservative, and tool authors must explicitly opt into optimizations.</p><h3>The buildTool Factory and TOOL_DEFAULTS</h3><pre><code>// src/Tool.ts
// Conservative defaults: every new tool starts as serial, stateful, and non-destructive.
// Tool authors must explicitly override to unlock concurrency or flag destructive behavior.
const TOOL_DEFAULTS = {
  isEnabled: () =&gt; true,
  isConcurrencySafe: (_input?: unknown) =&gt; false,   // serial by default
  isReadOnly: (_input?: unknown) =&gt; false,           // assume state mutation
  isDestructive: (_input?: unknown) =&gt; false,        // assume reversible
  checkPermissions: (
    input: { [key: string]: unknown },
    _ctx?: ToolUseContext,
  ): Promise&lt;PermissionResult&gt; =&gt;
    Promise.resolve({ behavior: 'allow', updatedInput: input }),  // defer to general system
  userFacingName: (_input?: unknown) =&gt; '',
}

export function buildTool&lt;D extends AnyToolDef&gt;(def: D): BuiltTool&lt;D&gt; {
  return {
    ...TOOL_DEFAULTS,
    userFacingName: () =&gt; def.name,
    ...def,  // tool-specific overrides win
  } as BuiltTool&lt;D&gt;
}</code></pre><p>The defaults are deliberately pessimistic. A new tool that forgets to declare <code>isConcurrencySafe: true</code> will run serially &#8212; slower, but safe. A tool that forgets <code>isDestructive: true</code> will skip the confirmation prompt &#8212; a gap, but the permission system still applies. The direction of failure is toward caution.</p><h3>Zod inputSchema: Compile-Time + Runtime Safety</h3><pre><code>// src/tools/AgentTool/AgentTool.tsx
// Zod schema serves two purposes simultaneously:
// 1. TypeScript infers the input type at compile time (z.infer&lt;typeof baseInputSchema&gt;)
// 2. The harness validates the JSON payload at runtime before calling the tool
const baseInputSchema = lazySchema(() =&gt; z.object({
  description: z.string().describe('A short (3-5 word) description of the task'),
  prompt: z.string().describe('The task for the agent to perform'),
  // Optional fields with explicit types &#8212; no implicit any
  subagent_type: z.string().optional().describe('The type of specialized agent to use'),
  model: z.enum(['sonnet', 'opus', 'haiku']).optional().describe('Optional model override'),
  run_in_background: z.boolean().optional().describe('Set to true to run in background'),
}))</code></pre><p><code>lazySchema</code> defers construction to break circular dependencies between tools that can spawn each other. The <code>.describe()</code> calls do double duty: they document the field for the model in the system prompt, and they appear in error messages when validation fails.</p><h3>Behavioral Declarations</h3><pre><code>// src/Tool.ts &#8212; the full behavioral surface of a tool
isConcurrencySafe(input: z.infer&lt;Input&gt;): boolean
// True &#8594; harness can batch this with other concurrent-safe tools
// False (default) &#8594; harness runs this serially

isReadOnly(input: z.infer&lt;Input&gt;): boolean
// True &#8594; permission system can auto-approve without user confirmation
// False (default) &#8594; requires permission evaluation

isDestructive?(input: z.infer&lt;Input&gt;): boolean
// True &#8594; requires explicit user confirmation even in auto-approve modes
// Optional &#8212; defaults to false via TOOL_DEFAULTS</code></pre><p>These are methods, not static flags, because the answer can depend on the input. A <code>FileWrite</code> tool writing to <code>/tmp</code> might be non-destructive; writing to <code>/etc/hosts</code> is destructive. The harness calls these methods with the validated input before making any execution decision.</p><h3>checkPermissions: Tool-Specific Safety Rules</h3><pre><code>// src/tools/AgentTool/AgentTool.tsx
// Tool-specific permission logic runs after the general permission system.
// Here, AgentTool auto-approves in most modes but defers to the classifier in auto mode.
async checkPermissions(input, context): Promise&lt;PermissionResult&gt; {
  const appState = context.getAppState()

  if (appState.toolPermissionContext.mode === 'auto') {
    return {
      behavior: 'passthrough',  // let the classifier decide
      message: 'Agent tool requires permission to spawn sub-agents.'
    }
  }
  
  return {
    behavior: 'allow',
    updatedInput: input  // can modify input before execution (e.g. normalize paths)
  }
}</code></pre><h3>maxResultSizeChars: Preventing Context Explosions</h3><pre><code>// src/Tool.ts
/**
 * Maximum size in characters for tool result before it gets persisted to disk.
 * When exceeded, the result is saved to a file and Claude receives a preview
 * with the file path instead of the full content.
 */
maxResultSizeChars: number</code></pre><p>Without this limit, a single grep across a large codebase could return enough text to exhaust the context window. The harness truncates at the limit, saves the full output to a temp file, and gives the model a preview plus the path. The model can then use <code>FileRead</code> to examine specific sections.</p><h2>3. Hermes Agent Implementation</h2><p>Hermes uses a central registry singleton instead of a type system. Tools register themselves at module import time, and the registry handles schema retrieval, availability checking, and dispatch.</p><h3>registry.register(): The Registration Pattern</h3><pre><code># hermes-agent/tools/registry.py
# Tools call this at module level &#8212; registration happens on import, not on first use.
# This means the registry is fully populated before any agent loop starts.
registry.register(
    name="read_file",           # tool name the model uses in tool_use blocks
    toolset="file",             # logical group (used by toolsets.py for bundling)
    schema={                    # JSON Schema &#8212; runtime validation only, no compile-time types
        "name": "read_file",
        "description": "Read a file with pagination and line numbers.",
        "parameters": {
            "type": "object",
            "properties": {
                "path":   {"type": "string", "description": "File path to read"},
                "offset": {"type": "integer", "description": "Start line (1-indexed)", "default": 1},
                "limit":  {"type": "integer", "description": "Max lines to return", "default": 500},
            },
            "required": ["path"],
        },
    },
    handler=read_file_tool,     # callable that executes the tool
    check_fn=None,              # None = always available; lambda returning bool for conditional tools
    requires_env=[],            # env vars that must be set for this tool to work
)</code></pre><p>The <code>check_fn</code> is the availability guard. When <code>get_definitions()</code> builds the tool list for the model, it calls each tool's <code>check_fn</code> and silently omits tools whose check returns <code>False</code>. This is how Hermes gates tools on environment conditions &#8212; a web search tool might check for an API key, a Home Assistant tool checks for <code>HASS_TOKEN</code>.</p><h3>JSON Schema: Runtime Validation Only</h3><pre><code># hermes-agent/tools/registry.py
def get_definitions(self, tool_names: Set[str], quiet: bool = False) -&gt; List[dict]:
    """Return OpenAI-format tool schemas for the requested tool names.
    
    Only tools whose check_fn() returns True (or have no check_fn) are included.
    The model never sees tools that aren't available &#8212; no confusing error messages.
    """
    result = []
    check_results: Dict[Callable, bool] = {}
    for name in sorted(tool_names):
        entry = self._tools.get(name)
        if not entry:
            continue
        if entry.check_fn:
            # Cache check results &#8212; multiple tools in the same toolset share a check_fn
            if entry.check_fn not in check_results:
                try:
                    check_results[entry.check_fn] = bool(entry.check_fn())
                except Exception:
                    check_results[entry.check_fn] = False  # fail closed
            if not check_results[entry.check_fn]:
                continue  # silently omit unavailable tools
        schema_with_name = {**entry.schema, "name": entry.name}
        result.append({"type": "function", "function": schema_with_name})
    return result</code></pre><p>Unlike Zod, JSON Schema gives you no compile-time guarantees. The model's JSON payload is validated by the LLM API layer (OpenAI/Anthropic format), not by Hermes itself. Hermes trusts that if the model followed the schema description, the handler will receive valid arguments.</p><h3>Global Concurrency Sets: <em>PARALLEL</em>SAFE<em>TOOLS and </em>NEVER<em>PARALLEL</em>TOOLS</h3><pre><code># hermes-agent/run_agent.py
# Tools that must NEVER run concurrently &#8212; interactive or user-facing tools
# that would produce confusing interleaved output.
_NEVER_PARALLEL_TOOLS = frozenset({"clarify"})

# Read-only tools with no shared mutable session state.
# These are safe to run in parallel because they don't modify anything.
_PARALLEL_SAFE_TOOLS = frozenset({
    "ha_get_state",
    "ha_list_entities",
    "ha_list_services",
    "read_file",
    "search_files",
    "session_search",
    "skill_view",
    "skills_list",
    "vision_analyze",
    "web_extract",
    "web_search",
})

# File tools can run concurrently only when they target independent paths.
# Two read_file calls on different files are safe; two write_file calls on
# the same file are not.
_PATH_SCOPED_TOOLS = frozenset({"read_file", "write_file", "patch"})</code></pre><p>This is a global declaration, not a per-tool property. The <code>_should_parallelize_tool_batch()</code> function checks these sets at runtime to decide whether a batch of tool calls can run concurrently. If any tool in the batch is in <code>_NEVER_PARALLEL_TOOLS</code>, the whole batch runs serially. If any tool is not in <code>_PARALLEL_SAFE_TOOLS</code> (and not in <code>_PATH_SCOPED_TOOLS</code>), the batch runs serially.</p><h3>File Tool Implementation: Read-Size Guard</h3><pre><code># hermes-agent/tools/file_tools.py
# Character-count guard prevents context explosions from large file reads.
# 100K chars &#8776; 25-35K tokens across typical tokenizers &#8212; a safe proxy
# when you don't know which model you're talking to.
_DEFAULT_MAX_READ_CHARS = 100_000

def read_file_tool(path: str, offset: int = 1, limit: int = 500, task_id: str = "default") -&gt; str:
    # ...
    content_len = len(result.content or "")
    max_chars = _get_max_read_chars()  # configurable via config.yaml
    if content_len &gt; max_chars:
        total_lines = result_dict.get("total_lines", "unknown")
        return json.dumps({
            "error": (
                f"Read produced {content_len:,} characters which exceeds "
                f"the safety limit ({max_chars:,} chars). "
                "Use offset and limit to read a smaller section. "
                f"The file has {total_lines} lines total."
            ),
            "path": path,
            "total_lines": total_lines,
        }, ensure_ascii=False)</code></pre><p>This is Hermes's equivalent of <code>maxResultSizeChars</code> &#8212; a hard cap on how much content a single tool call can inject into context. The limit is configurable per deployment via <code>config.yaml</code>, which matters when you're running against models with different context window sizes.</p><h2>4. Side-by-Side Comparison</h2><div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" href="https://substackcdn.com/image/fetch/$s_!XPOv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1a62fc76-21ae-41e8-ab43-a9ecf89d0965_1045x615.png" target="_blank"><div class="image2-inset"><source type="image/webp" /><img alt="Comparison table" class="sizing-normal" height="615" src="https://substackcdn.com/image/fetch/$s_!XPOv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1a62fc76-21ae-41e8-ab43-a9ecf89d0965_1045x615.png" title="Comparison table" width="1045" /><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset"><button class="pencraft pc-reset pencraft icon-container restack-image" tabindex="0" type="button"><svg fill="none" height="20" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><g><title></title><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button class="pencraft pc-reset pencraft icon-container view-image" tabindex="0" type="button"><svg class="lucide lucide-maximize2 lucide-maximize-2" fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button></div></div></div></a></figure></div><h2>5. When to Use Which</h2><p></p>
      <p>
          <a href="https://kenhuangus.substack.com/p/chapter-2-tool-architecture-and-the">
              Read more
          </a>
      </p>
