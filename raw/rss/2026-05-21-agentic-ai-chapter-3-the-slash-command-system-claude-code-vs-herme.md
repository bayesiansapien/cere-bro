---
source: farmer/rss
feed: agentic-ai
farmed: 2026-05-22T10:11:42.649379+00:00
title: Chapter 3: The Slash Command System (Claude Code vs. Hermes Agent)
url: https://kenhuangus.substack.com/p/chapter-3-the-slash-command-system
published: 2026-05-21
author: Ken Huang
---

# Chapter 3: The Slash Command System (Claude Code vs. Hermes Agent)

<p>This article is a series of total 10 posts. The <a href="https://kenhuangus.substack.com/p/chapter-1-cost-and-token-usage-accounting">chapter 1</a> and <a href="https://kenhuangus.substack.com/p/chapter-2-cancellation-and-abort">chapter 2</a> are already released. Read on for how to subscibe to unlock total 10 posts in the following weeks.</p><h2>1. Pattern Summary</h2><p>The slash command system is the agent's <em>meta-language</em> &#8212; a small surface area where the user talks directly to the harness instead of through the model. When an analyst types <code>/clear</code>, <code>/cost</code>, <code>/compact</code>, or <code>/help</code>, no token is sent to Claude or Hermes; the harness intercepts the input, dispatches to a local handler, and responds with text, a dialog, or a state mutation. This is structurally distinct from skills (model-invoked, Chapter 12) and tools (model-called, Chapter 2). Slash commands are the third leg of the user &#8594; harness &#8594; model triangle: the model never sees <code>/cost</code> because the cost report is a pure harness fact, not something the model needs to reason about. Getting this layer right is the difference between a chat box and an operator's console &#8212; it is where the human keeps direct, model-bypassing control over the session.</p><div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" href="https://substackcdn.com/image/fetch/$s_!ytia!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F74c93fb8-4720-472a-9ee5-f60da3ef97d1_1800x960.png" target="_blank"><div class="image2-inset"><source type="image/webp" /><img alt="Figure 3.1: Slash commands route directly to the harness, bypassing the model" class="sizing-normal" height="960" src="https://substackcdn.com/image/fetch/$s_!ytia!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F74c93fb8-4720-472a-9ee5-f60da3ef97d1_1800x960.png" title="Figure 3.1: Slash commands route directly to the harness, bypassing the model" width="1800" /><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset"><button class="pencraft pc-reset pencraft icon-container restack-image" tabindex="0" type="button"><svg fill="none" height="20" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><g><title></title><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button class="pencraft pc-reset pencraft icon-container view-image" tabindex="0" type="button"><svg class="lucide lucide-maximize2 lucide-maximize-2" fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button></div></div></div></a></figure></div><p><em>Figure 3.1.</em> User input is split at the dispatcher: anything starting with <code>/</code> is intercepted by the harness and routed to a local, modal, or prompt-generating handler &#8212; most flavors never cross the user/model boundary, so commands like <code>/clear</code> and <code>/cost</code> cost no tokens and cannot be triggered by prompt injection.</p><p></p><p>Before you read on &#8212; two quick announcements. First, you can now get 50% off a yearly subscription and unlock all paid content on Agentic AI, AI Security, and more: <a href="https://kenhuangus.substack.com/subscribe?coupon=302342d9">https://kenhuangus.substack.com/subscribe?coupon=302342d9</a>.</p><p>Second, all previously written 15 Hermes Agent and Claude Code agentic harness design patterns are now available in a single book on Amazon: <a href="https://www.amazon.com/Agentic-AI-Harness-Pattern-Patterns-ebook/dp/B0H13XWS8W">https://www.amazon.com/Agentic-AI-Harness-Pattern-Patterns-ebook/dp/B0H13XWS8W</a></p><h2>2. Claude Code Implementation</h2><p>Claude Code's slash command system lives across three files: <code>src/types/command.ts</code> defines the <code>Command</code> shape, <code>src/commands.ts</code> is the registry, and <code>src/utils/processUserInput/processSlashCommand.tsx</code> is the dispatcher. The architecture is plugin-friendly from the ground up &#8212; built-in commands, plugin commands, MCP commands, and dynamically discovered skills all flow through the same <code>Command[]</code> array.</p><h3>2.1 The Command type &#8212; three execution flavors</h3><p>Every slash command in Claude Code is a <code>Command</code>, defined as a discriminated union of three execution modes plus a shared metadata base. The base captures everything the typeahead and help UI need without forcing the command to declare how it runs.</p><pre><code>// src/types/command.ts &#8212; shared metadata for every command
export type CommandBase = {
  availability?: CommandAvailability[]
  description: string
  isEnabled?: () =&gt; boolean
  /** Defaults to false. Only set when the command should be hidden from typeahead/help. */
  isHidden?: boolean
  name: string
  aliases?: string[]
  argumentHint?: string // Hint text for command arguments
  loadedFrom?: 'commands_DEPRECATED' | 'skills' | 'plugin' | 'managed' | 'bundled' | 'mcp'
  immediate?: boolean // executes immediately, bypasses queue
  isSensitive?: boolean // args are redacted from conversation history
}</code></pre><p>Note <code>availability</code> and <code>isEnabled()</code> are deliberately separate. <code>availability</code> is a static auth-environment filter (<code>'claude-ai' | 'console'</code>) &#8212; who is <em>allowed</em> to use this. <code>isEnabled()</code> runs every render and reads feature flags or env vars &#8212; whether it is <em>turned on right now</em>. The split lets the user's account state hide a command without recomputing the registry.</p><p>The discriminator <code>type</code> selects one of three runtime shapes. The first, <code>local</code>, is the simplest &#8212; a side-effecting handler that returns text:</p><pre><code>// src/types/command.ts &#8212; type:'local' executes a side effect, returns text
type LocalCommand = {
  type: 'local'
  supportsNonInteractive: boolean
  load: () =&gt; Promise&lt;LocalCommandModule&gt;
}

