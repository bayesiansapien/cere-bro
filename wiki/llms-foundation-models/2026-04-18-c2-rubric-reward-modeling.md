# C2: Cooperative-Critical Rubric-Augmented Reward Modeling

**Date:** 2026-04-18  
**Tier:** 2 — LLMs / RLHF / Reward Modeling  
**arXiv:** [2604.13618](https://arxiv.org/abs/2604.13618)  
**Raw:** [source](../../raw/huggingface/2026-04-18-c2-scalable-rubric-augmented-reward-modeling-from-binary-pre.md)

## TL;DR

Rubric-augmented reward models are better than bare reward models — giving the model evaluation criteria (rubrics) before asking it to judge helps. But rubrics can backfire: a bad rubric misleads the reward model more than no rubric at all. C2 solves this with a cooperative-yet-critical design: a rubric generator trained from binary preferences, plus a critical verifier that accepts or rejects each rubric before acting on it. An 8B model matches the performance of one trained with rubrics from a 4× larger model.

## Mechanism

C2 trains two components:
1. **Cooperative rubric generator**: produces evaluation criteria using only binary preference supervision (no annotated rubrics needed). Trained with contrastive pairs: helpful rubrics (ones that pushed the reward model toward the correct preference) vs. misleading rubrics (ones that pushed it away).
2. **Critical verifier**: at inference, reads the proposed rubric and decides whether to use it or fall back to no-rubric judgment.

The key insight is that rubric quality is heterogeneous — and a bad rubric is worse than no rubric. Standard rubric-augmented RM papers assume rubrics are uniformly helpful. C2 explicitly models the adversarial case.

**Results:** +6.5 points on RM-Bench, +6.0 LC win-rate on AlpacaEval 2.0 vs. reasoning reward models on the same binary preferences.

## Connection to Broader RLHF Research

Reward model quality is the bottleneck for post-training. C2 is interesting because it extracts more signal from cheap binary preference labels (which scale) rather than requiring expensive rubric annotations. The cooperative-critical framing is essentially a self-checking mechanism: generate an intermediate reasoning step (rubric), then verify the reasoning before acting on it. This mirrors chain-of-thought-plus-verification patterns seen in math reasoning.

## Related Pages

- [RL for LLMs](rl-for-llms.md)
- [PreRL / DSRL: RL in Pretrain Space](2026-04-16-prerl-rl-in-pretrain-space.md)
