---
source: farmer/rss
feed: agentic-ai
farmed: 2026-04-30T00:00:00+00:00
title: "Chapter 10: Production Deployment Patterns (Claude Code vs. Hermes Agent)"
url: https://kenhuangus.substack.com/p/chapter-10-production-deployment
published: 2026-04-27
author: Ken Huang
---

# Chapter 10: Production Deployment Patterns (Claude Code vs. Hermes Agent)

<h2>1. Pattern Summary</h2><p>Production deployment is where the harness meets the real world: multiple users, multiple environments, scheduled automation, and the need to embed the agent into existing infrastructure. A prototype that works on a developer's laptop needs to survive API outages, multi-tenant isolation, cost overruns, and compliance audits before it earns the label "production." Both Claude Code and Hermes Agent have thought hard about this problem &#8212; but from opposite directions. Claude Code is SDK-first: it exposes an async generator interface designed to be embedded inside other applications. Hermes is CLI/gateway-first: it ships as a standalone agent that users interact with directly, across messaging platforms, on a schedule, or from the command line. Understanding both deployment philosophies lets you pick the right tool for each layer of your stack &#8212; and combine them when the job demands it.</p><h2>2. Claude Code Implementation</h2><h3>SDK Async Generator Interface</h3><p>The core of Claude Code's production story is the <code>ask()</code> convenience wrapper and the <code>QueryEngine.submitMessage()</code> method underneath it. Both return async generators, which means SDK consumers receive events as they happen rather than waiting for a full response:</p><pre><code>// src/QueryEngine.ts &#8212; the low-level SDK surface
export class QueryEngine {
  async *submitMessage(
    prompt: string | ContentBlockParam[],
    options?: { uuid?: string; isMeta?: boolean },
  ): AsyncGenerator&lt;SDKMessage, void, unknown&gt; {
    // Yields one SDKMessage per event: assistant text, tool use,
    // tool result, compaction boundary, retry notice, final result.
    // Consumers iterate with `for await (const msg of engine.submitMessage(...))`
  }
}</code></pre><pre><code>// src/QueryEngine.ts &#8212; the convenience wrapper for one-shot usage
export async function* ask({
  prompt,
  tools,
  mcpClients,
  canUseTool,
  mutableMessages = [],
  maxTurns,
  maxBudgetUsd,
  // ... 20+ more options
}): AsyncGenerator&lt;SDKMessage, void, unknown&gt; {
  const engine = new QueryEngine({ /* all options forwarded */ })
  try {
    yield* engine.submitMessage(prompt, { uuid: promptUuid })
  } finally {
    // Propagate file cache back to caller even on error
    setReadFileCache(engine.getReadFileState())
  }
}</code></pre><p>The <code>SDKMessage</code> union covers every event type a consumer needs: assistant text, tool use summaries, compaction boundaries, retry notices, and final results. A SIEM integration, a web UI, or a CI pipeline can all consume the same stream and filter for the events they care about.</p><h3>30 Compile-Time Feature Flags</h3><p>Claude Code ships with 30 feature flags that control experimental capabilities. In the external build, every flag returns <code>false</code> &#8212; dead code is eliminated at bundle time by the bundler:</p><pre><code>// src/entrypoints/cli.tsx &#8212; polyfill for external builds
function feature(name: string): boolean {
  return false  // All flags off; bundler tree-shakes the dead branches
}

// Usage pattern: conditional import eliminates the module from the bundle
const reactiveCompact = feature('REACTIVE_COMPACT')
  ? require('./services/compact/reactiveCompact.js')
  : null