export type LocalCommandResult =
  | { type: 'text'; value: string }
  | { type: 'compact'; compactionResult: CompactionResult; displayText?: string }
  | { type: 'skip' } // suppress any transcript entry</code></pre><p><code>/clear</code> is the canonical <code>local</code> command &#8212; its <code>call()</code> mutates conversation state and returns empty text. The <code>type: 'skip'</code> variant exists because some commands (<code>/clear</code>, <code>/redraw</code>) want zero footprint in the transcript.</p><p>The second flavor, <code>local-jsx</code>, opens a React modal. Instead of returning a value, the command receives an <code>onDone</code> callback and renders a component:</p><pre><code>// src/types/command.ts &#8212; type:'local-jsx' renders a modal, calls onDone() to close
export type LocalJSXCommandCall = (
  onDone: LocalJSXCommandOnDone,
  context: ToolUseContext &amp; LocalJSXCommandContext,
  args: string,
) =&gt; Promise&lt;React.ReactNode&gt;

type LocalJSXCommand = {
  type: 'local-jsx'
  load: () =&gt; Promise&lt;LocalJSXCommandModule&gt;
}</code></pre><p><code>/help</code>, <code>/login</code>, <code>/config</code>, <code>/cost</code> are all <code>local-jsx</code> &#8212; they paint a full-screen pane the user navigates with arrow keys. The <code>onDone</code> callback is how the modal communicates back to the harness when the user dismisses it.</p><p>The third flavor is <code>prompt</code>, and this is the bridge between slash commands and skills. A <code>prompt</code> command produces content blocks that are <em>injected as a user message</em> &#8212; meaning the model does see it, but the user invoked it directly via <code>/name</code>:</p><pre><code>// src/types/command.ts &#8212; type:'prompt' generates content for the model
export type PromptCommand = {
  type: 'prompt'
  progressMessage: string
  contentLength: number       // for token estimation
  source: SettingSource | 'builtin' | 'mcp' | 'plugin' | 'bundled'
  context?: 'inline' | 'fork' // inline expands into convo; fork = sub-agent
  paths?: string[]            // skill is only visible after model touches matching files
  getPromptForCommand(args: string, context: ToolUseContext): Promise&lt;ContentBlockParam[]&gt;
}</code></pre><p>The <code>Command</code> union ties these together with the base metadata:</p><pre><code>// src/types/command.ts &#8212; discriminated union
export type Command = CommandBase &amp;
  (PromptCommand | LocalCommand | LocalJSXCommand)</code></pre><p>This three-flavor split is load-bearing. The harness inspects <code>command.type</code> to decide whether the command runs purely locally (<code>local</code>), opens UI (<code>local-jsx</code>), or routes back into the query loop with a synthetic message (<code>prompt</code>). Only the <code>prompt</code> flavor crosses the user &#8594; model boundary; <code>local</code> and <code>local-jsx</code> never reach Claude.</p><div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" href="https://substackcdn.com/image/fetch/$s_!Vujw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd058f3f0-22fd-44b4-b88c-ff61b3792cee_1800x1080.png" target="_blank"><div class="image2-inset"><source type="image/webp" /><img alt="Figure 3.2: Claude Code's three-flavor Command discriminated union" class="sizing-normal" height="1080" src="https://substackcdn.com/image/fetch/$s_!Vujw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd058f3f0-22fd-44b4-b88c-ff61b3792cee_1800x1080.png" title="Figure 3.2: Claude Code's three-flavor Command discriminated union" width="1800" /><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset"><button class="pencraft pc-reset pencraft icon-container restack-image" tabindex="0" type="button"><svg fill="none" height="20" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><g><title></title><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button class="pencraft pc-reset pencraft icon-container view-image" tabindex="0" type="button"><svg class="lucide lucide-maximize2 lucide-maximize-2" fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button></div></div></div></a></figure></div><p><em>Figure 3.2.</em> Every Claude Code command shares the same <code>CommandBase</code> metadata (name, description, aliases, isHidden) but specializes via the <code>type</code> discriminator. <code>local</code> runs a side effect and returns text; <code>local-jsx</code> paints a React modal that calls back through <code>onDone</code>; <code>prompt</code> produces content blocks injected as a synthetic user message &#8212; only the third flavor crosses the user/model boundary, which is the design's central guarantee.</p><h3>2.2 The registry &#8212; built-ins, plugins, MCP, skills</h3><p>The <code>COMMANDS</code> array in <code>src/commands.ts</code> is the static built-in list. It is wrapped in <code>lodash.memoize</code> so it is computed once, but each entry is a plain object literal &#8212; not a class &#8212; so the file reads almost like a configuration manifest. Here is the start of it:</p><pre><code>// src/commands.ts &#8212; the static built-in registry, memoized once
