# Smarter Models Killed the Harness. Here's What's Left (Jediah Katz, SpaceXAI)

**Channel:** AI Engineer
**Published:** 2026-10-19
**Source:** https://www.youtube.com/watch?v=7Y4sbZgBdnc
**Domains:** ai-tech

## TL;DR
Katz, the longest-tenured Cursor harness engineer now at SpaceXAI after the acquisition, concedes the core claim of the "harness is dead" crowd: a fancy harness no longer adds coding intelligence, because the data flywheel (harness unlocks harder tasks, users generate data, labs train it in) makes the model absorb the tricks. What survives is everything the model cannot absorb: cloud runtime for day-long tasks, scoped permissions and spend guardrails, and cost efficiency. The same studies that show harness choice does not move eval scores show it moves cost per task significantly. The harness also opens each new frontier (Grok Bot's non-coding knowledge work, the "software factory"), where the guardrails and prompts are being added back in.

## Key Takeaways
- Title evolution: prompt engineer (2023) to context engineer (mid-2025) to harness engineer (2026). The harness is "eyes and hands" for the model: a runtime layer (where the loop runs, how state persists) and a context/orchestration layer (which model is called when, with what context, plus memory compaction and behavioral tricks).
- Peak harness was Cursor's Grind Swarm, a multi-agent, multi-machine harness that built a browser from scratch and took Cursor down once or twice.
- Cursor removed the small apply-edit model, codebase exploration instructions, and check-your-work prompts as frontier models absorbed those skills. Anthropic cut much of Claude Code's system prompt.
- Two studies cited: a UC Berkeley comparison of seven frontier models across Pi, Codex, and Claude Code harnesses on SWE-bench Lite, and an Apple study on MLE-bench. Both found harness choice did not significantly change scores, but both found significant differences in cost per task.
- The data flywheel: harness unlocks task, users attempt it, data flows to labs, model absorbs skill, harness deletes the scaffolding, and then the harness opens the next frontier.
- Grok Bot (coordinator bot orchestrating worker agents, like a lawyer with paralegals) is adding prompting and guardrails back for slide decks, travel booking, communication cadence, act-vs-ask decisions, and memory. None of these are new tasks, but the model has not nailed them in the general knowledge-work domain.
- Non-absorbable parts: cloud runtime (laptops sleep, tasks now run for days), trust and security (scoped permissions, no 10,000 dollar surprise API bills), and efficiency (cache hit rate, token efficiency, model mix).
- Prediction: within 6 months, 90 percent of agent work runs off the laptop. The product is once again moving faster than the model, so harnesses will get messier before cleaner.
- Engineering patterns: expose less of the harness to users (Hyrum's Law makes exposed internals impossible to change), design composable primitives (a single "subscriptions" tool for Slack, CI, and time-based wakeups), and track every deterministic "shim" centrally so a bot can open a PR to delete it when it stops firing.
- Abstraction is rising: yesterday's harness composed LLM calls, today's composes agents.

## Architecture & Optimization Mechanics
- **Cost is the surviving harness differentiator.** Katz spent a month on Grok Bot efficiency: cache hit rate, token efficiency, and model mix, with no quality loss. That is exactly the routing and prefix-caching problem. The harness owns the decision of which model handles each sub-task and how much context it sees, and that decision now dominates economics rather than accuracy.
- **Shim tracking is model-upgrade-aware technical debt.** Every behavioral patch is logged on use. When a new checkpoint stops triggering a shim, an agent proposes deleting it. This is a clean way to keep a routing or prompt layer from accreting dead heuristics across model generations.
- **Memory compaction and context control** live in the harness and are not absorbed by the model. Compaction policy directly sets KV-cache footprint and prefix-cache reuse.
- **Primitives over integrations** reduce tool-schema tokens in context. One subscription tool instead of N event integrations is a direct context-length and cache-stability win.
- **Coordinator plus workers** is a hierarchical routing topology: an expensive model owns strategy and a cheaper fleet executes. Model mix at that boundary is where the cost savings came from.

## Grounded Context (Web Enrichment)
The Apple study is real and matches the talk. "How Much of a Harness Does a Strong Agent Need for Autonomous ML Engineering?" (Hernández-Cano, Brilliantov, Abbé; arXiv, September 30, 2026) found that under equal time budgets and the same frontier backbone, open-source MLE harnesses gave no advantage over a minimal single-session agent with only read, write, and bash tools. The minimal agent, Malena, hit a 62.5 percent any-medal rate on MLE-bench versus 47.1 percent for the strongest external harness, and extra multi-agent or autonomy mechanisms added nothing once the agent had direct environment access. The Berkeley seven-model SWE-bench Lite study could not be located by title. The closest public work is DeepSWE (arXiv 2607.07946), which ran three models under a standardized harness versus vendor-native harnesses on SWE-Bench Pro and found no statistically significant score differences at comparable token cost, and "Same model, different harness" (arXiv 2608.26218). Treat the "seven models" detail as unverified, but the direction of the evidence is consistent.

Context on the acquisition: SpaceX signed to acquire Anysphere (Cursor) in June 2026 in an all-stock deal valued around 60 billion dollars, growing out of an April option agreement. The deal closed in mid-August 2026 and Cursor's team now works on Grok, Grok Build, Grok Bot, and the Grok API under SpaceXAI. Grok Bot launched around August 11 as an enterprise "AI colleague" that logs into your tools. Separately, a Berkeley RDI result from early 2026 showed agent benchmark harnesses are trivially exploitable by the agents they measure, which weakens any eval-score comparison across harnesses and strengthens Katz's argument that cost, not score, is the metric that still discriminates.

## Real-World Application / Actionable Step
- **Reframe routing work as harness efficiency.** The public evidence now says harness design does not move accuracy for frontier models but does move cost per task significantly. Any routing or model-mix result should be reported as cost per task at matched quality, which is the number harness teams are optimizing.
- **Adopt shim tracking** in any prompt or routing layer: log every heuristic trigger, and review for deletion on each model upgrade. Dead heuristics cost tokens and hide regressions.
- **Prioritize prefix-cache stability.** Katz's three levers were cache hit rate, token efficiency, and model mix. Stable system prompts, primitives instead of many tool schemas, and compaction that preserves prefixes are the concrete moves.
- **Experiment idea:** replicate the Apple minimal-harness result on an internal coding task set with a cheap model and a frontier model. If the harness still helps the cheap model, that gap is a routing opportunity: use the scaffolded cheap model where it matches the bare frontier model.
