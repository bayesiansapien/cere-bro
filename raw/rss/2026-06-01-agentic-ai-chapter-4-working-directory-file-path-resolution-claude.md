---
source: farmer/rss
feed: agentic-ai
farmed: 2026-06-02T10:59:37.951858+00:00
title: Chapter 4: Working Directory & File-Path Resolution (Claude Code vs. Hermes Agent)
url: https://kenhuangus.substack.com/p/chapter-4-working-directory-and-file
published: 2026-06-01
author: Ken Huang
---

# Chapter 4: Working Directory & File-Path Resolution (Claude Code vs. Hermes Agent)

<p>This is chapter 4 of total 10 chapters book to be published soon. The previous chpaters&#8217; links are below:</p><p><a href="https://kenhuangus.substack.com/p/chapter-1-cost-and-token-usage-accounting">chapter 1</a> and <a href="https://kenhuangus.substack.com/p/chapter-2-cancellation-and-abort">chapter 2</a>, <a href="https://kenhuangus.substack.com/p/chapter-3-the-slash-command-system">Chapter 3</a>, </p><h2>1. Pattern Summary</h2><p>Working directory resolution is the harness's answer to a deceptively simple question: when the model writes <code>Read("README.md")</code> or <code>Bash("cat config.json")</code>, what does that string actually mean on disk? An LLM produces tokens, not file handles. Every relative path, tilde, glob, symlink, and <code>cd</code> between turns must be resolved by the harness into an unambiguous absolute path before any syscall fires &#8212; and the resolution must stay consistent across hundreds of tool calls, parallel subagents, container hops, and shell sessions that may or may not preserve their own <code>cwd</code>. Without this layer, an agent that runs <code>cd /tmp</code> in turn 5 and <code>cat README.md</code> in turn 6 will surprise everyone: the human sees <code>/tmp/README.md</code>, the model thinks it's still in the project root, and the permission system validates a third path entirely. With this layer, the agent's mental model of the filesystem stays aligned with the harness's enforcement model and the user's expectation. This pattern is distinct from permissions (which decides <em>whether</em> a path is allowed) and tool architecture (which decides <em>what</em> a tool does) &#8212; it is purely about <em>interpretation</em>: turning a string the model produced into a stable, audited filesystem location.</p><div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" href="https://substackcdn.com/image/fetch/$s_!810K!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea75b031-9c0b-4f5a-8914-bad6d960123b_1800x960.png" target="_blank"><div class="image2-inset"><source type="image/webp" /><img alt="Figure 4.1: Path resolution anchor across stateless tool calls" class="sizing-normal" height="960" src="https://substackcdn.com/image/fetch/$s_!810K!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea75b031-9c0b-4f5a-8914-bad6d960123b_1800x960.png" title="Figure 4.1: Path resolution anchor across stateless tool calls" width="1800" /><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset"><button class="pencraft pc-reset pencraft icon-container restack-image" tabindex="0" type="button"><svg fill="none" height="20" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><g><title></title><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button class="pencraft pc-reset pencraft icon-container view-image" tabindex="0" type="button"><svg class="lucide lucide-maximize2 lucide-maximize-2" fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button></div></div></div></a></figure></div><p><em>Figure 4.1.</em> The harness sits between the model's raw path strings and the filesystem, canonicalizing every input through <code>expandPath</code>, the live cwd state, an immutable session anchor, and a containment check. Every relative path, tilde, glob, and <code>cd</code> between turns flows through the same anchored pipeline before any syscall fires.</p><p></p><p>Before you read on &#8212; two quick announcements. First, you can now get 50% off a yearly subscription and unlock all paid content on Agentic AI, AI Security, and more: <a href="https://kenhuangus.substack.com/subscribe?coupon=302342d9">https://kenhuangus.substack.com/subscribe?coupon=302342d9</a>.</p><p>Second, all previously written 15 Hermes Agent and Claude Code agentic harness design patterns are now available in a single book on Amazon: <a href="https://www.amazon.com/Agentic-AI-Harness-Pattern-Patterns-ebook/dp/B0H13XWS8W">https://www.amazon.com/Agentic-AI-Harness-Pattern-Patterns-ebook/dp/B0H13XWS8W</a></p><h2>2. Claude Code Implementation</h2><p>Claude Code treats cwd as session-global state with strict invariants: there is exactly one current working directory at any moment for the synchronous code path, but each subagent can carry its own override via <code>AsyncLocalStorage</code> so concurrent agents never race. The state lives in three layers &#8212; a global <code>STATE.cwd</code>, a per-async-context override store, and a <code>getCwd()</code> accessor that resolves to whichever applies.</p><h3>The cwd accessor and per-async override</h3><pre><code>// src/utils/cwd.ts
import { AsyncLocalStorage } from 'async_hooks'
import { getCwdState, getOriginalCwd } from '../bootstrap/state.js'

