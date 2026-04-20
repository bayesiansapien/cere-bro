---
source: farmer/rss
feed: agentic-ai
farmed: 2026-04-20T09:02:04.518593+00:00
title: Chapter 3: The Query / Agent Loop (Claude Code vs. Hermes Agent)
url: https://kenhuangus.substack.com/p/chapter-3-the-query-agent-loop-claude
published: 2026-04-20
author: Ken Huang
---

# Chapter 3: The Query / Agent Loop (Claude Code vs. Hermes Agent)

<h2>1. Pattern Summary</h2><p>The agent loop is the heartbeat of every autonomous agent. It drives the cycle of model call &#8594; tool execution &#8594; result injection &#8594; next model call, repeating until the model signals it is done or a termination condition fires. The design of this loop determines everything that matters in production: how the agent handles transient API errors, how it recovers from context overflow, how it knows when to stop, and how a post-mortem can reconstruct exactly what happened and why. Get the loop right and you get a resilient, debuggable agent. Get it wrong and you get an infinite retry spiral or a silent hang.</p><h2>2. Claude Code Implementation</h2><p>Claude Code's loop lives in <code>queryLoop()</code> inside <code>src/query.ts</code>. It is an async generator that runs <code>while (true)</code> and yields events as they happen &#8212; text deltas, tool results, error messages &#8212; rather than buffering everything and returning at the end.</p><h3>The State Type</h3><p>Every iteration of the loop reads from and writes to a <code>State</code> object:</p><pre><code>// src/query.ts &#8212; State carries mutable context between loop iterations.
// The `transition` field is the key: it records WHY the previous iteration
// continued, so the next one can make informed recovery decisions.
let state: State = {
  messages: params.messages,
  toolUseContext: params.toolUseContext,
  maxOutputTokensOverride: params.maxOutputTokensOverride,
  autoCompactTracking: undefined,
  stopHookActive: undefined,
  maxOutputTokensRecoveryCount: 0,
  hasAttemptedReactiveCompact: false,
  turnCount: 1,
  pendingToolUseSummary: undefined,
  transition: undefined,   // undefined on first iteration; named reason on all subsequent
}</code></pre><p>The <code>transition</code> field is what separates a naive retry loop from a state machine. When the loop continues, it stamps the reason onto <code>state.transition</code>. The next iteration reads that reason before deciding what to do. This prevents infinite loops: if <code>transition.reason === 'collapse_drain_retry'</code>, the next iteration skips the collapse drain and tries the next recovery strategy.</p><h3>The 7 Continue Sites</h3><p>The loop has exactly seven places where it can <code>continue</code> to the next iteration. Each one stamps a named reason:</p><pre><code>// Continue site 1 &#8212; context collapse drained staged collapses
// Cheapest recovery: archives old messages locally, no API call needed.
state = { messages: drained.messages, ..., transition: { reason: 'collapse_drain_retry', committed: drained.committed } }
continue

// Continue site 2 &#8212; reactive compact summarized old history via API
// More expensive: calls a fast model to summarize, then retries.
state = { messages: postCompactMessages, ..., transition: { reason: 'reactive_compact_retry' } }
continue

// Continue site 3 &#8212; escalated max output tokens to 64K
// Single-shot: retries the same request with a higher token ceiling.
state = { messages: messagesForQuery, ..., transition: { reason: 'max_output_tokens_escalate' } }
continue

// Continue site 4 &#8212; multi-turn recovery after hitting output token limit
// Injects a "resume without recap" user message and keeps going.
state = {
  messages: [...messagesForQuery, ...assistantMessages, recoveryMessage],
  maxOutputTokensRecoveryCount: maxOutputTokensRecoveryCount + 1,
  transition: { reason: 'max_output_tokens_recovery', attempt: maxOutputTokensRecoveryCount + 1 },
}
continue

// Continue site 5 &#8212; stop hook blocked continuation
// A post-turn hook returned blocking errors; inject them and retry.
state = {
  messages: [...messagesForQuery, ...assistantMessages, ...stopHookResult.blockingErrors],
  stopHookActive: true,
  transition: { reason: 'stop_hook_blocking' },
}
continue

// Continue site 6 &#8212; token budget pressure message injected
// Warns the model it is approaching its budget; asks it to wrap up.
state = {
  messages: [...messagesForQuery, ...assistantMessages, createUserMessage({...})],
  transition: { reason: 'token_budget_continuation' },
}
continue

