# Reinforcement Learning for LLMs

Using RL to improve LLM reasoning and alignment — from RLHF to RLVR (verifiable rewards) to newer approaches that optimize the pre-training distribution directly.

## Current State (as of 2026-04-16)

The RL era for LLMs is now firmly established. RLVR (RL with verifiable rewards) is the dominant paradigm for reasoning models. New work is pushing beyond the conditional distribution P(y|x) into pre-train space optimization.

## Key Papers

**PreRL / DSRL (2026-04-16)** — Applies RL directly to the marginal distribution P(y) rather than P(y|x), bypassing the ceiling imposed by the base model's output distribution. Negative Sample Reinforcement (NSR) prunes wrong reasoning paths and boosts reflection. DSRL combines PreRL + standard RL for best results. → [summary](2026-04-16-prerl-rl-in-pretrain-space.md)

**RationalRewards (2026-04-16)** — Reward models that produce explicit multi-dimensional critiques before scoring. Test-time Generate-Critique-Refine loop matches RL fine-tuning without parameter updates. → [summary](../multimodal/2026-04-16-rationalrewards-visual-generation.md)

## Key Concepts

- **RLHF**: RL from human feedback — aligns model outputs to human preferences
- **RLVR**: RL with verifiable rewards — uses ground-truth-checkable tasks (math, code) for reward signal
- **P(y|x) vs P(y)**: standard RL optimizes the conditional; PreRL optimizes the marginal, avoiding base model ceiling
- **Negative Sample Reinforcement**: learning from wrong outputs to prune incorrect reasoning subspaces

## Related Pages

- [Knowledge Distillation](../inference-efficiency/knowledge-distillation.md)
- [Open vs Closed Models Mid-2026](2026-04-16-open-vs-closed-models-mid-2026.md)