const cwdOverrideStorage = new AsyncLocalStorage&lt;string&gt;()

/**
 * Run a function with an overridden working directory for the current async context.
 * All calls to pwd()/getCwd() within the function (and its async descendants) will
 * return the overridden cwd instead of the global one. This enables concurrent
 * agents to each see their own working directory without affecting each other.
 */
export function runWithCwdOverride&lt;T&gt;(cwd: string, fn: () =&gt; T): T {
  return cwdOverrideStorage.run(cwd, fn)
}

export function pwd(): string {
  return cwdOverrideStorage.getStore() ?? getCwdState()
}</code></pre><p><code>AsyncLocalStorage</code> is the load-bearing primitive. Without it, two parallel subagents that ran in different worktrees would clobber each other's <code>process.chdir</code>. With it, each agent inherits a frozen snapshot of cwd at spawn time, and that snapshot follows every async tool call originating from that agent.</p><h3>Path expansion as the single ingress point</h3><p>Every file path the model produces flows through <code>expandPath()</code> before any syscall. This function is the harness's interpreter: it accepts raw input and emits a canonical absolute path in the platform-native format.</p><p>The opening of <code>expandPath</code> does two jobs: it picks a base directory to resolve against (falling back through cwd-override, global cwd, and finally Node's process cwd), then enforces the most basic safety property of all &#8212; rejecting null bytes that could truncate the path early in a syscall.</p><pre><code>// src/utils/path.ts &#8212; every model-produced path passes through here.
export function expandPath(path: string, baseDir?: string): string {
  const actualBaseDir = baseDir ?? getCwd() ?? getFsImplementation().cwd()

  // Security: Check for null bytes
  if (path.includes('\0') || actualBaseDir.includes('\0')) {
    throw new Error('Path contains null bytes')
  }</code></pre><p>Next come the user-friendliness layers: tilde expansion to the user's home directory, and a Windows-specific rewrite that converts Git-Bash-style paths like <code>/c/Users/...</code> into native <code>C:\Users\...</code>. Note the <code>.normalize('NFC')</code> &#8212; every return path is NFC-normalized so downstream string comparisons are stable.</p><pre><code>  // Handle home directory notation
  if (trimmedPath === '~') return homedir().normalize('NFC')
  if (trimmedPath.startsWith('~/'))
    return join(homedir(), trimmedPath.slice(2)).normalize('NFC')

  // On Windows, convert POSIX-style paths (/c/Users/...) to Windows format
  if (getPlatform() === 'windows' &amp;&amp; trimmedPath.match(/^\/[a-z]\//i)) {
    processedPath = posixPathToWindowsPath(trimmedPath)
  }</code></pre><p>Finally, the resolution proper: absolute paths are normalized in place, relative paths are joined against the base directory and then normalized. This is the function's whole point &#8212; every code path emits an absolute, NFC-normalized, platform-native string.</p><pre><code>  if (isAbsolute(processedPath)) return normalize(processedPath).normalize('NFC')
  return resolve(actualBaseDir, processedPath).normalize('NFC')
}</code></pre><p>Two details matter. First, NFC Unicode normalization: macOS APFS returns NFD for accented filenames, while user input is usually NFC, so without normalization a path comparison can falsely report "different" for the same file. Second, the platform branch: a model trained on Linux examples will sometimes emit <code>/c/Users/...</code> on Windows, and the harness silently rewrites these so the agent doesn't have to know which OS it's on.</p><h3>Tracking cwd across BashTool calls via a marker file</h3><p>The Bash tool runs each command in a fresh subprocess, but the harness reconstructs persistent shell state by injecting a <code>pwd -P</code> marker after the user's command and reading it back. This is how <code>cd /tmp</code> in turn 5 still affects turn 6 even though there is no long-lived shell.</p><p>The outer shape is a <code>.then()</code> on the shell command's result promise. The first guard is the <code>backgroundTaskId</code> check: cwd updates only fire for foreground commands, because a backgrounded <code>cd</code> would leave the agent's logical cwd out of sync with what the user actually sees.</p><pre><code>// src/utils/Shell.ts
void shellCommand.result.then(async result =&gt; {
  // Only foreground tasks update the cwd
  if (result &amp;&amp; !preventCwdChanges &amp;&amp; !result.backgroundTaskId) {
    try {
      let newCwd = readFileSync(nativeCwdFilePath, { encoding: 'utf8' }).trim()
      if (getPlatform() === 'windows') {
        newCwd = posixPathToWindowsPath(newCwd)
      }</code></pre><p>Then the comparison is performed in NFC space &#8212; without this normalize, a UTF-8 filename like <code>caf&#233;</code> written as NFD on macOS APFS would always read back as "changed" even when the user never <code>cd</code>'d, triggering spurious hook fires every command.</p><pre><code>      // cwd is NFC-normalized (setCwdState); newCwd from `pwd -P` may be
      // NFD on macOS APFS. Normalize before comparing so Unicode paths
      // don't false-positive as "changed" on every command.
      if (newCwd.normalize('NFC') !== cwd) {
        setCwd(newCwd, cwd)
        invalidateSessionEnvCache()
        void onCwdChangedForHooks(cwd, newCwd)
      }
    } catch {
      logEvent('tengu_shell_set_cwd', { success: false })
    }
  }
})</code></pre><p><code>pwd -P</code> is the physical path &#8212; symlinks resolved &#8212; which is what the harness wants for permission comparisons. The <code>readFileSync</code>/<code>unlinkSync</code> are intentionally synchronous to avoid a microtask boundary that would let a follow-up tool call observe a stale cwd.</p><h3>setCwd canonicalizes through realpathSync</h3><p>When the harness commits a new cwd, it resolves symlinks via <code>realpathSync</code> so the stored value is always canonical. This is the deliberate symmetry to <code>pwd -P</code> on the bash side.</p><pre><code>// src/utils/Shell.ts
export function setCwd(path: string, relativeTo?: string): void {
  const resolved = isAbsolute(path)
    ? path
    : resolve(relativeTo || getFsImplementation().cwd(), path)
  // Resolve symlinks to match the behavior of pwd -P.
  let physicalPath: string
  try {
    physicalPath = getFsImplementation().realpathSync(resolved)
  } catch (e) {
    if (isENOENT(e)) {
      throw new Error(`Path "${resolved}" does not exist`)
    }
    throw e
  }
  setCwdState(physicalPath)
}</code></pre><h3>Sandbox boundary: snap back when cwd escapes</h3><p>After every Bash tool result, the harness checks whether the agent has wandered out of its allowed working directories and silently resets if so. This is the bridge between path <em>resolution</em> and path <em>containment</em>.</p><pre><code>// src/tools/BashTool/utils.ts
export function resetCwdIfOutsideProject(
  toolPermissionContext: ToolPermissionContext,
): boolean {
  const cwd = getCwd()
  const originalCwd = getOriginalCwd()
  const shouldMaintain = shouldMaintainProjectWorkingDir()
  if (
    shouldMaintain ||
    (cwd !== originalCwd &amp;&amp;
      !pathInAllowedWorkingPath(cwd, toolPermissionContext))
  ) {
    setCwd(originalCwd)
    if (!shouldMaintain) {
      logEvent('tengu_bash_tool_reset_to_original_dir', {})
      return true
    }
  }
  return false
}</code></pre><p><code>getOriginalCwd()</code> is the immutable startup anchor &#8212; it is never mutated by <code>cd</code>, so the harness always has a known-safe directory to fall back to.</p><h3>Subagent cwd inheritance via wrapWithCwd</h3><p>When the AgentTool spawns a subagent &#8212; including for explicit <code>cwd</code> overrides or worktree isolation &#8212; it wraps the entire agent lifecycle in a <code>runWithCwdOverride</code> so every nested tool call sees the right directory.</p><pre><code>// src/tools/AgentTool/AgentTool.tsx
// Helper to wrap execution with a cwd override: explicit cwd arg (KAIROS)
// takes precedence over worktree isolation path.
const cwdOverridePath = cwd ?? worktreeInfo?.worktreePath;
const wrapWithCwd = &lt;T,&gt;(fn: () =&gt; T): T =&gt;
  cwdOverridePath ? runWithCwdOverride(cwdOverridePath, fn) : fn();</code></pre><p>Because <code>AsyncLocalStorage</code> propagates through the entire async tree, a Read tool call deep inside a subagent's nested generator still sees the override &#8212; even if other subagents are concurrently using a different override.</p><h3>Symlink-resolved permission checks</h3><p>The permission layer uses the same canonicalization the cwd layer uses. <code>safeResolvePath</code> calls <code>realpathSync</code> defensively, with explicit handling for FIFOs and sockets that would block.</p><p>The function signature returns three flags rather than just a path: the resolved path itself, whether it was a symlink, and whether the result is canonical. The first guard short-circuits on UNC paths (<code>\\server\share\&#8230;</code>), which on Windows would trigger a DNS or SMB lookup before we've even decided whether to touch the file.</p><pre><code>// src/utils/fsOperations.ts
export function safeResolvePath(
  fs: FsOperations,
  filePath: string,
): { resolvedPath: string; isSymlink: boolean; isCanonical: boolean } {
  // Block UNC paths before any filesystem access to prevent network requests
  if (filePath.startsWith('//') || filePath.startsWith('\\\\')) {
    return { resolvedPath: filePath, isSymlink: false, isCanonical: false }
  }</code></pre><p>The next chunk does a defensive <code>lstatSync</code> before any <code>realpathSync</code> &#8212; <code>realpathSync</code> will block indefinitely on a FIFO waiting for a writer, so the harness inspects the file type first and bails out for anything that could hang.</p><pre><code>  try {
    // realpathSync can block on FIFOs waiting for a writer.
    const stats = fs.lstatSync(filePath)
    if (stats.isFIFO() || stats.isSocket() ||
        stats.isCharacterDevice() || stats.isBlockDevice()) {
      return { resolvedPath: filePath, isSymlink: false, isCanonical: false }
    }
    const resolvedPath = fs.realpathSync(filePath)
    return { resolvedPath, isSymlink: resolvedPath !== filePath, isCanonical: true }
  } catch (_error) {
    return { resolvedPath: filePath, isSymlink: false, isCanonical: false }
  }
}</code></pre><p>The <code>isCanonical</code> flag is performance-load-bearing: when set, callers skip five redundant syscalls during permission checks.</p><h2>3. Hermes Agent Implementation</h2><p>Hermes solves the same problem with a different topology. Where Claude Code uses a global TypeScript module with <code>AsyncLocalStorage</code>, Hermes uses a per-environment Python object that wraps the actual execution backend (local subprocess, Docker container, Modal sandbox, SSH session, etc.). Each environment carries its own <code>self.cwd</code>, and after every command an injected bash epilogue writes the new pwd to a temp file or stdout marker.</p><div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" href="https://substackcdn.com/image/fetch/$s_!zxK1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fef71b50e-d93d-4c95-998e-02f6f7593828_1800x1080.png" target="_blank"><div class="image2-inset"><source type="image/webp" /><img alt="Figure 4.2: Two implementations reconstruct cwd across stateless subprocesses" class="sizing-normal" height="1080" src="https://substackcdn.com/image/fetch/$s_!zxK1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fef71b50e-d93d-4c95-998e-02f6f7593828_1800x1080.png" title="Figure 4.2: Two implementations reconstruct cwd across stateless subprocesses" width="1800" /><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset"><button class="pencraft pc-reset pencraft icon-container restack-image" tabindex="0" type="button"><svg fill="none" height="20" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><g><title></title><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button class="pencraft pc-reset pencraft icon-container view-image" tabindex="0" type="button"><svg class="lucide lucide-maximize2 lucide-maximize-2" fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button></div></div></div></a></figure></div><p><em>Figure 4.2.</em> The two harnesses reach the same property by different routes. Claude Code chains an immutable <code>getOriginalCwd()</code> anchor with global state and an <code>AsyncLocalStorage</code> override, all consulted through one <code>getCwd()</code> accessor. Hermes injects a bash epilogue that emits <code>pwd -P</code> to both a marker file and a stdout marker, then parses whichever channel the backend supports.</p><h3></h3>
      <p>
          <a href="https://kenhuangus.substack.com/p/chapter-4-working-directory-and-file">
              Read more
          </a>
      </p>
