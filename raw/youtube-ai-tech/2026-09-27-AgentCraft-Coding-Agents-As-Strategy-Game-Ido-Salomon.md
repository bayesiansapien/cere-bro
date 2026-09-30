# I Turned Coding Agents Into a Strategy Game (Ido Salomon, AgentCraft)

**Channel:** AI Engineer
**Published:** 2026-09-27
**Source:** https://www.youtube.com/watch?v=YIVkERhy8xo

## TL;DR
The human, not the model, is now the bottleneck in multi-agent coding: steering, reviewing, and context-switching across many agents burns people out. Ido Salomon (creator of MCP-UI, now MCP Apps) argues that RTS games already solved "supervise many asynchronous units," and built AgentCraft, a Warcraft-style orchestrator where Claude Code, Codex, and OpenCode agents are units, the file system is terrain, and spacebar jumps to whichever agent needs attention.

## Key Takeaways
- Four layers to raise the ceiling: **visibility** (status panel, file-system map, heat maps of agent activity), **attention routing** (spacebar-to-next-blocker), **autonomy** (auto-generated "quests," orchestrator breakdown in isolated containers, background loops), and **review** (diffs plus video/screenshot evidence, parallel implementations with pick-the-best).
- Review, not generation, is the scaling wall. Even 5 parallel outputs are hard to review. Visual evidence and best-of-N selection are his mitigations.
- Collaboration: shared "war rooms" where humans and agents see each other's work, hand off, or fork, without being bound to Git. Works over tunnels, mobile, Telegram.
- Unexpected finding: the gamified UI pulls in non-developers (kids, gamers). "Lower the floor" matters as much as "raise the ceiling."
- Next experiment ("Loopers"): a mobile-game-level abstraction that hides file granularity and relies on autonomous loops.
- Install: `npx @idosal/agentcraft`.

## Architecture & Optimization Mechanics
- No model-level content. The relevant mechanism is **human attention as the scarce resource** in an agent system. The spacebar "next thing that needs me" queue is a priority scheduler over human review, analogous to routing queries to the cheapest capable resource.
- Best-of-N parallel implementations with human selection trades compute for review time. This is cheap when inference is cheap, which ties agent UX directly to inference cost.
- Heat maps of file touches are a cheap observability signal for detecting agent conflicts and thrashing.

## Grounded Context (Web Enrichment)
AgentCraft is real and shipped: it is on npm as `@idosal/agentcraft`, has a site at getagentcraft.com, and supports Claude Code, OpenCode, and Cursor. Salomon gave an earlier version of the talk ("Putting the Orc in Agent Orchestration") at GitNation. The broader claim that humans are the bottleneck is consistent with every other talk in this AI Engineer batch (Antigravity's agent manager, Conductor, Warp, Factory), which all converge on orchestration UIs and review tooling.

The weak spot is evidence. The talk offers anecdotes (kids, a Starcraft dropout) rather than any measurement of throughput or review quality. Gamification can raise engagement while also encouraging rubber-stamping of agent output. Nothing here shows review quality holds as agent count rises.

## Real-World Application / Actionable Step
- **Adopt the "attention queue" idea for experiment management.** If you run many parallel pruning or quantization sweeps via agents, route only blocked or anomalous runs to yourself. A single "next thing needing me" view beats polling dashboards.
- **Require visual or metric evidence in agent PRs.** For compression work, have agents attach a before/after perplexity, latency, and memory table to every change so review takes seconds.
- Low priority to install. Try it only if you already run 5+ concurrent coding agents.

Sources: [getagentcraft.com](https://www.getagentcraft.com/), [npm @idosal/agentcraft](https://www.npmjs.com/package/@idosal/agentcraft), [GitNation talk](https://gitnation.com/contents/agentcraft-putting-the-orc-in-agent-orchestration), [StartupHub.ai](https://www.startuphub.ai/ai-news/artificial-intelligence/2026/agentcraft-gaming-the-ai-agent-workflow)
