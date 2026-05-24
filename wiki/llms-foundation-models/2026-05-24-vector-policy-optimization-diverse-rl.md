# Vector Policy Optimization: Training for Diversity Improves Test-Time Search

**arXiv:** [2605.22817](https://arxiv.org/abs/2605.22817)
**Source:** Reddit r/MLScaling, surfaced 2026-05-23, ingested 2026-05-24
**Raw:** [`raw/reddit/2026-05-24-r-mlscaling.md`](../../raw/reddit/2026-05-24-r-mlscaling.md)

## TL;DR

Vector Policy Optimization (VPO) replaces the single scalar reward in policy gradient with a vector of multiple criteria and a stochastic weight assignment over those criteria during training. The bet is that training the policy under randomly-weighted multi-objective rewards forces the policy to retain diverse modes of behavior, which then pays off at test time when a search procedure (best-of-N, beam search, MCTS) can pick the mode that fits the specific test instance. The result on the table is a measurable lift on test-time search benchmarks over standard single-objective RL.

## Why this matters for the wiki

This sits in a cluster of recent papers (the 2026-04-17 AIMO-3 paper on inference-time scaling, the 2026-04-19 VGF paper on value-gradient flow with transport budgets) that all argue the same thing from different angles. Single-objective RL collapses the policy onto a narrow band of solutions. Test-time search needs diversity. Therefore: train for diversity, then search at test time.

VPO is the most direct framing yet of that thesis as an objective-function modification rather than a sampling trick.

## Method, briefly

- Reward is a vector of K criteria rather than a single scalar.
- During training, a random weight vector samples a convex combination over the K criteria each step.
- The policy gradient is computed against this stochastic objective.
- Equivalent to training under a family of related tasks at once, where the family is parameterized by the weight simplex.

## Empirical claim

VPO improves test-time search performance versus standard single-objective RL baselines on the evaluated benchmarks. Quantitative numbers are in the paper. The paper is recent (May 2026) and has not yet appeared on HF Daily Papers, so this surface is from the practitioner sub r/MLScaling rather than the popularity-ranked HF feed.

## Connections

- [VGF (2026-04-19)](2026-04-19-vgf-value-gradient-flow-rl.md): VGF asks "where should probability mass move" via transport budgets. VPO asks "how do we preserve diverse mass" via multi-objective training. Different layers of the same problem.
- [AIMO-3 (2026-04-17)](../inference-efficiency/2026-04-17-model-capability-dominates-inference-time.md) argued prompt-diversity alone cannot close the pass@N gap. VPO provides a policy-training-side answer to that critique: train the policy itself to be diverse rather than diversifying prompts at test time.
- Connects forward to today's [SCRL (2026-05-23)](2026-05-23-scrl-subproblem-curriculum-rlvr.md): SCRL solves credit assignment via subproblem decomposition; VPO solves diversity via objective vectorization. Both attack RLVR's coarse-signal problem from complementary angles.

## Open questions

- How is the criteria vector populated for tasks without obvious multi-axis evaluation (math, single-answer benchmarks)? Auto-decomposition of a scalar reward into a vector of correlated criteria is a research direction in itself.
- Does VPO compose with PRM-based step rewards (uPRM, supervised PRMs)? The vector-of-criteria framing is at the trajectory level; PRM is at the step level. Both could plug in simultaneously.

## Source

[arXiv 2605.22817](https://arxiv.org/abs/2605.22817). Surfaced via r/MLScaling on 2026-05-23 (Reddit score 5, but the sub is gwern-curated and treats new arxiv posts as practitioner-vetted signal).
