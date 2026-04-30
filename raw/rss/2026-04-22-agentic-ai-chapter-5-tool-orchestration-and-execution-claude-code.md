---
source: farmer/rss
feed: agentic-ai
farmed: 2026-04-30T00:00:00+00:00
title: "Chapter 5: Tool Orchestration and Execution (Claude Code vs. Hermes Agent)"
url: https://kenhuangus.substack.com/p/chapter-5-tool-orchestration-and
published: 2026-04-22
author: Ken Huang
---

# Chapter 5: Tool Orchestration and Execution (Claude Code vs. Hermes Agent)

<p></p><h2>1. Pattern Summary</h2><p>Tool orchestration is the layer between "the model wants to call 5 tools" and "those 5 tools actually execute safely and efficiently." It decides which tools can run in parallel, which must run serially, and what happens when a tool fails mid-batch. Without it, an agent either serializes everything (slow) or parallelizes everything (dangerous) &#8212; orchestration is the logic that threads the needle between those two failure modes, and it's what separates a production harness from a weekend prototype.</p><h2>2. Claude Code Implementation</h2><p>Claude Code's orchestration layer lives in <code>toolOrchestration.ts</code> and is built around a single key insight: group tool calls into batches by concurrency safety, then run each batch either fully parallel or fully serial.</p><h3>partitionToolCalls</h3><p>The partitioning function uses a reduce over the tool_use blocks, calling <code>isConcurrencySafe()</code> on each tool's parsed input. Adjacent safe tools get merged into the same batch; any unsafe tool starts a new serial batch.</p><pre><code>// src/services/tools/toolOrchestration.ts
// Groups tool_use blocks into concurrent or serial batches.
// Conservative: if parsing fails or isConcurrencySafe() throws, defaults to serial.
function partitionToolCalls(
  toolUseMessages: ToolUseBlock[],
  toolUseContext: ToolUseContext,
): Batch[] {
  return toolUseMessages.reduce((acc: Batch[], toolUse) =&gt; {
    const tool = findToolByName(toolUseContext.options.tools, toolUse.name)
    const parsedInput = tool?.inputSchema.safeParse(toolUse.input)

    const isConcurrencySafe = parsedInput?.success
      ? (() =&gt; {
          try { return Boolean(tool?.isConcurrencySafe(parsedInput.data)) }
          catch { return false }
        })()
      : false

    // Merge into the last batch if it's also concurrent; otherwise start a new one
    if (isConcurrencySafe &amp;&amp; acc[acc.length - 1]?.isConcurrencySafe) {
      acc[acc.length - 1]!.blocks.push(toolUse)
    } else {
      acc.push({ isConcurrencySafe, blocks: [toolUse] })
    }
    return acc
  }, [])
}</code></pre><p>For a sequence like <code>Read, Read, Write, Read, Bash(rm)</code>, this produces four batches: <code>[Read, Read]</code> concurrent, <code>[Write]</code> serial, <code>[Read]</code> concurrent, <code>[Bash]</code> serial. Two reads run together; the destructive command runs alone.</p><h3>runToolsConcurrently</h3><p>Concurrent batches use an <code>all</code> async generator that yields results out-of-order as they complete &#8212; so a 1-second tool doesn't wait behind a 5-second tool.</p><pre><code>// src/services/tools/toolOrchestration.ts
// Runs all tools in the batch simultaneously, up to CLAUDE_CODE_MAX_TOOL_USE_CONCURRENCY workers.
// Results stream out as each tool finishes, not in input order.
async function* runToolsConcurrently(
  toolUseMessages: ToolUseBlock[],
  assistantMessages: AssistantMessage[],
  canUseTool: CanUseToolFn,
  toolUseContext: ToolUseContext,
): AsyncGenerator&lt;MessageUpdateLazy, void&gt; {
  yield* all(
    toolUseMessages.map(async function* (toolUse) {
      // Mark as in-progress for UI tracking
      toolUseContext.setInProgressToolUseIDs(prev =&gt; new Set(prev).add(toolUse.id))
      yield* runToolUse(toolUse, /* ... */, canUseTool, toolUseContext)
      markToolUseAsComplete(toolUseContext, toolUse.id)
    }),
    getMaxToolUseConcurrency(), // reads CLAUDE_CODE_MAX_TOOL_USE_CONCURRENCY, default 10
  )
}</code></pre><h3>runToolsSerially</h3><p>Serial batches apply context modifiers immediately after each tool, so the next tool sees the updated state (e.g., a changed working directory).</p><pre><code>// src/services/tools/toolOrchestration.ts
// Runs tools one at a time. Context changes (like cwd updates) apply before the next tool.
async function* runToolsSerially(/* ... */): AsyncGenerator&lt;MessageUpdate, void&gt; {
  let currentContext = toolUseContext
  for (const toolUse of toolUseMessages) {
    for await (const update of runToolUse(toolUse, /* ... */, currentContext)) {
      if (update.contextModifier) {
        // Apply immediately &#8212; next tool in the loop sees this change
        currentContext = update.contextModifier.modifyContext(currentContext)
      }
      yield { message: update.message, newContext: currentContext }
    }
  }
}</code></pre><h3>StreamingToolExecutor and yieldMissingToolResultBlocks</h3><p>The <code>StreamingToolExecutor</code> starts executing tools as their blocks arrive during streaming, rather than waiting for the full response. When the user interrupts mid-execution, <code>yieldMissingToolResultBlocks</code> generates synthetic <code>tool_result</code> error blocks for any tool<em>use that never completed &#8212; maintaining the invariant that every `tool</em>use<code> has a matching </code>tool_result`.</p><pre><code>// src/query.ts
// Generates error tool_results for any tool_use that was interrupted before completing.
// Without this, the model would see orphaned tool_use blocks and get confused.
function* yieldMissingToolResultBlocks(
  assistantMessages: AssistantMessage[],
  errorMessage: string,
) {
  for (const assistantMessage of assistantMessages) {
    const toolUseBlocks = /* filter content for tool_use blocks */
    for (const toolUse of toolUseBlocks) {
      yield createUserMessage({
        content: [{
          type: 'tool_result',
          content: errorMessage,  // e.g. "Interrupted by user"
          is_error: true,
          tool_use_id: toolUse.id,
        }],
      })
    }
  }
}</code></pre><p>The design choices here are deliberate: concurrency is opt-in per tool (via <code>isConcurrencySafe</code>), the worker limit is externally configurable, and context propagation is deferred for concurrent batches to keep ordering deterministic.</p><h2>3. Hermes Agent Implementation</h2><p>Hermes takes a heuristic approach: instead of per-tool declarations, it maintains global sets of known-safe and known-unsafe tool names, then adds path-overlap detection for file tools.</p><h3><em>should</em>parallelize<em>tool</em>batch()</h3><pre><code># hermes-agent/run_agent.py

