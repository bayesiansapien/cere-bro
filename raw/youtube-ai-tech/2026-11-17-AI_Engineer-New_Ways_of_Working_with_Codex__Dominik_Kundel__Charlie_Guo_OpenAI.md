# New Ways of Working with Codex (Dominik Kundel & Charlie Guo, OpenAI)

**Channel:** AI Engineer
**Published:** 2026-11-17
**Source:** https://www.youtube.com/watch?v=IPh9YsWvDQk

## TL;DR
OpenAI's devex team argues Codex is no longer a coding CLI but the shared agent harness behind ChatGPT work, Slack, Dots (always-on agents) and the new Agents API. The July to November 2026 feature wave centers on five themes: context (plugins, app shots, computer history), iteration (Ultra Fast + live annotations), cloud execution (Codex Cloud v2 with auto-configured, snapshotted environments), shipping (ChatGPT Sites with DB/storage/auth), and delegation (voice as control plane, Dots, peer sub-agents). Their core advice: turn reasoning effort down and let a mid-tier model escalate to bigger sub-agents.

## Key Takeaways
- **One harness everywhere:** plugins (MCP servers + skills + resources, mostly remote MCP) connect once and work across desktop, CLI, ChatGPT web, Slack and Dots. This enables "vague prompting", where the agent resolves ambiguous references from Slack/Drive context.
- **Plugin extensions** let you modify the desktop/ChatGPT UI itself (sidebars, panels, composer autocomplete). Built-in features like Sites and code review are themselves plugins.
- **App shots** (⌘+⌘ on Mac) capture screenshot plus the full accessibility tree, including off-screen content. This is richer and cheaper context than raw screenshots.
- **Computer history** (macOS) learns your app usage from OS event streams rather than screenshots, which is more token-efficient, and turns it into memories. It supports pause, retroactive clear and per-app exclusion.
- **Ultra Fast:** ~8x faster at ~6x cost on GPT-6/6.1 Sol and GPT-6 Astra. Worth it only for tight interactive loops with a hot-reload dev server on "light" reasoning. Useless when build/test time dominates.
- **Codex Cloud v2:** multi-repo environments, auto-discovered setup scripts, snapshotting plus background dependency refresh for near-instant resume, Tailscale/OIDC for private resources. Bring-your-own hardware (e.g. Mac for iOS builds) is in progress. `codex remote-control start` exposes a headless dev box to your phone.
- **ChatGPT Sites** are full apps: D1 database, R2 object storage, Sign in with ChatGPT auth, plugins, secrets. Internal example: "Cut Room", where an agent with DaVinci Resolve skills autonomously edits launch videos. Some GPT-6 Astra secondary launch videos were fully agent-edited.
- **Delegation patterns:** a voice mode that drives the whole app; Dots as safety net (caught a PR bug, a merge conflict, a calendar clash, a nearby wildfire) and as a delegation sink; peer sub-agents that coordinate across web/mobile workstreams; threads that spawn independent threads.
- **Speed-round tips:** default to high (not xhigh) reasoning and step down one notch per new model generation. Use Sol-medium as orchestrator spawning Astra-high sub-agents for hard bits and Luna-high sub-agents for tedious bits. Re-test old workflows on every model release and drop scaffolding that no longer helps.

## Architecture & Optimization Mechanics
- **Model cascade inside the agent:** "Sol-medium orchestrator escalates to Astra-high or fans out to Luna" is an in-harness LLM router. The speakers concede it is "not always better or cheaper" because the models still misjudge which tier a subtask needs. That routing-decision quality is exactly Amit's research problem.
- **Ultra Fast is a latency/cost trade, not a throughput win:** 8x speed for 6x price implies dedicated low-batch serving (likely smaller batch sizes and speculative decoding on reserved capacity). End-to-end gains are Amdahl-bounded by tool and build time.
- **Context efficiency moves:** accessibility trees over pixels, and OS event streams over screenshots, are deliberate token-compression choices. Structured context beats vision tokens for agent loops.
- **Environment snapshotting** amortizes cold-start (dependency install, warm caches), the agent-infra analog of KV-cache reuse.

## Grounded Context (Web Enrichment)
Feature claims line up with DevDay 2026 (Sept 29, 2026, San Francisco), which OpenAI billed as its biggest yet with 20+ launches. Coverage confirms Dots (always-on agents for Pro, Business Premium and Enterprise), ChatGPT Space, cloud Codex environments, Agents API computer use, and GPT-6.1 Sol as the headline model. Decrypt reports Ultrafast at up to 8x in Codex and 6x in the API, bundled with a new $500/month Pro 500 plan. The talk's "Is Codex dead?" opener reflects real community sentiment after Anthropic's Fable-class lead in mid-2026. Note also that OpenAI shelved a model release around DevDay over safety concerns, per Fast Company.

Separately (WorldofAI, same week), Codex capacity errors reportedly fell from a 6.89% daily-active-user peak to 0.085% after a Nov 6 retry/backoff fix. That was overload handling, not new compute.

## Real-World Application / Actionable Step
- **Measure the orchestrator-escalation pattern as a routing benchmark:** log which subtasks Sol-medium delegates to Astra vs Luna and score whether each escalation was needed. That gives free labeled data for a learned router.
- **Default your own agent runs to "high", not max,** and A/B one notch lower on every new model. Track tokens per solved task.
- **Use app-shot/accessibility-tree style context** for any GUI-driving eval harness instead of screenshots to cut vision-token spend.
- **Try a Codex Cloud environment with Tailscale** for long-running compression sweeps, so the laptop can close and the private GPU box stays reachable without public exposure.
