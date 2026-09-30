# Orchestras, Not Factories: How the Fastest Builders Work (Charlie Holtz, Conductor)

**Channel:** AI Engineer
**Published:** 2026-09-27
**Source:** https://www.youtube.com/watch?v=TRfzFJCJ7ZE

## TL;DR
Conductor's CEO distills what he has seen the fastest agent-driven engineers do into six principles (acronym "STICKFO"): stay near (not at) the frontier, don't try to beat the market on workflow tuning, keep strict human-reviewed "slop-free zones," centralize all org context in a database for agents, give agents persistent cloud sandboxes, and treat the human as a conductor of an orchestra rather than a factory line manager. The talk doubles as the launch of Conductor's multiplayer cloud workspaces.

## Key Takeaways
- **Stay near the frontier.** Try new workflows the day they ship; relying on your social graph leaves you 3 to 6 months behind. Conductor itself came from over-using Claude Code (5 repo clones, then worktrees).
- **Don't beat the market.** An efficient-market heuristic: ask "why isn't this workflow the default?" If it works for everyone (e.g. Ralph loops), wait for Anthropic or OpenAI to build it into the harness. Only invest in workflow where you have real alpha, meaning codebase or user knowledge the model lacks.
- **Slop-free zones.** Parts of the codebase require strict human review, enforced in CI (any migrations change needs a human). Docs, CLAUDE.md, skills, and Slack are treated as human-only. They rewrote the app a couple of times before adopting this.
- **CLAUDE.md is the most leveraged text you write.** It is what you would whisper to an intern every morning. Top builders spend unusual time on it.
- **Feed the beast.** An internal agent ("CIA") ingests every Slack message, Discord bug report, and recorded meeting into Postgres. Give the agent a SQL tool and let it handle the rest.
- **Free-range agents.** Persistent cloud sandboxes that survive laptop close, can spawn more agents via API, and can be triggered from Telegram, Slack, or phone.
- **Orchestras, not factories.** "Feature factories" failed a decade ago. The human should stay at the center, zooming in and out, not pushing buttons on a line.

## Architecture & Optimization Mechanics
- **Efficient-market heuristic for tooling investment** is the most transferable idea. Frontier labs absorb generic workflow improvements into default harnesses within months. Custom work only pays where you have private information.
- **Selective review as a quality/cost router.** Slop-free zones are a routing policy for human attention: high-blast-radius files (migrations, agent instructions) get expensive review, the rest gets cheap or no review.
- **Everything-in-SQL context.** One queryable store beats many bespoke MCP integrations for small teams. It is the same conclusion WorkOS reached with its MCP gateway.
- **Worktree to cloud sandbox** migration (built on Vercel Sandbox) moves agent runtime off local hardware, enabling longer runs and multiplayer.

## Grounded Context (Web Enrichment)
The launch is confirmed. Conductor (YC S24) shipped multiplayer cloud workspaces built on Vercel Sandbox, replacing local Git worktrees as the substrate for every task. Users can bring their own model subscriptions, see teammates' agents live, co-steer a session, hand off a session with one keystroke, and manage it from iPhone or API. In a separate YC podcast, Holtz pushed the thesis further, calling code "sawdust" and the prompt the real asset. That fits his emphasis on CLAUDE.md and skills as the durable artifact.

The anti-factory framing is mostly a positioning argument against the other talks at this event (Warp, Factory, WorkOS). The "don't beat the market" heuristic is the strongest idea and holds up: features like worktrees, loops, and sub-agents did get absorbed into default harnesses (Claude Code, Codex, Antigravity) within months of going viral.

## Real-World Application / Actionable Step
- **Declare slop-free zones in your research repos.** Enforce human review in CI on eval harness code, benchmark configs, and quantization kernels, since a silent bug there corrupts every downstream result. Let agents roam freely in plotting and sweep scripts.
- **Apply "don't beat the market" to your tooling time.** Stop hand-building generic agent loops. Spend that time encoding your private alpha (layer-sensitivity priors, known outlier-channel behavior, hardware quirks) into CLAUDE.md and skills.
- **Dump experiment logs into one SQL store.** Give your agent a single query tool over runs, configs, and metrics instead of scraping W&B pages.

Sources: [Vercel customer story](https://vercel.com/customers/how-conductor-moved-parallel-coding-agents-from-the-laptop-to-the-cloud-with-vercel-sandbox), [Mastra Podcast](https://mastra.ai/podcasts/multiplayer-coding-agents-in-the-cloud-charlie-holtz-conductor), [BigGo: Orchestras, Not Factories](https://finance.biggo.com/news/0ee50e95347f903d), [BigGo: Code is sawdust](https://finance.biggo.com/news/fe599900ba5c87ae), [YC: Conductor](https://ycombinator.com/companies/conductor)