# Tools that must never run concurrently &#8212; interactive or user-facing.
_NEVER_PARALLEL_TOOLS = frozenset({"clarify"})

# Read-only tools with no shared mutable session state &#8212; safe to parallelize.
_PARALLEL_SAFE_TOOLS = frozenset({
    "ha_get_state", "ha_list_entities", "ha_list_services",
    "read_file", "search_files", "session_search", "skill_view",
    "skills_list", "vision_analyze", "web_extract", "web_search",
})

# File tools that can run concurrently only when targeting independent paths.
_PATH_SCOPED_TOOLS = frozenset({"read_file", "write_file", "patch"})

# Hard cap on concurrent worker threads.
_MAX_TOOL_WORKERS = 8

def _should_parallelize_tool_batch(tool_calls) -&gt; bool:
    """Return True when a tool-call batch is safe to run concurrently."""
    if len(tool_calls) &lt;= 1:
        return False  # No point parallelizing a single tool

    tool_names = [tc.function.name for tc in tool_calls]

    # Any never-parallel tool in the batch forces serial execution
    if any(name in _NEVER_PARALLEL_TOOLS for name in tool_names):
        return False

    reserved_paths: list[Path] = []
    for tool_call in tool_calls:
        tool_name = tool_call.function.name
        try:
            function_args = json.loads(tool_call.function.arguments)
        except Exception:
            return False  # Unparseable args &#8594; default to serial (safe)

        if tool_name in _PATH_SCOPED_TOOLS:
            scoped_path = _extract_parallel_scope_path(tool_name, function_args)
            if scoped_path is None:
                return False
            # Reject if this path overlaps with any already-reserved path
            if any(_paths_overlap(scoped_path, existing) for existing in reserved_paths):
                return False
            reserved_paths.append(scoped_path)
            continue

        if tool_name not in _PARALLEL_SAFE_TOOLS:
            return False  # Unknown tool &#8594; serial

    return True</code></pre><h3><em>paths</em>overlap()</h3><pre><code># hermes-agent/run_agent.py
