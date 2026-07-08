---
source: farmer/rss
feed: agentic-ai
farmed: 2026-07-08T05:20:22Z
title: Chapter 6: Terminal UI Architecture (Claude Code vs. Hermes Agent)
url: https://kenhuangus.substack.com/p/chapter-6-terminal-ui-architecture
published: 2026-06-29
author: Ken Huang
---

# Chapter 6: Terminal UI Architecture (Claude Code vs. Hermes Agent)

<p>Before you read on &#8212; two quick announcements. First, you can now get 50% off a yearly subscription and unlock all paid content on Agentic AI, AI Security, and more: <a href="https://kenhuangus.substack.com/subscribe?coupon=302342d9">https://kenhuangus.substack.com/subscribe?coupon=302342d9</a>.</p><p>Second, all previously written 15 Hermes Agent and Claude Code agentic harness design patterns are now available in a single book on Amazon: <a href="https://www.amazon.com/Agentic-AI-Harness-Pattern-Patterns-ebook/dp/B0H13XWS8W">https://www.amazon.com/Agentic-AI-Harness-Pattern-Patterns-ebook/dp/B0H13XWS8W</a></p><p><strong>Previously in this series.</strong> This chapter builds on five earlier deep dives into the Claude Code and Hermes harness. If you are new here, read these first:</p><ul><li><p><a href="https://kenhuangus.substack.com/p/chapter-1-cost-and-token-usage-accounting">Chapter 1: Cost &amp; Token-Usage Accounting</a></p></li><li><p><a href="https://kenhuangus.substack.com/p/chapter-2-cancellation-and-abort">Chapter 2: Cancellation &amp; Abort Propagation</a></p></li><li><p><a href="https://kenhuangus.substack.com/p/chapter-3-the-slash-command-system">Chapter 3: The Slash Command System</a></p></li><li><p><a href="https://kenhuangus.substack.com/p/chapter-4-working-directory-and-file">Chapter 4: Working Directory &amp; File-Path Resolution</a></p></li><li><p><a href="https://kenhuangus.substack.com/p/chapter-5-trajectory-compression">Chapter 5: Trajectory Compression and Replay</a></p></li></ul><h2>1. Pattern Summary</h2><p>Terminal UI architecture is the rendering substrate of an agent harness &#8212; the layer that takes a stream of agent events (tokens, tool starts, tool completions, status changes) and turns it into a coherent, redrawable picture inside an 80-column box of cells. It is distinct from the input substrate (slash commands, key bindings) and from the content substrate (output styles, markdown rendering). The rendering substrate has its own concerns: how do you reconcile a React-style component tree against a fixed-cell terminal grid; how do you handle resize without flicker; how do you overlay a modal dialog without losing the conversation underneath; how do you keep two processes (agent core and TUI) in sync over a wire; how do you re-enter the alternate screen after the user backgrounds and resumes the process. Claude Code and Hermes solve the same set of problems with different process topologies &#8212; Claude Code runs the renderer in-process with the agent loop, while Hermes splits the agent and the TUI into separate processes connected by a JSON-RPC gateway.</p><div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" href="https://substackcdn.com/image/fetch/$s_!YblR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe164c4d2-d941-41cf-a804-8655a37ae1df_1800x1080.png" target="_blank"><div class="image2-inset"><source type="image/webp" /><img alt="Figure 6.1: Streaming events become reactive frames in two topologies" class="sizing-normal" height="1080" src="https://substackcdn.com/image/fetch/$s_!YblR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe164c4d2-d941-41cf-a804-8655a37ae1df_1800x1080.png" title="Figure 6.1: Streaming events become reactive frames in two topologies" width="1800" /><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset"><button class="pencraft pc-reset pencraft icon-container restack-image" tabindex="0" type="button"><svg fill="none" height="20" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><g><title></title><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button class="pencraft pc-reset pencraft icon-container view-image" tabindex="0" type="button"><svg class="lucide lucide-maximize2 lucide-maximize-2" fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button></div></div></div></a></figure></div><p><em>Figure 6.1.</em> The same stream of agent events feeds two render topologies: Claude Code commits a React tree directly to the terminal cell grid in-process, while Hermes ships every event as JSON-RPC across a process boundary so a separate Node renderer can paint the same component tree.</p><h2>2. Claude Code Implementation</h2><p>Claude Code's rendering substrate is a fork of the <a href="https://github.com/vadimdemedes/ink">Ink</a> library that has been heavily customized for production-grade agent UX. The key insight is that Ink uses React-reconciler to commit a virtual DOM into a flat grid of terminal cells, with double-buffered frame diffing so each frame writes only the cells that changed. The agent loop is just another React component tree &#8212; streaming text becomes <code>setState</code> calls, tool starts become new child components, and the user never sees the seam between "model thinking" and "tool executing" because the same render scheduler drives both.</p><h3>The Ink class as render owner</h3><p>Ink is implemented as a single class that owns the React reconciler container, the front and back frame buffers, the focus manager, and the terminal I/O streams.</p><pre><code>// src/ink/ink.tsx
export default class Ink {
  private readonly log: LogUpdate;
  private readonly terminal: Terminal;
  private scheduleRender: (() =&gt; void) &amp; {
    cancel?: () =&gt; void;
  };
  private isUnmounted = false;
  private isPaused = false;
  private readonly container: FiberRoot;
  private rootNode: dom.DOMElement;
  readonly focusManager: FocusManager;
  private renderer: Renderer;</code></pre><p>The <code>container</code> is the React reconciler root &#8212; it holds the fiber tree that React commits into. The <code>frontFrame</code> / <code>backFrame</code> pair is a classic double-buffer: the renderer paints into the back, then a diff against the front produces the minimal sequence of cursor-move + cell-write escapes to send to the terminal. The <code>LogUpdate</code> instance owns the relative-cursor invariants that let <code>console.log</code> and a redrawing UI coexist on the main screen.</p><h3>Resize handling without flicker</h3><p>Terminal resize is one of the trickier UX problems. When a user drags the window edge, the terminal can emit two or three resize events back-to-back, and the OS-reported <code>stdout.columns</code> value changes asynchronously. A naive renderer either flickers (clears the screen, then paints) or shows stale layout (paints with old columns, then re-flows). Ink's handler is deliberately synchronous and goes through an alt-screen-aware repaint path.</p><pre><code>// src/ink/ink.tsx
private handleResize = () =&gt; {
  const cols = this.options.stdout.columns || 80;
  const rows = this.options.stdout.rows || 24;
  if (cols === this.terminalColumns &amp;&amp; rows === this.terminalRows) return;
  this.terminalColumns = cols;
  this.terminalRows = rows;
  this.altScreenParkPatch = makeAltScreenParkPatch(this.terminalRows);</code></pre><p>Same-dimension resize events are dropped immediately &#8212; emulators commonly emit two or three events for a single drag, and rendering each one would cause double or triple repaints. After a real change, the alt-screen branch resets the frame buffers and queues an <code>ERASE_SCREEN</code> to be folded into the next paint.</p><pre><code>// src/ink/ink.tsx (continued)
  if (this.altScreenActive &amp;&amp; !this.isPaused &amp;&amp; this.options.stdout.isTTY) {
    if (this.altScreenMouseTracking) {
      this.options.stdout.write(ENABLE_MOUSE_TRACKING);
    }
    this.resetFramesForAltScreen();
    this.needsEraseBeforePaint = true;
  }</code></pre><p>The <code>needsEraseBeforePaint</code> flag is the key to flicker-free resize. Writing <code>ERASE_SCREEN</code> synchronously in the resize handler would leave the terminal blank for the ~80 ms it takes React to reconcile the new layout. Instead, the erase is deferred into the next <code>onRender</code>'s patch list, which writes the erase and the new content inside a single Begin-Sync-Update / End-Sync-Update block &#8212; atomic from the user's eye.</p><h3>Alternate screen as a React component</h3><p>The most distinctive pattern in Ink is treating the alternate screen as a JSX wrapper component, not a global mode flag. Mounting <code>&lt;AlternateScreen&gt;</code> enters DEC mode 1049; unmounting it exits and restores the main screen content. This means a transcript-overlay key like Ctrl+O can simply mount a different component tree.</p><pre><code>// src/ink/components/AlternateScreen.tsx
export function AlternateScreen({ children, mouseTracking = true }: Props) {
  const size = useContext(TerminalSizeContext)
  const writeRaw = useContext(TerminalWriteContext)
  useInsertionEffect(() =&gt; {
    const ink = instances.get(process.stdout)
    if (!writeRaw) return
    writeRaw(
      ENTER_ALT_SCREEN + '\x1b[2J\x1b[H' +
      (mouseTracking ? ENABLE_MOUSE_TRACKING : '')
    )
    ink?.setAltScreenActive(true, mouseTracking)
    return () =&gt; {
      ink?.setAltScreenActive(false)
      ink?.clearTextSelection()
      writeRaw((mouseTracking ? DISABLE_MOUSE_TRACKING : '') + EXIT_ALT_SCREEN)
    }
  }, [writeRaw, mouseTracking])
  return &lt;Box flexDirection="column" height={size?.rows ?? 24} width="100%" flexShrink={0}&gt;{children}&lt;/Box&gt;
}</code></pre><p>The use of <code>useInsertionEffect</code> (not <code>useLayoutEffect</code>) is load-bearing &#8212; it fires during React's mutation phase, before <code>resetAfterCommit</code> runs Ink's <code>onRender</code>. If layout-effect were used instead, the first frame would paint to the main screen with <code>altScreenActive=false</code>, then the alt-screen would be entered, leaving a "broken view" frame visible behind the alt buffer.</p><h3>Modal dialog overlays via dynamic imports</h3><p>Concurrent dialogs (permission requests, settings validation, snapshot updates, teleport pickers) are launched as one-off React subtrees that resolve a Promise when the user picks an option. The <code>dialogLaunchers.tsx</code> module is a pure adapter &#8212; each launcher dynamic-imports its component, mounts it via <code>showSetupDialog</code>, and returns a Promise.</p><pre><code>// src/dialogLaunchers.tsx
export async function launchSnapshotUpdateDialog(root: Root, props: {
  agentType: string;
  scope: AgentMemoryScope;
  snapshotTimestamp: string;
}): Promise&lt;'merge' | 'keep' | 'replace'&gt; {
  const { SnapshotUpdateDialog } = await import('./components/agents/SnapshotUpdateDialog.js');
  return showSetupDialog&lt;'merge' | 'keep' | 'replace'&gt;(root, done =&gt; (
    &lt;SnapshotUpdateDialog
      agentType={props.agentType}
      scope={props.scope}
      snapshotTimestamp={props.snapshotTimestamp}
      onComplete={done}
      onCancel={() =&gt; done('keep')}
    /&gt;
  ))
}</code></pre><p>The <code>done</code> callback is the dialog's only escape hatch. Whatever the user clicks resolves the outer Promise, and the agent loop that awaited the launcher continues. Because the dialog is just a React subtree mounted into the same Ink container, it inherits theme, focus, and key handling for free &#8212; there is no separate "dialog runtime."</p><h3>Reactive streaming via state hooks</h3><p>The agent loop turns into a render via React state. Streaming tokens accumulate in a state slice; a tool start pushes a new tool element into the tree; a tool completion replaces the in-progress element with its result. The REPL screen subscribes to <code>useStdin</code>, <code>useTerminalSize</code>, <code>useTerminalFocus</code>, and a dozen other hooks that all bottom-out in React context.</p><pre><code>// src/screens/REPL.tsx (imports)
import { Box, Text, useStdin, useTheme, useTerminalFocus, useTerminalTitle, useTabStatus } from '../ink.js';</code></pre><p>The render scheduler is throttled with <code>lodash-es/throttle</code>. When state updates come faster than <code>FRAME_INTERVAL_MS</code>, they coalesce into a single React commit, which produces a single frame diff, which produces a single batched write to the terminal. This is what keeps the UI responsive when 200 tokens per second are streaming in: one paint per frame interval, not one paint per token.</p><h2>3. Hermes Agent Implementation</h2><p>Hermes takes a fundamentally different topology. The agent core lives in a Python process; the TUI lives in a Node.js process; they communicate over JSON-RPC framed as newline-delimited JSON on stdio (or as messages on a WebSocket when running attached). The TUI process uses its own fork of Ink &#8212; published as <code>@hermes/ink</code> &#8212; but the renderer never touches the agent loop directly. Every event the user sees was JSON-encoded in Python, parsed in Node, dispatched to a nanostore, and triggered a React rerender.</p><div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" href="https://substackcdn.com/image/fetch/$s_!PTwd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe6b97510-6636-4103-9633-36611c1acf23_1800x1080.png" target="_blank"><div class="image2-inset"><source type="image/webp" /><img alt="Figure 6.2: Hermes ui-tui (Node) and tui_gateway (Python) connected by JSON-RPC over stdio" class="sizing-normal" height="1080" src="https://substackcdn.com/image/fetch/$s_!PTwd!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe6b97510-6636-4103-9633-36611c1acf23_1800x1080.png" title="Figure 6.2: Hermes ui-tui (Node) and tui_gateway (Python) connected by JSON-RPC over stdio" width="1800" /><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset"><button class="pencraft pc-reset pencraft icon-container restack-image" tabindex="0" type="button"><svg fill="none" height="20" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><g><title></title><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button class="pencraft pc-reset pencraft icon-container view-image" tabindex="0" type="button"><svg class="lucide lucide-maximize2 lucide-maximize-2" fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button></div></div></div></a></figure></div><p><em>Figure 6.2.</em> The Node ui-tui process owns the screen and runs <code>GatewayClient</code>, a nanostore, and the React tree; the Python tui_gateway owns the agent and runs the read-parse-dispatch loop. RPCs flow right (terminal.resize, prompt.send), events flow left (<code>method:"event"</code>), and <code>BrokenPipeError</code> is the protocol's clean-disconnect signal.</p><h3>The TUI entry as a thin Node bootstrap</h3><p>The TUI process starts by spawning the Python gateway as a child process and wiring up exit handlers. There is no agent in the TUI process &#8212; only a <code>GatewayClient</code> that pushes RPCs out and pulls events in.</p><pre><code>// hermes-agent/ui-tui/src/entry.tsx
if (!process.stdin.isTTY) {
  console.log('hermes-tui: no TTY')
  process.exit(0)
}
resetTerminalModes()
const gw = new GatewayClient()
gw.start()</code></pre><p>The first thing the entry does is reset terminal modes &#8212; a kill-9'd previous TUI can leave mouse tracking, bracketed paste, and Kitty keyboard mode all enabled, and the new process must clear them before its own React tree runs. Then the gateway client is constructed and started, which spawns the Python child.</p><pre><code>// hermes-agent/ui-tui/src/entry.tsx (continued)
const [ink, { App }, { logFrameEvent }, { trackFrame }] = await Promise.all([
  import('@hermes/ink'),
  import('./app.js'),
  import('./lib/perfPane.js'),
  import('./lib/fpsStore.js')
])
ink.render(&lt;App gw={gw} /&gt;, { exitOnCtrlC: false, onFrame })</code></pre><p>The four imports are launched in parallel &#8212; the gateway is already booting Python in the background, so the parallelism here matters. By the time <code>ink.render</code> mounts the React tree, the gateway is usually past <code>gateway.ready</code> and the App can immediately fetch session state.</p><h3>The gateway as a separate process</h3><p>The Python gateway process is a JSON-RPC dispatcher built on stdin/stdout. It owns the agent, but it doesn't render. The TUI process owns the screen, but it has no agent. The boundary is the wire format. The gateway's first responsibility on startup is to emit <code>gateway.ready</code>, which is the synchronization point the TUI uses to begin fetching session state.</p><pre><code># hermes-agent/tui_gateway/entry.py
def main():
    _install_sidecar_publisher()
    if not write_json({
        "jsonrpc": "2.0",
        "method": "event",
        "params": {"type": "gateway.ready", "payload": {"skin": resolve_skin()}},
    }):
        _log_exit("startup write failed (broken stdout pipe before first event)")
        sys.exit(0)</code></pre><p>After ready, the gateway becomes a synchronous read-parse-dispatch loop. Each iteration reads a JSON line from stdin, parses it, dispatches to the registered RPC handler, and writes the response back to stdout.</p><pre><code># hermes-agent/tui_gateway/entry.py (continued)
    for raw in sys.stdin:
        line = raw.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except json.JSONDecodeError:
            if not write_json({"jsonrpc": "2.0", "error": {"code": -32700, "message": "parse error"}, "id": None}):
                _log_exit("parse-error-response write failed (broken stdout pipe)")
                sys.exit(0)
            continue
        method = req.get("method") if isinstance(req, dict) else None
        resp = dispatch(req)
        if resp is not None:
            if not write_json(resp):
                _log_exit(f"response write failed for method={method!r} (broken stdout pipe)")
                sys.exit(0)</code></pre><p>Events that happen asynchronously &#8212; tool progress, streaming deltas, status changes &#8212; are pushed via the same <code>write_json</code> path, distinguished by a <code>method: "event"</code> field instead of a response <code>id</code>. The TUI's dispatch routes the two cases: an <code>id</code> match resolves a pending RPC promise, while a <code>method === 'event'</code> frame is published to the nanostore.</p><h3>The transport abstraction</h3><p>Because the gateway can run over stdio or attached WebSocket, the I/O sink is abstracted as a <code>Transport</code> protocol. The same dispatcher handles both transports without duplicating any business logic. The class header binds a stream getter and a lock &#8212; the getter is a callable so monkey-patching the underlying stream still works.</p><pre><code># hermes-agent/tui_gateway/transport.py
class StdioTransport:
    __slots__ = ("_stream_getter", "_lock")

    def __init__(self, stream_getter: Callable[[], Any], lock: threading.Lock) -&gt; None:
        self._stream_getter = stream_getter
        self._lock = lock</code></pre><p>The <code>write</code> method serializes outside the lock and then writes inside. Crucially, <code>BrokenPipeError</code> (and a small set of OSError errnos meaning "peer gone") returns <code>False</code> rather than raising &#8212; this is the protocol's clean-disconnect signal.</p><pre><code># hermes-agent/tui_gateway/transport.py (continued)
    def write(self, obj: dict) -&gt; bool:
        line = json.dumps(obj, ensure_ascii=False) + "\n"
        with self._lock:
            stream = self._stream_getter()
            try:
                stream.write(line)
            except BrokenPipeError:
                return False
            except OSError as e:
                if e.errno not in _PEER_GONE_ERRNOS:
                    raise
                return False
            return True</code></pre><p>The serialization happens outside the lock so a large payload &#8212; say, a 200KB tool result &#8212; cannot block other threads from emitting their own frames. The <code>BrokenPipeError</code> handling is the key wire-protocol invariant: when the TUI quits, the gateway sees a broken pipe and exits cleanly via the <code>False</code> return path, rather than crashing on an unhandled exception.</p><h3>The gateway client as Node-side mirror</h3><p>On the TUI side, <code>GatewayClient</code> is a Node.js EventEmitter that owns the Python child process, parses every line of stdout as a JSON-RPC frame, and routes responses back to in-flight RPC promises.</p><pre><code>// hermes-agent/ui-tui/src/gatewayClient.ts
private startSpawnedGateway(root: string) {
  const python = resolvePython(root)
  const cwd = process.env.HERMES_CWD || root
  const env = { ...process.env }
  const pyPath = env.PYTHONPATH?.trim()
  env.PYTHONPATH = pyPath ? `${root}${delimiter}${pyPath}` : root
  this.startReadyTimer(python, cwd)
  this.proc = spawn(python, ['-m', 'tui_gateway.entry'],
    { cwd, env, stdio: ['pipe', 'pipe', 'pipe'] })</code></pre><p>The <code>startReadyTimer</code> is one of the more nuanced parts of the contract: if the gateway doesn't emit <code>gateway.ready</code> within the configured timeout, the TUI surfaces a <code>gateway.start_timeout</code> event so the user sees something more actionable than a blank screen.</p><pre><code>// hermes-agent/ui-tui/src/gatewayClient.ts (continued)
  this.stdoutRl = createInterface({ input: this.proc.stdout! })
  this.stdoutRl.on('line', raw =&gt; {
    try {
      this.dispatch(JSON.parse(raw))
    } catch {
      const preview = raw.trim().slice(0, MAX_LOG_PREVIEW) || '(empty line)'
      this.pushLog(`[protocol] malformed stdout: ${preview}`)
      this.publish({ type: 'gateway.protocol_error', payload: { preview } })
    }
  })</code></pre><p>The dispatch routes parsed frames either to a pending RPC's resolver (when <code>id</code> matches) or to the event bus (when <code>method === 'event'</code>). This is what makes the TUI feel alive &#8212; every render the user sees is an event published from this stream, transformed into a <code>patchUiState</code> call, which triggers React to rerender the relevant pane.</p><h3>Resize as a wire protocol message</h3><p>Because the TUI process owns the terminal but the gateway's <code>cols</code> value affects how it formats output (markdown wrapping, diff column width), resize must round-trip across the wire. The TUI debounces 100 ms to avoid spamming the gateway, then sends a <code>terminal.resize</code> RPC.</p><pre><code>// hermes-agent/ui-tui/src/app/useMainApp.ts
useEffect(() =&gt; {
  if (!ui.sid || !stdout) return
  let timer: ReturnType&lt;typeof setTimeout&gt; | undefined
  const onResize = () =&gt; {
    clearTimeout(timer)
    timer = setTimeout(() =&gt; {
      timer = undefined
      void rpc&lt;TerminalResizeResponse&gt;('terminal.resize', { cols: stdout.columns ?? 80, session_id: ui.sid })
    }, 100)
  }
  stdout.on('resize', onResize)
  return () =&gt; { clearTimeout(timer); stdout.off('resize', onResize) }
}, [rpc, stdout, ui.sid])</code></pre><p>On the gateway side, the handler is trivial &#8212; it just stashes the new column count in the session state so subsequent renders use it.</p><pre><code># hermes-agent/tui_gateway/server.py
@method("terminal.resize")
def _(rid, params: dict) -&gt; dict:
    session, err = _sess_nowait(params, rid)
    if err:
        return err
    session["cols"] = int(params.get("cols", 80))
    return _ok(rid, {"cols": session["cols"]})</code></pre><p>This split &#8212; the TUI knows the screen, the gateway knows the agent, and <code>terminal.resize</code> is the only point where the two perspectives reconcile &#8212; is the architectural commitment of the gateway model.</p><h3>Concurrent overlays via nanostore</h3><p>Hermes does not use React Context for global UI state. It uses <code>@nanostores/react</code>, which gives it a synchronous, subscription-based store that any component can read without prop-drilling and without forcing parent rerenders. The overlay store is what drives modal switching.</p><pre><code>// hermes-agent/ui-tui/src/components/appLayout.tsx
const Shell = INLINE_MODE ? Fragment : AlternateScreen
const shellProps = INLINE_MODE ? {} : { mouseTracking }
return (
  &lt;Shell {...shellProps}&gt;
    &lt;Box flexDirection="column" flexGrow={1}&gt;
      &lt;Box flexDirection="row" flexGrow={1}&gt;
        {overlay.agents ? (
          &lt;PerfPane id="agents"&gt;&lt;AgentsOverlayPane /&gt;&lt;/PerfPane&gt;
        ) : (
          &lt;PerfPane id="transcript"&gt;
            &lt;TranscriptPane ... /&gt;
          &lt;/PerfPane&gt;
        )}
      &lt;/Box&gt;</code></pre><p>Note the <code>INLINE_MODE</code> toggle: Hermes can render either inside the alternate screen (full-screen TUI with mouse tracking) or inline in the host terminal's scrollback. The <code>Shell</code> swaps between <code>AlternateScreen</code> and <code>Fragment</code> based on the env var, and the rest of the layout is identical. This is the same JSX-as-mode-switch pattern Claude Code uses for <code>&lt;AlternateScreen&gt;</code>, applied to a different problem (inline vs. fullscreen) rather than (modal vs. main).</p><h2>4. Side-by-Side Comparison</h2><p>The single biggest architectural difference between Claude Code and Hermes is process topology. Claude Code's renderer is a React tree mounted in the same Node process as the agent loop &#8212; <code>setState</code> from the loop directly schedules a render, and the React commit phase writes terminal escape sequences synchronously. There is no wire protocol because there is no wire. Hermes's renderer is a different process from the agent &#8212; every byte the user sees is JSON-encoded in Python, decoded in Node, dispatched to a nanostore, and rendered through React. This adds latency (a few milliseconds per event in the steady state) but buys process isolation: the Python agent can crash without taking down the TUI, the TUI can be backgrounded and reattached, and a remote dashboard can subscribe to the same event stream via a WebSocket sidecar transport.</p><p>The second difference is how the two systems handle alt-screen mode and overlays. Claude Code treats alt-screen as just another React component (<code>&lt;AlternateScreen&gt;</code>) that toggles DEC mode 1049 from a <code>useInsertionEffect</code>, mounted as a wrapper around the modal subtree. Modal dialogs are mounted by dynamic-importing the dialog component and resolving a Promise on the user's choice &#8212; a fully reactive flow with no separate dialog runtime. Hermes uses the same <code>&lt;AlternateScreen&gt;</code> JSX wrapper at the top of <code>AppLayout</code>, but its overlays come from a separate <code>nanostore</code> &#8212; <code>$overlayState.agents</code> flips a boolean and the layout swaps the transcript pane for the agents pane. Hermes's modals (approval dialogs, secret prompts) come down the wire as gateway events that flip the overlay store; Claude Code's modals are mounted directly by the agent loop's await of <code>showSetupDialog</code>.</p><p>The third difference is resize handling. Both systems debounce or de-duplicate resize events to avoid double-paints, but Claude Code's resize stays entirely in-process and uses a deferred-erase trick (<code>needsEraseBeforePaint</code>) to fold the screen-clear into the next atomic frame paint. Hermes's resize goes around an extra loop: the TUI debounces locally, then sends a <code>terminal.resize</code> RPC over the wire so the gateway's column count tracks the screen, then the next outbound rendered text from the agent uses the new column width. Hermes also has a unique concern Claude Code doesn't &#8212; backwards-compatibility between <code>INLINE_MODE</code> and full-screen mode, since the gateway can be embedded inside a host shell's scrollback rather than always taking over the screen.</p><h2>5. When to Use Which</h2><p><strong>Use Claude Code's in-process rendering when:</strong></p><ul><li><p>You want minimum latency from agent state to pixel &#8212; there is no wire to cross, so a streaming token can reach the screen in a single React commit.</p></li><li><p>You're building an SDK-first product where the agent is embedded in a larger TypeScript app and you don't need to support the renderer running on a different host.</p></li><li><p>Your modal flow is <code>await showDialog(...)</code> &#8212; Claude Code's dialog launchers turn a JSX tree into a Promise, and the agent loop just awaits it.</p></li></ul><p><strong>Use Hermes's gateway-plus-TUI architecture when:</strong></p><ul><li><p>The agent and the TUI must run on different machines or processes &#8212; for example, a Python agent in a Docker container with a Node TUI on the developer's laptop attached over WebSocket.</p></li><li><p>You need a sidecar transport that mirrors agent events to a separate dashboard, log aggregator, or monitoring system without modifying the agent.</p></li><li><p>The agent is in Python and the rendering library you want is in Node &#8212; Hermes's wire protocol decouples language choice from rendering choice.</p></li></ul><p><strong>Hybrid recommendation:</strong> Most production deployments need both modes. The right architecture is to make the rendering substrate transport-aware: an in-process React tree when the agent is local, a JSON-RPC client when it's remote. Claude Code's <code>Ink</code> instance and Hermes's <code>GatewayClient</code> could share a common interface &#8212; both produce a stream of <code>GatewayEvent</code>-shaped objects &#8212; and the React tree above could be identical. You get Claude Code's latency for local development and Hermes's process isolation for production deployment, with one component tree.</p><p><strong>For paid subscribers &#8212; the applied build and a hands-on deep dive continue below.</strong></p><p>Everything above is free: the full terminal-UI architecture of both Claude Code and Hermes, the side-by-side comparison, and when to use each. The paid section is where you <strong>build it for real</strong>. You get (1) a complete defensive-cyber <strong>SOC analyst console</strong> on the gateway-plus-TUI pattern &#8212; every file, from the per-panel nanostores to the wire handler to a destructive-remediation approval modal; (2) a <strong>concrete runnable example</strong> wiring a cost-threshold overlay from streaming event to cell grid; (3) how this pattern <strong>compares to MCP, A2A, and adjacent UI architectures</strong>; and (4) four <strong>project-driven Claude Code exercises</strong> you can land in a single focused session.</p><p>Unlock it &#8212; and every paid deep-dive across the Agentic AI and AI Security series &#8212; at 50% off a yearly subscription here: <a href="https://kenhuangus.substack.com/subscribe?coupon=302342d9">https://kenhuangus.substack.com/subscribe?coupon=302342d9</a>.</p>
      <p>
          <a href="https://kenhuangus.substack.com/p/chapter-6-terminal-ui-architecture">
              Read more
          </a>
      </p>
