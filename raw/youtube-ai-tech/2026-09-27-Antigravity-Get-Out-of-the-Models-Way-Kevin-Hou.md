# Get Out of the Model's Way (Kevin Hou, Google Antigravity)

**Channel:** AI Engineer
**Published:** 2026-09-27
**Source:** https://www.youtube.com/watch?v=buHC7bQE1X4

## TL;DR
Google's Antigravity lead argues that agent products must "scale with intelligence": every product primitive should get more useful as the model improves, and scaffolding that constrains the model should be removed. Antigravity 2.0 splits the agent manager from the IDE (the IDE becomes what the debugger was to the IDE) and bets on three 2026 primitives: dynamically generated sub-agents, sidecars (long-lived event listeners), and generative UI rendered on the fly by a ~900 tok/s Gemini Flash.

## Key Takeaways
- Primitive eras: 2022 autocomplete/chat (embeddings, AST, deterministic). 2024 agents (MCP, tools, permissions). 2025 agent managers (skills, hooks, artifacts). 2026 agent teams (sub-agents, sidecars, generative UI).
- Removing features users love is the hard part. Precedents: giving agents a terminal, and killing the chat sidebar in Windsurf for agent-only. Both paid off as models improved.
- `/teamwork` mode: a lead agent (Gemini 3.5 Flash) spawns a team of arbitrary size with specialized roles, and can pick a different model per sub-agent. This is model routing done by the orchestrator itself.
- OS kernel hero run: 93 sub-agents, 12 hours, 15,000 requests, 2B tokens, under $1,000, booted and played Doom. That implies roughly $0.50 per million tokens blended.
- Internal side-by-side eval workflow: agent computes control vs experiment deltas, a research agent proposes ~100 hypotheses, one sub-agent per hypothesis drills in parallel, results come back as an interactive generated UI. Claimed 90% automation of a notebook-heavy task.
- Sidecars: a plug-in protocol for long-lived processes that let the agent subscribe to SMS, webhooks, cron, GitHub PRs. Scheduled tasks already run on it.
- Generative UI thesis: human-written specialized UIs are "kind of dead" when a model can render a kanban or timeline in seconds.

## Architecture & Optimization Mechanics
- **Speed is the enabler.** Generative UI and hundred-agent fan-out only work because Flash runs at ~900 tok/s. Latency and cost per token, not peak capability, decide which product primitives are viable. This is the strongest argument for inference optimization as product strategy.
- **Orchestrator-as-router.** The lead agent choosing a model per sub-agent is learned routing embedded in the planner. The routing decision moves from a separate classifier into the orchestrating LLM's context.
- **Flash leading teams.** A cheap model acting as coordinator (not just worker) pushes the Pareto frontier: coordination is mostly decomposition and state tracking, which does not need Pro-tier capability.
- **Hypothesis fan-out for eval diffing** is a reusable pattern: diff, generate N explanations, verify each in parallel, aggregate.

## Grounded Context (Web Enrichment)
This talk is from the June World's Fair. Minor correction: Gemini 3.5 Flash launched May 19, 2026 at Google I/O, not April. It was the first Flash model to beat the prior Pro (Gemini 3.1 Pro) on coding and agentic tasks, which supports Hou's claim. Antigravity 2.0 shipped as five pieces: desktop app, IDE, Go CLI, SDK, and a Managed Agents API.

The agent-team bet has since produced real results. Google reports that Teamwork paired with Gemini 3.7 Flash solved seven open problems at FOCS/JMLR level, including Knuth's Cycles Conjecture (40+ and 70+ page proofs, the shorter one verified in Lean), and notably a result on **provable LLM quantization**, plus a cycle-accurate out-of-order RISC-V simulator booting xv6 at 0.71% cycle error. A "Boost Mode" for Gemini 3.8 Flash has also appeared. The "cheap fast model plus many agents that critique each other" thesis looks validated, though Google's own claims have not all been independently replicated.

## Real-World Application / Actionable Step
- **Read the provable-quantization result.** Find the Antigravity Teamwork paper/blog on the LLM quantization proof and check whether the bound is useful for your GPTQ-style work.
- **Try the hypothesis fan-out pattern on your compression ablations.** When a pruned or quantized model regresses on a slice, have an agent generate 50 to 100 hypotheses (layer sensitivity, outlier channels, specific token types) and dispatch one sub-agent per hypothesis. This replaces hours of notebook work.
- **Treat throughput as a routing feature.** In your router, include tokens/sec and time-to-first-token as first-class objectives, since agentic fan-out multiplies latency.
- **Evaluate a Flash-tier orchestrator.** Test whether a small model can coordinate while routing hard sub-tasks up to a larger model. That is the cost structure behind the $1,000 kernel run.

Sources: [Antigravity blog](https://antigravity.google/blog/gemini-3-5-flash-in-google-antigravity), [getaibook](https://getaibook.com/news/antigravity-20-decouples-agent-environments-with-gemini-35), [Google blog: Teamwork + Gemini 3.7 Flash](https://blog.google/innovation-and-ai/technology/developers-tools/antigravity-teamwork-multi-agent/), [OfficeChai](https://officechai.com/ai/google-says-antigravity-with-gemini-3-7-flash-solved-7-open-problems-including-knuths-cycles-conjecture/), [MindStudio Boost Mode](https://www.mindstudio.ai/blog/antigravity-boost-mode-gemini-3-8-flash)