# Prevents two file tools from running concurrently if one path is a prefix of the other.
# e.g., read_file("/etc") and read_file("/etc/passwd") would overlap.
def _paths_overlap(left: Path, right: Path) -&gt; bool:
    """Return True when two paths may refer to the same subtree."""
    left_parts = left.parts
    right_parts = right.parts
    common_len = min(len(left_parts), len(right_parts))
    # If one path is a prefix of the other, they overlap
    return left_parts[:common_len] == right_parts[:common_len]</code></pre><h3>ThreadPoolExecutor</h3><p>When <code>_should_parallelize_tool_batch()</code> returns True, Hermes dispatches all tools to a <code>ThreadPoolExecutor</code> and waits for all futures to complete before processing results.</p><pre><code># hermes-agent/run_agent.py
# Parallel execution path &#8212; all tools in the batch run simultaneously.
max_workers = min(num_tools, _MAX_TOOL_WORKERS)  # Never exceed 8 workers
with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
    futures = []
    for i, (tc, name, args) in enumerate(parsed_calls):
        # Each tool call is submitted as an independent future
        f = executor.submit(_run_tool, i, tc, name, args)
        futures.append(f)
    # Block until all tools complete (errors captured inside _run_tool)
    concurrent.futures.wait(futures)
# Results are collected in order after all futures finish</code></pre><h3>process_registry.py</h3><p>For tools that spawn background processes (via <code>terminal(background=true)</code>), Hermes uses a <code>ProcessRegistry</code> singleton that tracks every spawned process across the agent's lifetime.</p><pre><code># hermes-agent/tools/process_registry.py
# Global registry &#8212; thread-safe, survives across agent turns.
class ProcessRegistry:
    """In-memory registry of running and finished background processes.
    
    Provides: output buffering (200KB rolling window), status polling,
    blocking wait with interrupt support, kill, and crash recovery via
    JSON checkpoint file.
    """
    def __init__(self):
        self._running: Dict[str, ProcessSession] = {}
        self._finished: Dict[str, ProcessSession] = {}
        self._lock = threading.Lock()
        # Processes with notify_on_complete push here on exit,
        # triggering a new agent turn automatically.
        self.completion_queue: queue.Queue = queue.Queue()

    def spawn_local(self, command: str, ...) -&gt; ProcessSession:
        # Spawns via subprocess.Popen with a reader thread for live output
        ...

    def poll(self, session_id: str) -&gt; dict:
        # Non-blocking status check &#8212; returns output preview + exit code
        ...

    def wait(self, session_id: str, timeout: int = None) -&gt; dict:
        # Blocking wait with interrupt support (checks _interrupt_event)
        ...</code></pre><p>The <code>completion_queue</code> is particularly useful for long-running background tasks: when a process exits, it pushes a completion event that the CLI loop drains to auto-trigger a new agent turn with the results.</p><h2>4. Side-by-Side Comparison</h2><div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" href="https://substackcdn.com/image/fetch/$s_!FB4F!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F630b2f15-e03e-4ff7-b59d-56fd1ac13e13_1049x541.png" target="_blank"><div class="image2-inset"><source type="image/webp" /><img alt="Comparison table" class="sizing-normal" height="541" src="https://substackcdn.com/image/fetch/$s_!FB4F!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F630b2f15-e03e-4ff7-b59d-56fd1ac13e13_1049x541.png" title="Comparison table" width="1049" /><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset"><button class="pencraft pc-reset pencraft icon-container restack-image" tabindex="0" type="button"><svg fill="none" height="20" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><g><title></title><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button class="pencraft pc-reset pencraft icon-container view-image" tabindex="0" type="button"><svg class="lucide lucide-maximize2 lucide-maximize-2" fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button></div></div></div></a></figure></div><h2>5. When to Use Which</h2><p></p>
      <p>
          <a href="https://kenhuangus.substack.com/p/chapter-5-tool-orchestration-and">
              Read more
          </a>
      </p>