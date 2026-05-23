# SR²AM: Efficient Agentic Reasoning Through Self-Regulated Simulative Planning

**Source:** HuggingFace daily papers, 2026-05-23.
**arxiv:** [2605.22138](https://arxiv.org/abs/2605.22138)

## TL;DR

Reactive agents trained end-to-end with adaptive chain-of-thought tend to over-think: reasoning length explodes without reliable accuracy gains because the model has no control over whether, when, or how deeply to plan. SR²AM (Self-Regulated Simulative Reasoning Agentic LLM) decomposes agent decision-making into three systems: System I (reactive execution of fine-grained actions), System II (simulative reasoning grounded in future-state prediction via a world model), and System III (self-regulation, a learned configurator that decides when and how deeply to plan). Across math, science, tabular analysis, and web search, v0.1-8B and v1.0-30B match Pass@1 of 120-355B and 685B-1T parameter systems respectively, while v1.0-30B uses 25.8-95.3% fewer reasoning tokens than comparable agentic LLMs. RL increases average planning horizon by 22.8% while planning frequency only grows 2.0% — the model learns to plan *further ahead* rather than *more often*.

## What this paper actually proposes

The three-system decomposition is a clean operationalization of the dual-process / control-hierarchy idea that has been informally circulating since GPT-4. Most prior agentic work conflates planning and execution into a single chain-of-thought, then tries to control reasoning depth via heuristics (max-tokens cap, "think harder" prompts, reward shaping). SR²AM separates them: a configurator decides how much planning to allocate to each step, the planner simulates with an LLM world model, the executor acts.

The 25.8-95.3% reduction in reasoning tokens at matched accuracy is the practical claim. The structural claim — that learned self-regulation extends beyond planning to "how agents govern their own learning and adaptation" — is a research-program statement worth holding the field to.

## Connections to prior wiki state

This is the most direct reply to a tension that has been building in agent research since [the May Worth Watching prediction that token economics will become the binding constraint on agent deployment](../daily-digest/2026-05/) (Microsoft canceling internal Claude Code licenses this week is the strongest evidence yet that the constraint is now real). SR²AM gives a concrete answer: don't reduce model size, reduce planning frequency. A 30B model that uses 50% fewer tokens than its competitors at matched accuracy has the same effect on unit economics as a 2x model compression — but with no quality loss.

The "RL learns to plan further ahead, not more often" finding is also notable in light of [Karpathy's Autoresearch (last-week roundup from Ken Huang's compound-engineering taxonomy)](../) and the broader observation that autonomous research / agentic systems benefit more from longer-horizon single plans than from many short plans. The empirical signal here lines up.

## Gaps

The world model is the same LLM as the executor. The paper does not explore whether a smaller, faster world model would suffice (separating the simulator from the executor is the obvious extension). The configurator's decisions — when to plan, how deep — are learned end-to-end but not interpretable. We don't see an analysis of what triggers the configurator to plan deeper.

Also: math, science, tabular, web search are all task families where a structured plan helps. Whether SR²AM helps on tasks with high ambient noise (open-ended dialogue, creative writing) is unaddressed.

## Research angle

The strongest open question is whether the configurator generalizes across task families. If the same configurator learned on math + web search makes good planning-allocation decisions on software engineering or biomedical literature search, then SR²AM is the start of a general-purpose self-regulation layer. If not, every domain needs its own configurator and the architecture is closer to a sophisticated multi-skill MoE.

For routing: SR²AM is a *temporal* router (when and how much to think) where [Maestro (today's paper)](../ai-routing/2026-05-23-maestro-rl-orchestrated-model-skill-ensemble.md) is a *resource* router (which expert to call). The two systems are orthogonal and likely compose. A combined SR²AM + Maestro system would route both *when* and *to whom*.

## Raw source

[raw/huggingface/2026-05-23-efficient-agentic-reasoning-through-self-regulated-simulativ.md](../../raw/huggingface/2026-05-23-efficient-agentic-reasoning-through-self-regulated-simulativ.md)
