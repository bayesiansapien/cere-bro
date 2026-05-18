---
source: farmer/rss
feed: agentic-ai
farmed: 2026-05-18T03:44:44.080694+00:00
title: Chapter 2: Cancellation & Abort Propagation (Claude Code vs. Hermes Agent)
url: https://kenhuangus.substack.com/p/chapter-2-cancellation-and-abort
published: 2026-05-17
author: Ken Huang
---

# Chapter 2: Cancellation & Abort Propagation (Claude Code vs. Hermes Agent)

<p></p><h2>1. Pattern Summary</h2><p>Cancellation is the property that is important part of steering agent to stop or abort some actions. When a user hits Ctrl-C, when an upstream timeout fires, or when a moderation system flags a generation, the harness must stop end-to-end: the in-flight HTTP stream to the model must close, the spawned subprocess must die, the pending permission dialog must release, and the audit log must record what stopped. Anything less leaks resources &#8212; orphaned shell processes, stranded child agents, hung approval prompts, half-applied edits. The iteration-budget pattern caps <em>throughput</em>; cancellation governs <em>immediacy</em>. Both Claude Code and Hermes invest substantial machinery in making cancellation reach every leaf of the call tree, but they take fundamentally different routes &#8212; Claude Code threads <code>AbortController.signal</code> through every async boundary, while Hermes uses a thread-scoped interrupt flag that long-running tools poll cooperatively.</p><div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" href="https://substackcdn.com/image/fetch/$s_!_6sr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4eca6ee8-7bfc-4711-8dd8-cfd59b3ac252_1800x1080.png" target="_blank"><div class="image2-inset"><source type="image/webp" /><img alt="Figure 2.1: Cancellation propagation chain from user to leaves" class="sizing-normal" height="1080" src="https://substackcdn.com/image/fetch/$s_!_6sr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4eca6ee8-7bfc-4711-8dd8-cfd59b3ac252_1800x1080.png" title="Figure 2.1: Cancellation propagation chain from user to leaves" width="1800" /><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset"><button class="pencraft pc-reset pencraft icon-container restack-image" tabindex="0" type="button"><svg fill="none" height="20" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><g><title></title><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button class="pencraft pc-reset pencraft icon-container view-image" tabindex="0" type="button"><svg class="lucide lucide-maximize2 lucide-maximize-2" fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button></div></div></div></a></figure></div><p><em>Figure 2.1.</em> The four canonical entry points for a cancellation request &#8212; user Ctrl-C, SLA or budget timeout, queued priority message, and moderation policy &#8212; all converge on the harness's single public <code>interrupt()</code> method, which then fans out through a propagation primitive (an <code>AbortSignal</code> tree in Claude Code, a thread-scoped flag set in Hermes) to every leaf that holds external state: the model HTTP stream, spawned subprocesses, the sub-agent tree, pending permission dialogs, and the audit log. The pattern's invariant is that one abort at the root deterministically reaches every place that could leak resources or strand work.</p><p></p><p>Before you read on &#8212; two quick announcements. First, you can now get 50% off a yearly subscription and unlock all paid content on Agentic AI, AI Security, and more: <a href="https://kenhuangus.substack.com/subscribe?coupon=302342d9">https://kenhuangus.substack.com/subscribe?coupon=302342d9</a>.</p><p>Second, all previously written 15 Hermes Agent and Claude Code agentic harness design patterns are now available in a single book on Amazon: <a href="https://www.amazon.com/Agentic-AI-Harness-Pattern-Patterns-ebook/dp/B0H13XWS8W">https://www.amazon.com/Agentic-AI-Harness-Pattern-Patterns-ebook/dp/B0H13XWS8W</a></p><p></p><h2>2. Claude Code Implementation</h2><h3>2.1 The single owner: <code>QueryEngine.abortController</code></h3><p>Claude Code's cancellation contract is anchored at the harness core. Every <code>QueryEngine</code> instance owns one <code>AbortController</code>, created in the constructor and accepted optionally from the caller so an embedding application (REPL, SDK consumer, IDE plugin) can hold its own reference and abort from outside.</p><pre><code>// src/QueryEngine.ts (lines 156, 187, 200-207)
// QueryEngine owns one AbortController per session. The caller can pass
// their own (so the IDE/REPL holds the abort handle); otherwise we make one.
abortController?: AbortController
// ...
private abortController: AbortController

