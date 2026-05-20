# BetaPRM: Process Rewards with Learned Reliability

**Source:** HuggingFace Daily Papers 2026-05-20 · [arXiv 2605.15529](https://arxiv.org/abs/2605.15529) · [raw](../../raw/huggingface/2026-05-20-process-rewards-with-learned-reliability.md)

## TL;DR

Process Reward Models (PRMs) give step-level feedback for reasoning but currently output a single point score per step. Downstream methods treat these imperfect predictions as reliable signals, with no indication of when to trust them. BetaPRM predicts both a step-level success probability and the reliability of that prediction. Given step-success supervision from Monte Carlo continuations, it learns a Beta belief that explains the observed successful-continuation count through a Beta-Binomial likelihood, instead of regressing to the finite-sample success ratio as a point target. The learned reliability signal tells downstream applications when a step reward is trustworthy. Adaptive Computation Allocation (ACA) for PRM-guided Best-of-N uses this signal to stop when a high-reward solution is reliable and spend more computation on uncertain candidate prefixes. Across four backbones and four reasoning benchmarks, BetaPRM improves PRM-guided Best-of-N selection while preserving standard step-level error detection. ACA improves the accuracy-token tradeoff over fixed-budget Best-of-16, cutting token usage by up to 33.57% while improving final-answer accuracy.

## Why it matters

The reliability dimension has been missing from PRM design. Treating a noisy point estimate as a hard signal explains a lot of empirical PRM brittleness. The Beta-Binomial parameterization is the right choice for finite-sample count data and gives calibrated uncertainty without extra labeling.

## Connections

- **CEPO (today)** sharpens token-level credit via contrastive evidence. BetaPRM sharpens step-level credit via calibrated uncertainty. Two layers of the same problem (which signal can be trusted, where).
- **PUMA (2026-05-19)** uses reasoning-level redundancy to decide when to stop. ACA on top of BetaPRM uses step-level reliability to decide whether to spend more compute. Stack: reliability decides compute, redundancy decides termination.
