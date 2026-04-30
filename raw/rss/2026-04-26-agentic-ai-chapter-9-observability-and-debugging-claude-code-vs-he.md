---
source: farmer/rss
feed: agentic-ai
farmed: 2026-04-30T00:00:00+00:00
title: "Chapter 9: Observability and Debugging (Claude Code vs. Hermes Agent)"
url: https://kenhuangus.substack.com/p/chapter-9-observability-and-debugging
published: 2026-04-26
author: Ken Huang
---

# Chapter 9: Observability and Debugging (Claude Code vs. Hermes Agent)

<h2>1. Pattern Summary</h2><p>Observability is how you know what your agent is doing, why it made each decision, and what went wrong when it fails. Without it, debugging a multi-turn agent is archaeology &#8212; you're sifting through opaque state trying to reconstruct a sequence of events that already happened. A well-instrumented agent harness emits structured events at every decision point, tracks execution chains across turns and subagents, profiles latency at key checkpoints, and saves enough context that any failure can be replayed and understood after the fact. The two harnesses examined here &#8212; Claude Code and Hermes Agent &#8212; solve this problem from different angles: Claude Code builds a distributed tracing model into the query loop itself, while Hermes Agent prioritizes structured file logging and JSONL trajectory capture for post-hoc analysis and training data generation.</p><h2>2. Claude Code Implementation</h2><h3>Structured Logging with PII-Safe Analytics</h3><p>Every significant event in Claude Code is logged via <code>logEvent()</code> with a branded metadata type that prevents accidental PII or filepath leakage into analytics:</p><pre><code>// src/services/analytics/index.js
// The branded type forces explicit casting &#8212; you can't pass a raw string.
// This is a compile-time guarantee that analytics fields are safe to ship.
export type AnalyticsMetadata_I_VERIFIED_THIS_IS_NOT_CODE_OR_FILEPATHS = string &amp; {
  readonly __analyticsMetadata: unique symbol
}

// Usage: agent selection event with safe metadata fields
logEvent('tengu_agent_tool_selected', {
  agent_type: selectedAgent.agentType as AnalyticsMetadata_I_VERIFIED_THIS_IS_NOT_CODE_OR_FILEPATHS,
  model: resolvedAgentModel as AnalyticsMetadata_I_VERIFIED_THIS_IS_NOT_CODE_OR_FILEPATHS,
  is_async: run_in_background === true,
  is_fork: isForkPath
})</code></pre><p>The explicit cast is the enforcement mechanism. A developer who wants to log a filepath or code snippet has to write the full type name &#8212; which reads as a self-documenting assertion that they've verified the value is safe. This is a clever use of TypeScript's type system as a compliance guardrail.</p><h3>Query Chain IDs: Distributed Tracing Across Turns</h3><p>Every query gets a <code>chainId</code> and a <code>depth</code>, enabling end-to-end tracing from the initial user message through all turns and subagent spawns:</p><pre><code>// src/query.ts
// If a parent query exists, inherit its chainId and increment depth.
// If this is a root query, generate a fresh UUID at depth 0.
const queryTracking = toolUseContext.queryTracking
  ? {
      chainId: toolUseContext.queryTracking.chainId,
      depth: toolUseContext.queryTracking.depth + 1,
    }
  : {
      chainId: deps.uuid(),
      depth: 0,
    }

// Cast to analytics-safe type before including in any event
const queryChainIdForAnalytics =
  queryTracking.chainId as AnalyticsMetadata_I_VERIFIED_THIS_IS_NOT_CODE_OR_FILEPATHS</code></pre><p>This creates a causal chain: the root query is depth 0, any subagent it spawns is depth 1, and so on. By filtering analytics for a single <code>chainId</code>, you can reconstruct the full execution tree of a complex multi-agent conversation.</p><h3>Headless Profiler Checkpoints</h3><p>Latency is measured at named checkpoints throughout the query lifecycle:</p><pre><code>// src/utils/headlessProfiler.js
// Checkpoints bracket every expensive phase &#8212; system prompt, skills, API, tools.
headlessProfilerCheckpoint('before_getSystemPrompt')
// ... fetch system prompt ...
headlessProfilerCheckpoint('after_getSystemPrompt')

headlessProfilerCheckpoint('query_api_streaming_start')
// ... stream API response ...
headlessProfilerCheckpoint('query_api_streaming_end')