const COMMANDS = memoize((): Command[] =&gt; [
  addDir,
  advisor,
  agents,
  branch,
  clear,
  compact,
  config,
  cost,
  diff,
  doctor,
  help,
  init,
  // ... ~80 more built-ins
])</code></pre><p>Notice there is no <code>register()</code> call anywhere. Each command is a default-exported object that conforms to the <code>Command</code> type, and the array order is the only registration. Compare this to Hermes (next section), which uses a dataclass registry &#8212; Claude Code's approach is more of a lookup table than a registry.</p><p>The actual definition of each entry is intentionally minimal. Take <code>clear</code> &#8212; the index file is metadata only, with the implementation lazy-loaded:</p><pre><code>// src/commands/clear/index.ts &#8212; metadata only, lazy-loaded implementation
import type { Command } from '../../commands.js'

const clear = {
  type: 'local',
  name: 'clear',
  description: 'Clear conversation history and free up context',
  aliases: ['reset', 'new'],
  supportsNonInteractive: false,
  load: () =&gt; import('./clear.js'),
} satisfies Command

export default clear</code></pre><p>The lazy <code>load: () =&gt; import('./clear.js')</code> is critical for startup time &#8212; the typeahead needs all 80+ command names instantly, but the heavyweight implementations (which pull in React, the compact algorithm, the rendering pipeline) only get loaded when the user actually types the slash. Cost weighs in at a few hundred lines that run analytics queries; the index file is 23.</p><p><code>/cost</code> shows how <code>isHidden</code> adapts the registry to user state at lookup time:</p><pre><code>// src/commands/cost/index.ts &#8212; isHidden gates visibility per user
const cost = {
  type: 'local',
  name: 'cost',
  description: 'Show the total cost and duration of the current session',
  get isHidden() {
    if (process.env.USER_TYPE === 'ant') return false
    return isClaudeAISubscriber()
  },
  supportsNonInteractive: true,
  load: () =&gt; import('./cost.js'),
} satisfies Command</code></pre><p>The <code>get isHidden()</code> getter &#8212; not a static value &#8212; means the typeahead re-evaluates visibility on every render. When the user logs in via <code>/login</code> and switches from API-key auth to a Claude.ai subscription, <code>/cost</code> quietly disappears from the autocomplete because subscribers do not pay per token. No event bus, no cache invalidation &#8212; just a getter.</p><p>Beyond the static built-ins, <code>getCommands()</code> in <code>src/commands.ts</code> merges in plugin commands, MCP commands, dynamic skills, and plugin-provided skills. The merge handles deduplication and ordering carefully &#8212; dynamic skills are inserted <em>after</em> plugin skills but <em>before</em> built-ins:</p><pre><code>// src/commands.ts &#8212; getCommands merges built-ins with dynamic skills
export async function getCommands(cwd: string): Promise&lt;Command[]&gt; {
  const allCommands = await loadAllCommands(cwd)
  const dynamicSkills = getDynamicSkills()
  const baseCommands = allCommands.filter(
    _ =&gt; meetsAvailabilityRequirement(_) &amp;&amp; isCommandEnabled(_),
  )
  if (dynamicSkills.length === 0) return baseCommands

  // Dedupe &#8212; only add dynamic skills not already present
  const baseCommandNames = new Set(baseCommands.map(c =&gt; c.name))
  const uniqueDynamicSkills = dynamicSkills.filter(
    s =&gt; !baseCommandNames.has(s.name) &amp;&amp;
         meetsAvailabilityRequirement(s) &amp;&amp; isCommandEnabled(s),
  )
  return [...baseCommands, ...uniqueDynamicSkills]
}</code></pre><p>The two-pass filter &#8212; <code>meetsAvailabilityRequirement &amp;&amp; isCommandEnabled</code> &#8212; applies on every call, not just once at startup. That is what makes <code>/login</code> immediately switch the visible command set: the auth state changes, the next render of the typeahead runs the predicates again, and the right commands appear or vanish.</p><h3>2.3 The dispatcher &#8212; parsing and routing</h3><p></p>
      <p>
          <a href="https://kenhuangus.substack.com/p/chapter-3-the-slash-command-system">
              Read more
          </a>
      </p>