// Continue site 7 &#8212; normal next turn after tool execution
// The happy path: tools ran, results appended, loop continues.
state = {
  messages: [...messagesForQuery, ...assistantMessages, ...toolResults],
  turnCount: nextTurnCount,
  maxOutputTokensRecoveryCount: 0,
  hasAttemptedReactiveCompact: false,
  transition: { reason: 'next_turn' },
}
continue</code></pre><h3>Async Generator Streaming</h3><p>The loop yields events as they arrive from the API. The caller sees text appear in real time:</p><pre><code>// src/query.ts &#8212; yield each streaming event immediately rather than buffering.
// This is what makes Claude Code feel responsive: the user sees output
// character-by-character, not in one big dump at the end.
for await (const message of deps.callModel({...})) {
  if (!withheld) {
    yield yieldMessage   // push to caller immediately
  }
  // ... collect tool_use blocks for execution
}</code></pre><p>The design choice here is deliberate: async generators compose naturally. The <code>submitMessage</code> method in <code>QueryEngine</code> is also an async generator, so the entire call stack from API response to UI update is non-blocking and incremental.</p><h2>3. Hermes Agent Implementation</h2><p>Hermes's loop lives in <code>run_conversation()</code> inside <code>run_agent.py</code>. It is synchronous &#8212; it returns a final string when done, not a stream. The loop condition is a double gate: iteration counter AND budget.</p><h3>The Loop Gate</h3><pre><code># run_agent.py &#8212; the main while loop.
# Two conditions must both be true to continue:
#   1. api_call_count &lt; self.max_iterations  (hard ceiling from config)
#   2. self.iteration_budget.remaining &gt; 0   (shared budget across parent + subagents)
while api_call_count &lt; self.max_iterations and self.iteration_budget.remaining &gt; 0:

    # Check for user interrupt before each iteration
    if self._interrupt_requested:
        interrupted = True
        break

    api_call_count += 1

    # consume() is the actual gate &#8212; thread-safe, returns False if exhausted.
    # This is the canonical check; the while condition is a fast pre-filter.
    if not self.iteration_budget.consume():
        self._safe_print(f"&#9888;&#65039;  Iteration budget exhausted ({self.iteration_budget.used}/{self.iteration_budget.max_total})")
        break</code></pre><h3>IterationBudget</h3><p>The <code>IterationBudget</code> class is a thread-safe counter that can be shared across a parent agent and its subagents:</p><pre><code># run_agent.py &#8212; IterationBudget is the shared resource that prevents
# runaway loops across the entire agent tree (parent + all children).
class IterationBudget:
    def __init__(self, max_total: int):
        self.max_total = max_total
        self._used = 0
        self._lock = threading.Lock()   # thread-safe for concurrent subagents

    def consume(self) -&gt; bool:
        """Try to consume one iteration. Returns True if allowed, False if exhausted."""
        with self._lock:
            if self._used &gt;= self.max_total:
                return False
            self._used += 1
            return True

    def refund(self) -&gt; None:
        """Return one iteration (used for programmatic tool calls that don't count)."""
        with self._lock:
            if self._used &gt; 0:
                self._used -= 1

    @property
    def remaining(self) -&gt; int:
        with self._lock:
            return max(0, self.max_total - self._used)</code></pre><p>Each <code>run_conversation()</code> call resets the budget at the start of the turn:</p><pre><code># run_agent.py &#8212; budget resets per conversation turn, not per session.
# This prevents subagent usage from a previous turn eating into the next one.
self.iteration_budget = IterationBudget(self.max_iterations)</code></pre><h3>Error Handling: Retry with Exponential Backoff</h3><p>Inside the loop, each API call is wrapped in its own <code>while retry_count &lt; max_retries</code> inner loop:</p><pre><code># run_agent.py &#8212; inner retry loop for transient API failures.
# Separate from the outer agent loop: retries are transparent to the
# conversation; the iteration counter only increments on success.
retry_count = 0
max_retries = 3

while retry_count &lt; max_retries:
    try:
        response = self._interruptible_streaming_api_call(api_kwargs, on_first_delta=_stop_spinner)
        break   # success &#8212; exit retry loop, continue agent loop
    except RateLimitError as e:
        # 429: back off and retry on the same iteration
        wait = min(2 ** retry_count * 5, 60)
        time.sleep(wait)
        retry_count += 1
    except Exception as e:
        # Non-retryable: surface to outer loop
        raise</code></pre><h3>Context Compression Trigger</h3><p>The <code>ContextCompressor</code> fires before the API call when token usage crosses 50% of the model's context window:</p><pre><code># run_agent.py &#8212; preflight compression check before entering the main loop.
# Handles the case where a loaded session already exceeds the threshold
# before the first API call of the new turn.
if self.compression_enabled and self.context_compressor.should_compress_preflight(messages):
    messages, active_system_prompt = self._compress_context(messages, ...)</code></pre><h2>4. Side-by-Side Comparison</h2><div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" href="https://substackcdn.com/image/fetch/$s_!1qZG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe51677cc-807c-4b26-984e-abe0602f84fb_1030x551.png" target="_blank"><div class="image2-inset"><source type="image/webp" /><img alt="Comparison table" class="sizing-normal" height="551" src="https://substackcdn.com/image/fetch/$s_!1qZG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe51677cc-807c-4b26-984e-abe0602f84fb_1030x551.png" title="Comparison table" width="1030" /><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset"><button class="pencraft pc-reset pencraft icon-container restack-image" tabindex="0" type="button"><svg fill="none" height="20" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><g><title></title><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button class="pencraft pc-reset pencraft icon-container view-image" tabindex="0" type="button"><svg class="lucide lucide-maximize2 lucide-maximize-2" fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button></div></div></div></a></figure></div><h2>5. When to Use Which</h2><p></p>
      <p>
          <a href="https://kenhuangus.substack.com/p/chapter-3-the-query-agent-loop-claude">
              Read more
          </a>
      </p>