headlessProfilerCheckpoint('query_tool_execution_start')
// ... execute tool calls ...
headlessProfilerCheckpoint('query_tool_execution_end')</code></pre><p>The checkpoint names are self-documenting. By diffing timestamps between paired checkpoints, you get the duration of each phase without any instrumentation inside the phase itself. This is particularly useful for identifying whether slowness is in the API call, the tool execution, or the system prompt generation.</p><h3>Continue Sites: The Debug Trail for Multi-Turn Loops</h3><p>The query loop's <code>transition.reason</code> field records exactly why each loop iteration continued, turning multi-turn debugging from guesswork into a readable audit trail:</p><pre><code>// src/query.ts
// Every continue site sets a named reason &#8212; this becomes the debug trail.
state = {
  messages: drained.messages,
  toolUseContext,
  autoCompactTracking: tracking,
  transition: { reason: 'collapse_drain_retry', committed: drained.committed },
}
continue

// Other transition reasons in the codebase:
// 'multi_turn_continue'     &#8212; normal tool-use continuation
// 'reactive_compact_retry'  &#8212; context was compacted, retrying
// 'collapse_drain_retry'    &#8212; context collapsed, draining and retrying</code></pre><p>When a conversation takes an unexpected path, you search the logs for <code>transition.reason</code> and read the sequence. Each entry is a single sentence explaining why the loop didn't stop.</p><h3>SDK Event Queue and EDE Diagnostics</h3><p>For SDK consumers, task completion events are queued with full usage metadata:</p><pre><code>// src/utils/sdkEventQueue.js
// Notify SDK consumers of task completion with token and timing data
enqueueSdkEvent({
  type: 'system',
  subtype: 'task_notification',
  status: syncAgentError ? 'failed' : wasAborted ? 'stopped' : 'completed',
  usage: {
    total_tokens: progress.tokenCount,
    tool_uses: progress.toolUseCount,
    duration_ms: Date.now() - agentStartTime
  }
})</code></pre><p>When errors occur, the EDE (Error Diagnostic Event) prefix provides structured context:</p><pre><code>// src/QueryEngine.ts
// EDE prefix: result_type, last_content_type, stop_reason &#8212; enough to triage
// without reading the full conversation transcript.
errors: [
  `[ede_diagnostic] result_type=${edeResultType} last_content_type=${edeLastContentType} stop_reason=${lastStopReason}`,
  ...all.slice(start).map(_ =&gt; _.error),
]</code></pre><p>The <code>result_type</code> tells you whether the last message was from the assistant or user. <code>last_content_type</code> tells you what kind of content block ended the conversation. <code>stop_reason</code> gives the API's own assessment. Together, these three fields usually tell you what went wrong without needing to inspect the full message history.</p><h2>3. Hermes Agent Implementation</h2><h3>Structured Logging with Session Correlation</h3><p>Hermes uses Python's standard <code>logging</code> module with rotating file handlers and a <code>RedactingFormatter</code> that strips secrets before they hit disk:</p><pre><code># hermes-agent/hermes_logging.py

def setup_logging(*, hermes_home=None, log_level=None, ...):
    """Single entry point for all logging setup &#8212; CLI and gateway both call this."""
    from agent.redact import RedactingFormatter  # strips API keys, tokens, etc.

    # agent.log: INFO+ &#8212; the main activity log for all tool/session events
    _add_rotating_handler(
        root,
        log_dir / "agent.log",
        level=level,
        max_bytes=max_bytes,
        formatter=RedactingFormatter(_LOG_FORMAT),
    )

    # errors.log: WARNING+ &#8212; quick triage, smaller rotation window
    _add_rotating_handler(
        root,
        log_dir / "errors.log",
        level=logging.WARNING,
        max_bytes=2 * 1024 * 1024,
        formatter=RedactingFormatter(_LOG_FORMAT),
    )

    # Silence noisy third-party loggers (httpx, openai, grpc, etc.)
    for name in _NOISY_LOGGERS:
        logging.getLogger(name).setLevel(logging.WARNING)</code></pre><p>The two-file split is practical: <code>agent.log</code> is the full record, <code>errors.log</code> is the fast triage view. The <code>RedactingFormatter</code> is the PII/secret protection layer &#8212; analogous to Claude Code's branded analytics type, but applied at write time rather than compile time.</p><h3>JSONL Trajectory Saving</h3><p>Hermes saves every completed conversation as a JSONL entry, enabling post-incident replay and training data generation:</p><pre><code># hermes-agent/agent/trajectory.py