// Usage pattern: inline gate for experimental code paths
if (feature('CONTEXT_COLLAPSE') &amp;&amp; contextCollapse) {
  messagesForQuery = await contextCollapse.applyCollapsesIfNeeded(...)
}</code></pre><p>The 30 flags span six categories: autonomous agents (<code>KAIROS</code>, <code>COORDINATOR_MODE</code>, <code>BUDDY</code>), remote/distributed (<code>BRIDGE_MODE</code>, <code>DAEMON</code>, <code>SSH_REMOTE</code>), communication (<code>UDS_INBOX</code>), enhanced tools (<code>WEB_BROWSER_TOOL</code>, <code>VOICE_MODE</code>, <code>MCP_SKILLS</code>), conversation management (<code>HISTORY_SNIP</code>, <code>ULTRAPLAN</code>), and infrastructure (<code>HARD_FAIL</code>, <code>TRANSCRIPT_CLASSIFIER</code>, <code>TORCH</code>). Internal Anthropic builds replace the polyfill with a real feature flag service, enabling gradual rollouts and A/B testing without redeployment.</p><h3>Multi-Provider Support</h3><p>The harness abstracts over four cloud providers through a unified API client layer:</p><div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" href="https://substackcdn.com/image/fetch/$s_!RHH_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb4013d3d-c435-4448-a511-470767f76b1f_453x249.png" target="_blank"><div class="image2-inset"><source type="image/webp" /><img alt="Comparison table" class="sizing-normal" height="249" src="https://substackcdn.com/image/fetch/$s_!RHH_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb4013d3d-c435-4448-a511-470767f76b1f_453x249.png" title="Comparison table" width="453" /><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset"><button class="pencraft pc-reset pencraft icon-container restack-image" tabindex="0" type="button"><svg fill="none" height="20" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><g><title></title><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button class="pencraft pc-reset pencraft icon-container view-image" tabindex="0" type="button"><svg class="lucide lucide-maximize2 lucide-maximize-2" fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button></div></div></div></a></figure></div><p>Model selection at runtime considers permission mode, user-specified overrides, and whether the context exceeds 200K tokens &#8212; the harness can automatically switch to a larger context model mid-session.</p><h3>Plugin System and MCP Integration</h3><pre><code>// src/utils/plugins/pluginLoader.js &#8212; load plugins from cache, no network call
export async function loadAllPluginsCacheOnly(): Promise&lt;{ enabled: Plugin[] }&gt; {
  // Scans plugin directories, validates manifests, returns enabled plugins.
  // Plugins inject custom tools into the system prompt at session start.
}</code></pre><p>MCP (Model Context Protocol) integration spans 24 files and 12K+ lines. MCP tools are namespaced as <code>mcp__server__tool</code> so the harness can route calls to the right server:</p><pre><code>// Extract server name from a namespaced MCP tool call
if (tool.name?.startsWith('mcp__')) {
  const parts = tool.name.split('__')
  const serverName = parts[1]  // e.g. "mcp__filesystem__read_file" &#8594; "filesystem"
}</code></pre><h3>Deployment Checklist (from chapter10.md)</h3><p>The Claude Code deployment checklist covers five areas: <strong>Infrastructure</strong> (secrets manager, rate limiting, multi-region, monitoring); <strong>Security</strong> (permission modes, tool allow/deny lists, sandbox isolation, PII filtering, audit logging); <strong>Reliability</strong> (circuit breakers, retry with backoff, graceful degradation, budget limits); <strong>Observability</strong> (structured logging with correlation IDs, cost tracking, health checks); <strong>Performance</strong> (token counting, prompt caching, concurrent tool limits).</p><h2>3. Hermes Agent Implementation</h2><h3>CLI + Gateway Dual Entry Points</h3><p>Hermes ships two production entry points. The <code>hermes</code> CLI is for interactive use and scripted automation. The gateway is for always-on messaging platform integration:</p><pre><code># hermes-agent/hermes_cli/main.py &#8212; the full CLI surface
# hermes                     &#8594; interactive chat
# hermes gateway start       &#8594; start gateway as a background service
# hermes cron                &#8594; manage scheduled jobs
# hermes doctor              &#8594; check config and dependencies
# hermes model               &#8594; switch models at runtime
# hermes sessions browse     &#8594; interactive session picker
# hermes acp                 &#8594; run as ACP server for editor integration</code></pre><pre><code># hermes-agent/gateway/run.py &#8212; messaging gateway entry point
# Manages platform adapters for: Telegram, Discord, Slack, WhatsApp,
# Signal, Matrix, Mattermost, DingTalk, Feishu, WeCom, SMS, Email, Webhook.
# Each platform runs as an async adapter; the gateway multiplexes them
# all under a single process with a shared agent backend.

