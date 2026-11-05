# Why AI Makes You 100x Faster but Not Your Company (Mitchell Troyanovsky, Basis)

**Channel:** AI Engineer
**Published:** 2026-11-04
**Source:** https://www.youtube.com/watch?v=JGtkTjn4120

## TL;DR
Individual developers get 10x to 100x from coding-style agents, but firms do not, because those agents push complexity onto the user (competency gap) and let each user improvise the process (process gap). Organizations scale non-deterministic workers through top-down process, not determinism. Basis argues production agents must be simple and reliable, which requires being opinionated about behavior. Those opinions become "behavior specs" that act as rubrics on trajectories with no ground truth, scaling eval signal far beyond outcome-based evals. Forking and cheap sub-agent "simulations" then debug where behavior diverged.

## Key Takeaways
- **Two gaps block enterprise gains:** (1) competency, where users must manage skills, memories and a theory of mind over the agent, which most knowledge workers cannot do; (2) process, where per-user customization contradicts how firms scale (process comes from leadership down).
- **Consistency beats brilliance.** The target is not perfection but doing things the same way every time, including failing the same way. Flashes of genius plus random basic misses read as unreliable.
- **Opinions resolve open choice.** "Read this PDF" has infinite strategies (VLM, OCR library, OCR vendor, OCR plus VLM check, N-way VLM voting). Unopinionated agents pick differently each time, so outcomes vary even when each method is fine.
- **Many opinions come from expertise, not evals:** read the primary source before answering a tax question, screenshot a generated PowerPoint before returning it. Opinions also trade off latency and cost, not just accuracy.
- **Context is runtime training data.** Behavior emerges from system prompt, progressive disclosure, tool descriptions and model training together, so "prompt" understates it. Care about every token.
- **Behavior specs:** a product spec for agent behavior, written before context edits, listing only the most important opinions (e.g. "on a bank reconciliation mismatch, explain the difference, never post a plug entry"). Used both to align the team and as an LLM-judged rubric: was the behavior relevant in this trajectory, and was it exhibited?
- **Process supervision scales; outcome evals don't.** Long-horizon trajectories have combinatorially many decision points and no ground truth. Checking behaviors gives far more signal per trajectory and a proxy for whether evals generalize to production.
- **Forking:** clone a failed trajectory just before the divergent decision, ask the agent why, or edit context and replay. Hard to build in the cloud (requires recreating DB and environment state) but turns a failed outcome into a localized cause.
- **Simulations:** have a coding agent spawn a sub-agent with the production system prompt and skills, told not to cheat, and probe what it would do in the scenario. Cruder than forking but nearly free. Troyanovsky used it for 18+ months before building forking.
- **Trust is earned like a coworker's.** Review depth scales with blast radius times perceived competence. Narrow, reliable agents earn wider scope. Nobody wants a "Move 37" on their tax return.

## Architecture & Optimization Mechanics
- **Behavior-spec judging = process reward modeling at the harness level.** Each spec item is a conditional predicate (relevance, then compliance) evaluated over the trajectory, giving dense supervision on unlabelled production traces.
- **Forking needs deterministic environment snapshots** (DB state, tool state, rendered context) at each step. This is checkpoint and restore for agents, analogous to KV-cache or state checkpointing for replay.
- **Simulation is a cheap surrogate model of the agent.** It trades fidelity for iteration speed, the same trade as using a small proxy model to tune hyperparameters before the full run.
- **Opinionated pipelines reduce variance,** which is what makes cheaper models viable: fixing the method (e.g. OCR then VLM verify) removes the planning burden that otherwise requires a frontier model.

## Grounded Context (Web Enrichment)
Basis is credible on this topic. It raised a $100M Series B in February 2026 at a $1.15B valuation (Khosla, Accel, NFDG among backers), builds long-horizon accounting agents on OpenAI models that run for hours or days, and reports use at about 30% of the top 25 US accounting firms. The "100x for me, not for the company" framing matches the macro data. An NBER working paper (March 2026) surveying nearly 6,000 executives across the US, UK, Germany and Australia found about 90% reporting no measurable AI impact on productivity or employment over three years, with realized gains around 0.29% vs an expected 1.4% over the next three, reviving the Solow paradox. An Atlanta Fed survey found gains concentrated in high-skill services and finance, which is exactly Basis's market.

The talk's weak point is the "100x" personal figure, which is anecdotal and unmeasured. The organizational explanation (process and competency gaps) is plausible but competes with others in the literature, notably the revenue-recognition lag the NBER authors favor and the cost of complementary investments. Behavior-spec rubrics also inherit every LLM-judge weakness (leniency, low discrimination) that NatWest documented at the same conference. Their signal is only as good as judge calibration.

## Real-World Application / Actionable Step
- **Write behavior specs for your routing and compression evals.** Beyond accuracy, define 5 to 10 behaviors a compressed or routed model must preserve (cites source before answering, verifies tool output, refuses rather than guesses). Score trajectories for them. Compression often breaks process behaviors before it breaks final-answer accuracy.
- **Use behavior-consistency as a routing signal.** A cheap model that consistently follows an opinionated pipeline can be routed to more often than one with higher peak quality but erratic process.
- **Try the simulation trick now:** when a routed or quantized model misbehaves, spawn a sub-agent with the exact production context to reproduce and test context fixes before running expensive full replays.
- **Calibrate the behavior judge** against a small human-labelled set (rank correlation, not MAE) before trusting its scores at scale.