constructor(config: QueryEngineConfig) {
  this.config = config
  this.mutableMessages = config.initialMessages ?? []
  this.abortController = config.abortController ?? createAbortController()
  // ...
}</code></pre><p>Exposing the controller as a constructor parameter is what makes Claude Code embeddable. The print-mode CLI (<code>src/cli/print.ts</code>) installs a SIGINT handler that calls <code>abortController.abort()</code> directly without touching the QueryEngine internals.</p><h3>2.2 The public interrupt API</h3><p>The QueryEngine exposes a single method that any caller can use to request cancellation. It is a thin wrapper, but its narrow surface means the rest of the codebase has only one channel through which cancellation can enter the system.</p><pre><code>// src/QueryEngine.ts (lines 1158-1160)
interrupt(): void {
  this.abortController.abort()
}</code></pre><p>The simplicity is deliberate: every downstream consumer &#8212; the API client, every tool, every child agent &#8212; listens to <code>abortController.signal</code>, so calling <code>abort()</code> once propagates the cancellation everywhere automatically.</p><h3>2.3 Listener-limit hygiene</h3><p>A naive <code>new AbortController()</code> would leak listener warnings in long sessions because every tool, HTTP fetch, and child agent attaches its own <code>abort</code> listener. Claude Code wraps construction in a helper that bumps the per-signal listener cap up front.</p><pre><code>// src/utils/abortController.ts (lines 16-22)
export function createAbortController(
  maxListeners: number = DEFAULT_MAX_LISTENERS,
): AbortController {
  const controller = new AbortController()
  setMaxListeners(maxListeners, controller.signal)
  return controller
}</code></pre><p><code>DEFAULT_MAX_LISTENERS = 50</code> is sized for the typical agent turn &#8212; a handful of fetches, a dozen tool calls, plus permission dialogs and progress timers each subscribing for <code>abort</code> events.</p><h3>2.4 Child controllers for sub-agents and per-tool isolation</h3><p>When the harness fans out &#8212; spawning a sub-agent or running tools concurrently &#8212; each branch needs its own abort scope so that an error in one tool can cancel siblings without poisoning the whole session. Claude Code's <code>createChildAbortController</code> builds a child whose abort propagates <em>down</em> from the parent but not <em>up</em> unless explicitly bubbled.</p><pre><code>// src/utils/abortController.ts (lines 68-99, abridged for the propagation core)
export function createChildAbortController(
  parent: AbortController,
  maxListeners?: number,
): AbortController {
  const child = createAbortController(maxListeners)
  // Fast path: parent already aborted, no listener setup needed
  if (parent.signal.aborted) {
    child.abort(parent.signal.reason)
    return child
  }
  // WeakRef prevents the parent from keeping an abandoned child alive.
  const weakChild = new WeakRef(child)
  const weakParent = new WeakRef(parent)
  const handler = propagateAbort.bind(weakParent, weakChild)
  parent.signal.addEventListener('abort', handler, { once: true })
  return child
}</code></pre><p>The <code>WeakRef</code> discipline matters in long-running sessions: a parent that retained strong references to every spawned child controller would leak every short-lived sub-agent's tool-call closure for the lifetime of the conversation.</p><p>The streaming tool executor uses this child mechanism so a Bash error can cancel its sibling tools without aborting the entire query. The first half builds the child controller anchored to the per-batch sibling controller &#8212; the per-tool scope that lets one tool's failure abort its peers.</p><pre><code>// src/services/tools/StreamingToolExecutor.ts (lines 294-303)
// Per-tool child controller. Lets siblingAbortController kill running
// subprocesses (Bash spawns listen to this signal) when a Bash error
// cascades. Permission-dialog rejection also aborts this controller &#8212;
// that abort must bubble up to the query controller so the loop ends.
const toolAbortController = createChildAbortController(
  this.siblingAbortController,
)</code></pre><p>The second half wires up <em>upward</em> propagation: when the child aborts for any reason other than a peer-tool failure, the abort is bubbled to the query-level controller so the whole turn ends. This is the fix for a regression where a permission-rejected tool would silently send the rejection back to the model instead of aborting cleanly.</p><pre><code>// src/services/tools/StreamingToolExecutor.ts (lines 304-318)
toolAbortController.signal.addEventListener(
  'abort',
  () =&gt; {
    if (
      toolAbortController.signal.reason !== 'sibling_error' &amp;&amp;
      !this.toolUseContext.abortController.signal.aborted &amp;&amp;
      !this.discarded
    ) {
      this.toolUseContext.abortController.abort(
        toolAbortController.signal.reason,
      )
    }
  },
  { once: true },
)</code></pre><p>The <code>signal.reason</code> field carries the cancellation cause across the tree &#8212; <code>'interrupt'</code> for user Ctrl-C, <code>'sibling_error'</code> for a peer-tool failure, an Error object for permission denials. Downstream tools inspect the reason to decide whether to surface a retryable error, a hard abort, or a partial result.</p><h3>2.5 Subprocess cancellation: the Bash tool</h3><p>Cancellation only matters if it reaches the subprocess. Claude Code's BashTool threads the abort signal directly into its <code>exec</code> helper, which spawns the shell with the signal attached so a kernel-level kill follows automatically.</p><pre><code>// src/tools/BashTool/BashTool.tsx (lines 826-898, abridged)
async function* runShellCommand({
  input,
  abortController,
  // ...
}: {
  input: BashToolInput;
  abortController: AbortController;
  // ...
}) {
  const { command, timeout, run_in_background } = input;
  const timeoutMs = timeout || getDefaultTimeoutMs();
  // Pass abortController.signal directly to exec so the spawned
  // shell process is killed when the signal fires.
  const shellCommand = await exec(command, abortController.signal, 'bash', {
    timeout: timeoutMs,
    onProgress(/* ... */) { /* ... */ },
  });
  // ...
}</code></pre><p>Once the result is back, the BashTool reads <code>signal.reason</code> to distinguish a user-requested interrupt from a non-zero exit caused by the command itself. Surfacing the right reason matters because the model behaves differently on <code>'interrupt'</code> (don't retry) vs an exit-code failure (it might).</p><pre><code>// src/tools/BashTool/BashTool.tsx (line 684)
const isInterrupt = result.interrupted &amp;&amp; abortController.signal.reason === 'interrupt';</code></pre><h3>2.6 Streaming HTTP cancellation: the WebFetch and model client paths</h3><p>Closing a streaming HTTP response is the second leak vector. The WebFetch tool's <code>applyPromptToMarkdown</code> is the canonical example &#8212; it summarises a fetched page through a secondary Haiku call, and the signal threads through that secondary call too. The function signature shows how the signal is a first-class parameter: every async helper that touches the network takes one.</p><pre><code>// src/tools/WebFetchTool/utils.ts (lines 484-490)
export async function applyPromptToMarkdown(
  prompt: string,
  markdownContent: string,
  signal: AbortSignal,
  isNonInteractiveSession: boolean,
  isPreapprovedDomain: boolean,
): Promise&lt;string&gt; {</code></pre><p>Inside the body, the signal is forwarded to <code>queryHaiku</code> so the LLM stream itself is cancellable, and a post-await check throws <code>AbortError</code> if the abort fired while the response was buffering &#8212; the request completed, but the result must be discarded.</p><pre><code>// src/tools/WebFetchTool/utils.ts (lines 503-520, abridged)
const assistantMessage = await queryHaiku({
  systemPrompt: asSystemPrompt([]),
  userPrompt: modelPrompt,
  signal,
  options: { /* ... */ },
})
// We need to bubble this up, so that the tool call throws, causing us
// to return an is_error tool_use block to the server.
if (signal.aborted) {
  throw new AbortError()
}</code></pre><p>The post-await <code>signal.aborted</code> check catches the case where abort fired while the response was already buffering &#8212; the request itself completed but the result must be discarded.</p><h3>2.7 The signal entry points: SIGINT and message-queue priority</h3><p>The two main ways cancellation enters the system are an OS signal and a high-priority queued user message. Print mode (<code>claude -p</code>) installs its own SIGINT handler that aborts the in-flight controller before delegating to the global graceful-shutdown machinery.</p><pre><code>// src/cli/print.ts (lines 1023-1034)
// Ctrl+C in -p mode: abort the in-flight query, then shut down gracefully.
const sigintHandler = () =&gt; {
  logForDiagnosticsNoPII('info', 'shutdown_signal', { signal: 'SIGINT' })
  if (abortController &amp;&amp; !abortController.signal.aborted) {
    abortController.abort()
  }
  void gracefulShutdown(0)
}
process.on('SIGINT', sigintHandler)</code></pre><p>The interactive REPL takes a different route &#8212; when the user types a message tagged <code>'now'</code> priority, the message-queue subscriber aborts with reason <code>'interrupt'</code>, allowing the loop to distinguish a deliberate user interruption from a structural cancellation.</p><pre><code>// src/cli/print.ts (lines 1858-1863)
// Abort the current operation when a 'now' priority message arrives.
subscribeToCommandQueue(() =&gt; {
  if (abortController &amp;&amp; getCommandsByMaxPriority('now').length &gt; 0) {
    abortController.abort('interrupt')
  }
})</code></pre><h3>2.8 Cleanup, audit, and the failsafe forceExit</h3><p>After abort, the <code>gracefulShutdown</code> pipeline drains the event loop, runs SessionEnd hooks under their own bounded <code>AbortSignal.timeout</code>, flushes analytics, and arms a failsafe timer that hard-exits if cleanup itself hangs.</p><pre><code>// src/utils/gracefulShutdown.ts (lines 417-426 and 472-480, abridged)
// Failsafe: guarantee process exits even if cleanup hangs.
failsafeTimer = setTimeout(
  code =&gt; {
    cleanupTerminalModes()
    printResumeHint()
    forceExit(code)
  },
  Math.max(5000, sessionEndTimeoutMs + 3500),
  exitCode,
)
failsafeTimer.unref()</code></pre><p>The hooks themselves run under a derived signal, so even shutdown work is cancellable by the same mechanism.</p><pre><code>// src/utils/gracefulShutdown.ts (lines 472-480)
try {
  await executeSessionEndHooks(reason, {
    ...options,
    signal: AbortSignal.timeout(sessionEndTimeoutMs),
    timeoutMs: sessionEndTimeoutMs,
  })
} catch {
  // Ignore SessionEnd hook exceptions (including AbortError on timeout)
}</code></pre><p>This is cancellation turned in on itself: <code>AbortSignal.timeout</code> lets the <em>cancellation</em> path re-use the same primitive that the <em>agent</em> path uses, so a hung SessionEnd hook can't strand the whole process during shutdown.</p><h2>3. Hermes Agent Implementation</h2><div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" href="https://substackcdn.com/image/fetch/$s_!epfr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F37113359-5534-4557-8ecf-c806f409f4cc_1800x1080.png" target="_blank"><div class="image2-inset"><source type="image/webp" /><img alt="Figure 2.2: Push vs. poll &#8212; the AbortController tree and the thread-scoped flag side by side" class="sizing-normal" height="1080" src="https://substackcdn.com/image/fetch/$s_!epfr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F37113359-5534-4557-8ecf-c806f409f4cc_1800x1080.png" title="Figure 2.2: Push vs. poll &#8212; the AbortController tree and the thread-scoped flag side by side" width="1800" /><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset"><button class="pencraft pc-reset pencraft icon-container restack-image" tabindex="0" type="button"><svg fill="none" height="20" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><g><title></title><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button class="pencraft pc-reset pencraft icon-container view-image" tabindex="0" type="button"><svg class="lucide lucide-maximize2 lucide-maximize-2" fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button></div></div></div></a></figure></div><p><em>Figure 2.2.</em> On the left, Claude Code's push model: the <code>QueryEngine.abortController</code> is the root, child controllers branch off for per-tool sibling scopes and sub-agents, and <code>signal.aborted</code> fires once to every subscribed leaf &#8212; the BashTool's spawned shell, the WebFetch stream, the sub-agent recursion &#8212; with <code>signal.reason</code> carrying the cause. On the right, Hermes's poll model: <code>AIAgent.interrupt()</code> flips a <code>_interrupt_requested</code> flag and writes every relevant thread ident into a process-global <code>_interrupted_threads</code> set; each long-running tool calls <code>is_interrupted()</code> on every loop iteration and checks its own bit. The two converge on the same outer shape &#8212; one public <code>interrupt()</code>, one audit trail &#8212; but invert the responsibility: Claude Code does the plumbing once at every async boundary; Hermes does the polling once at every long-running tick.</p><h3>3.1 Why Hermes can't use <code>AbortController</code></h3>
      <p>
          <a href="https://kenhuangus.substack.com/p/chapter-2-cancellation-and-abort">
              Read more
          </a>
      </p>