async def start_gateway():
    """Start all configured platform adapters."""
    # Handles SSL cert auto-detection for NixOS and non-standard systems
    _ensure_ssl_certs()
    # Loads platform configs, starts adapters, runs event loop</code></pre><h3>Profile System: HERMES_HOME Isolation</h3><p>Multi-tenant isolation in Hermes is built on the <code>HERMES_HOME</code> environment variable. Each profile gets its own directory with its own config, keys, sessions, and memories:</p><pre><code># hermes-agent/hermes_constants.py &#8212; single source of truth for home dir
def get_hermes_home() -&gt; Path:
    """Return the Hermes home directory (default: ~/.hermes).

    Override with HERMES_HOME to isolate profiles:
      HERMES_HOME=~/.hermes/profiles/analyst1 hermes chat
      HERMES_HOME=~/.hermes/profiles/analyst2 hermes chat
    Each profile has its own config.yaml, .env, sessions/, memories/, cron/.
    """
    return Path(os.getenv("HERMES_HOME", Path.home() / ".hermes"))

def display_hermes_home() -&gt; str:
    """User-friendly display: ~/.hermes/profiles/analyst1 &#8594; ~/...analyst1"""
    home = get_hermes_home()
    try:
        return "~/" + str(home.relative_to(Path.home()))
    except ValueError:
        return str(home)</code></pre><p>The <code>ensure_hermes_home()</code> function in <code>config.py</code> creates the full directory structure with secure permissions (0700 for dirs, 0600 for files) on first run &#8212; so spinning up a new tenant profile is a single <code>mkdir</code> + env var.</p><h3>Runtime Config: DEFAULT_CONFIG and config.yaml</h3><p>Hermes uses a layered config system. <code>DEFAULT_CONFIG</code> in <code>config.py</code> defines every settable value with sensible defaults; <code>~/.hermes/config.yaml</code> overrides them at runtime without redeployment:</p><pre><code># hermes-agent/hermes_cli/config.py &#8212; DEFAULT_CONFIG (selected fields)
DEFAULT_CONFIG = {
    "model": "",                    # Empty = use provider default
    "providers": {},                # Per-provider API key overrides
    "fallback_providers": [],       # Ordered fallback chain on API error
    "toolsets": ["hermes-cli"],     # Active toolset groups
    "agent": {
        "max_turns": 90,            # Hard iteration cap per conversation
        "gateway_timeout": 1800,    # Inactivity timeout for gateway sessions (seconds)
        "tool_use_enforcement": "auto",  # Force tool calls for gpt/codex models
    },
    "compression": {
        "enabled": True,
        "threshold": 0.50,          # Compress when context &gt; 50% full
        "target_ratio": 0.20,       # Keep 20% of threshold as recent tail
        "protect_last_n": 20,       # Always keep last 20 messages verbatim
    },
    "terminal": {
        "backend": "local",         # local | ssh | docker | modal | daytona
        "timeout": 180,
        "docker_image": "nikolaik/python-nodejs:python3.11-nodejs20",
        "container_memory": 5120,   # MB
    },
    # ... auxiliary model config, browser config, checkpoint config
}</code></pre><p>Optional env vars (defined in <code>_EXTRA_ENV_KEYS</code>) cover platform tokens, SSH keys, and provider credentials &#8212; all stored in <code>~/.hermes/.env</code> with 0600 permissions.</p><h3>200+ Models via OpenRouter</h3><p>Hermes routes through OpenRouter by default, giving access to 200+ models from a single API key. Model switching is a runtime operation &#8212; no redeployment needed:</p><pre><code># Switch models at runtime &#8212; updates config.yaml immediately
hermes model

