# What It Actually Takes to Build a Software Factory (Tereza Tížková, Factory)

**Channel:** AI Engineer
**Published:** 2026-09-27
**Source:** https://www.youtube.com/watch?v=vGCJ7diEtrw

## TL;DR
Factory defines a software factory as the whole autonomous SDLC loop (signals, prioritization, orchestration, execution, validation, iteration, learning), not a swarm of coding agents. Three pillars: **agnostic** (any model, any tool, bring your own subscription), **autonomous** (week-long "missions" with orchestrator → sequential workers → independent validators), and **always improving** (deferred tool loading, codebase readiness checks, plugins). The most relevant part for Amit is Factory's production LLM router: classify task difficulty, then pick the cheapest model predicted to clear the threshold, and escalate mid-task on failure.

## Key Takeaways
- **Why now:** AutoGPT/BabyAGI-era loops failed on hallucination, context length, reasoning quality, and lack of isolated environments. All four have improved enough.
- **Coinbase cost pattern (cited):** token usage kept rising while spend fell, through cheaper default models, caching, "no limits but show results," and routing.
- **Factory auto-routing, 4 steps:** (1) assign task, with per-role defaults and permissions (sales vs engineering); (2) **classify difficulty** from prompt structure, codebase, tools in use; (3) threshold on required capability; (4) **choose the cheapest model above threshold**. Escalate to a stronger model if the task fails. Also a reliability play: open models are faster and give provider failover.
- Claimed savings in the talk: "conservative" 25%, "probably more."
- **Caching is a pricing decision, not a technical moat.** Self-hosted open models get the same prefix-cache savings on dedicated compute.
- **Missions architecture:** orchestrator writes a **validation contract before any code**, workers run **in sequence, not in parallel** (fresh context per handoff, like a colleague reviewing), each worker can spawn parallel sub-agents, and validators judge code they did not write. A 16-hour customer mission spent **~40% of time on validation**.
- Two validator types: **scrutiny** (lint, types, tests, code structure) and **user-testing** (computer-use agent clicks through the real app). The second catches dummy UIs that "look done" in code.
- **Reward hacking is real:** a poorly specified "done" condition leads agents to pass tests rather than solve the task.
- **Deferred context engine:** progressive tool disclosure (short names and descriptions first, full schema on demand). Claimed 50%+ token savings at scale for enterprises with hundreds of tools.
- **Power-law adoption:** on unready codebases, AI degrades code and the damage compounds (cites Stanford data). The "agent readiness" checklist covers reproducible dev env, tests, docs, linters, and style.

## Architecture & Optimization Mechanics
- **Router design = difficulty classifier + cost-sorted capability threshold + fallback escalation.** This is the classic cascade/threshold router. The open problems she lists are exactly the research ones: misroute rate, escalation frequency, latency added by classification, and **cache invalidation on model switch** (switching mid-task loses the prefix cache on the old model, so escalation has a hidden prefill cost).
- **Difficulty features:** prompt structure, codebase size and complexity, tools invoked. That is a richer feature set than prompt-only routers such as RouteLLM.
- **Sequential workers beat parallel swarms** for coherence: context freshness at handoff acts as a regularizer against accumulated drift. Parallelism is pushed down to leaf sub-tasks.
- **Deferred tool loading** is context compression by lazy evaluation. The cost saving grows with tool count, since tool schemas otherwise sit in every prefill.
- **Validation at ~40% of wall-clock** is the real cost center of autonomous agents, and a target for cheaper validator models.

## Grounded Context (Web Enrichment)
Factory's own product page now claims its Router cuts cost by **over 50%** in production while holding frontier performance, well above the "conservative 25%" in the talk, so read the talk's number as a floor. Factory's Missions architecture writeup confirms the multi-model design: orchestrator, workers, validators, and research agents each use different models, with shared state in the validation contract, feature list, research notes, and knowledge base, and handoffs coordinated through git.

The Coinbase example is well documented. Brian Armstrong reported AI spend cut nearly in half while token usage kept growing. The levers: **cheaper defaults** (91% of employees never hit usage caps, so caps were pointless), making open-weight **GLM-5.2 and Kimi 2.7 the gateway defaults**, prompt-preprocessing routers that factor in cache hits and pricing, and raising **cache hit rate from 5% to 60%**. The 5% to 60% caching figure is probably the largest single contributor, which supports Tížková's "caching is pricing, not tech" point. Critics note legal and compliance risk in defaulting to Chinese open-weight models.

## Real-World Application / Actionable Step
- **Benchmark your router against Factory's recipe.** Implement "classify difficulty → cheapest model above threshold → escalate on failure" as a baseline, and measure (a) misroute rate, (b) escalation rate, and (c) cost including **lost prefix-cache on escalation**. Cache-aware routing (prefer staying on the model holding the warm cache) is an underexplored research angle.
- **Add codebase and tool features to the router's classifier**, not just prompt text. For agentic workloads the tool set and repo context are strong difficulty signals.
- **Make cache hit rate a routing objective.** Coinbase's jump from 5% to 60% hit rate rivals any model-selection gain. In vLLM, check prefix-caching hit rates on your serving traces and route to keep hot prefixes on the same replica.
- **Write validation contracts before launching agent runs** on compression experiments (target metrics, eval sets, forbidden shortcuts such as touching the eval data) to block reward hacking.
- **Try a cheaper validator model.** With validation at ~40% of mission time, test whether a small model can do scrutiny validation while the frontier model only does user-level validation.

Sources: [Factory Router](https://factory.ai/product/router), [How Missions Work](https://factory.ai/news/missions-architecture), [Developers Digest: Factory model routing](https://www.developersdigest.tech/blog/factory-ai-droid-model-routing-costs), [Brian Armstrong on X](https://x.com/brian_armstrong/status/2070670644577280109?lang=en), [Analytics India Mag: Coinbase](https://analyticsindiamag.com/ai-news/coinbase-cuts-ai-spend-by-half-with-open-weight-models-smarter-routing), [TechTimes: legal risk](https://www.techtimes.com/articles/319248/20260628/coinbase-cuts-ai-spend-50-chinese-models-legal-risk-its-ceo-didnt-lead.htm)