def save_trajectory(trajectory, model, completed, filename=None):
    """Append one conversation to a JSONL file.

    trajectory: ShareGPT-format list of turns
    completed: True = trajectory_samples.jsonl, False = failed_trajectories.jsonl
    """
    # Route to different files based on success &#8212; failed runs are kept separate
    # so they can be analyzed for failure modes without polluting training data.
    if filename is None:
        filename = "trajectory_samples.jsonl" if completed else "failed_trajectories.jsonl"

    entry = {
        "conversations": trajectory,   # full turn-by-turn record
        "timestamp": datetime.now().isoformat(),
        "model": model,
        "completed": completed,
    }

    # Append-only write &#8212; each line is a self-contained JSON object
    with open(filename, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")</code></pre><p>The JSONL format is append-only and self-describing &#8212; each line is a complete record. Failed trajectories go to a separate file, which is a simple but effective way to separate training signal from failure analysis. The <code>convert_scratchpad_to_think()</code> helper normalizes reasoning tags before saving, ensuring the trajectory format is consistent regardless of which model produced it.</p><h3>Real-Time Error Detection with <code>_detect_tool_failure</code></h3><p>Hermes inspects every tool result in real time to surface failures immediately in the CLI:</p><pre><code># hermes-agent/agent/display.py

def _detect_tool_failure(tool_name: str, result: str | None) -&gt; tuple[bool, str]:
    """Check a tool result for failure signals. Returns (is_failure, suffix)."""

    # Terminal tools: parse JSON result and check exit code
    if tool_name == "terminal":
        data = json.loads(result)
        exit_code = data.get("exit_code")
        if exit_code is not None and exit_code != 0:
            return True, f" [exit {exit_code}]"  # e.g. " [exit 1]"

    # Memory tool: distinguish capacity errors from real failures
    if tool_name == "memory":
        data = json.loads(result)
        if data.get("success") is False and "exceed the limit" in data.get("error", ""):
            return True, " [full]"  # memory full, not a crash

    # Generic heuristic: look for error signals in the first 500 chars
    lower = result[:500].lower()
    if '"error"' in lower or '"failed"' in lower or result.startswith("Error"):
        return True, " [error]"

    return False, ""</code></pre><p>This function is called by <code>get_cute_tool_message()</code> to annotate the CLI activity feed. A failed tool call gets a red prefix and an informational suffix like <code>[exit 1]</code> or <code>[error]</code> &#8212; the analyst sees the failure immediately without waiting for the model to report it.</p><h3>Cost Estimation Per Turn</h3><p><code>usage_pricing.py</code> provides structured cost tracking with a <code>CanonicalUsage</code> datatype that normalizes token counts across providers:</p><pre><code># hermes-agent/agent/usage_pricing.py

@dataclass(frozen=True)
class CanonicalUsage:
    """Normalized token usage &#8212; works across Anthropic, OpenAI, and OpenRouter."""
    input_tokens: int = 0
    output_tokens: int = 0
    cache_read_tokens: int = 0   # Anthropic prompt caching
    cache_write_tokens: int = 0
    reasoning_tokens: int = 0    # o1/o3 extended thinking
    request_count: int = 1

    @property
    def total_tokens(self) -&gt; int:
        # prompt_tokens includes cache reads/writes for accurate billing
        return self.prompt_tokens + self.output_tokens</code></pre><p>The frozen dataclass ensures usage records are immutable &#8212; you accumulate them by creating new instances, not by mutating state. This makes cost tracking safe to use across concurrent tool executions.</p><h3>KawaiiSpinner Activity Feed</h3><p>The <code>KawaiiSpinner</code> class provides real-time tool status in the CLI, with graceful degradation when stdout is not a terminal:</p><pre><code># hermes-agent/agent/display.py

class KawaiiSpinner:
    """Animated spinner with kawaii faces for CLI feedback during tool execution."""

    def _animate(self):
        # Non-TTY environments (Docker, systemd, pipes): log once and wait.
        # Avoids flooding logs with animation escape codes.
        if not self._is_tty:
            self._write(f"  [tool] {self.message}", flush=True)
            while self.running:
                time.sleep(0.5)
            return
        # TTY: animate with spinner frames and elapsed time</code></pre><p>The TTY check is the key design decision &#8212; the same spinner code works in interactive terminals and in headless/containerized deployments without configuration.</p><h2>4. Side-by-Side Comparison</h2><div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" href="https://substackcdn.com/image/fetch/$s_!nT2z!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe61d74a4-ec6b-4bad-b226-fe89e9a88af2_1022x423.png" target="_blank"><div class="image2-inset"><source type="image/webp" /><img alt="Comparison table" class="sizing-normal" height="423" src="https://substackcdn.com/image/fetch/$s_!nT2z!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe61d74a4-ec6b-4bad-b226-fe89e9a88af2_1022x423.png" title="Comparison table" width="1022" /><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset"><button class="pencraft pc-reset pencraft icon-container restack-image" tabindex="0" type="button"><svg fill="none" height="20" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><g><title></title><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button class="pencraft pc-reset pencraft icon-container view-image" tabindex="0" type="button"><svg class="lucide lucide-maximize2 lucide-maximize-2" fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button></div></div></div></a></figure></div><h2>5. When to Use Which</h2><p></p>
      <p>
          <a href="https://kenhuangus.substack.com/p/chapter-9-observability-and-debugging">
              Read more
          </a>
      </p>