# Or set per-session via env var
HERMES_MODEL=anthropic/claude-opus-4-5 hermes chat

# Or per-cron-job in the job definition
# { "model": "google/gemini-2.5-pro", "schedule": "0 2 * * *", ... }</code></pre><p>The <code>smart_model_routing</code> config block can automatically route simple queries to a cheap model and complex ones to a capable model &#8212; cost optimization without code changes.</p><h3>Built-In Cron Scheduling</h3><p>Hermes ships a production-grade cron scheduler. Jobs are defined in <code>~/.hermes/cron/</code> and executed by the gateway's background thread every 60 seconds:</p><pre><code># hermes-agent/cron/scheduler.py &#8212; tick() runs due jobs
# Uses a file-based lock (~/.hermes/cron/.tick.lock) so only one tick
# runs at a time even if gateway + daemon + systemd timer overlap.

def run_job(job: dict) -&gt; tuple[bool, str, str, Optional[str]]:
    """Execute a single cron job via AIAgent.run_conversation().

    - Loads config.yaml fresh every run (no restart needed for key rotation)
    - Injects HERMES_CRON_AUTO_DELIVER_* env vars for platform delivery
    - Enforces inactivity timeout (default 600s) via ThreadPoolExecutor
    - Saves output to ~/.hermes/cron/sessions/ for audit
    - Delivers result to origin chat, specific platform, or local-only
    """
    agent = AIAgent(
        model=turn_route["model"],
        quiet_mode=True,
        skip_memory=True,       # Cron prompts shouldn't corrupt user memory
        platform="cron",
        session_id=_cron_session_id,
        session_db=_session_db, # SQLite persistence for post-run search
    )
    # Inactivity-based timeout: job can run for hours if actively calling tools,
    # but a hung API call with no activity for 600s is killed and logged.
    result = _run_with_inactivity_timeout(agent, prompt, limit=600)</code></pre><p>The <code>[SILENT]</code> sentinel lets a cron job suppress delivery when there's nothing new to report &#8212; the output is still saved locally for audit, but the user's chat isn't spammed.</p><h3>Skills Hub</h3><p>Hermes integrates with agentskills.io, an open standard for shareable agent skills. Skills are reusable prompt workflows that can be invoked from cron jobs, chat sessions, or the gateway:</p><pre><code># Skills can be loaded into cron jobs by name
job = {
    "name": "nightly-threat-hunt",
    "schedule": "0 2 * * *",
    "skills": ["threat-hunt-v2"],   # Loaded from agentskills.io or ~/.hermes/skills/
    "prompt": "Focus on lateral movement indicators from the last 24h.",
    "deliver": "origin",
}</code></pre><h2>4. Side-by-Side Comparison Table</h2><div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" href="https://substackcdn.com/image/fetch/$s_!ckIL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff3f24e42-a255-4f20-8d4c-670f58dd7b5f_1022x451.png" target="_blank"><div class="image2-inset"><source type="image/webp" /><img alt="Comparison table" class="sizing-normal" height="451" src="https://substackcdn.com/image/fetch/$s_!ckIL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff3f24e42-a255-4f20-8d4c-670f58dd7b5f_1022x451.png" title="Comparison table" width="1022" /><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset"><button class="pencraft pc-reset pencraft icon-container restack-image" tabindex="0" type="button"><svg fill="none" height="20" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"><g><title></title><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button class="pencraft pc-reset pencraft icon-container view-image" tabindex="0" type="button"><svg class="lucide lucide-maximize2 lucide-maximize-2" fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button></div></div></div></a></figure></div><h2>5. When to Use Which</h2><p><strong>Use Claude Code when:</strong></p><ul><li><p></p></li></ul>
      <p>
          <a href="https://kenhuangus.substack.com/p/chapter-10-production-deployment">
              Read more
          </a>
      </p>