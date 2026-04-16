---
date: 2026-04-16
source: huggingface
arxiv: 2604.14142
---

# From P(y|x) to P(y): Reinforcement Learning in Pre-train Space

**TL;DR:** PreRL applies reward-driven RL directly to the marginal distribution P(y) (pre-train space) rather than the conditional P(y|x), bypassing the bounded output distribution of the base model. Negative Sample Reinforcement (NSR) rapidly prunes wrong reasoning paths and boosts reflective behaviors. Combined with standard RL via Dual Space RL (DSRL), it outperforms strong baselines.

## Key Findings

- **Core bottleneck of RLVR**: optimizing P(y|x) is bounded by what the base model already outputs. Pre-train space optimization has no such ceiling.
- Strong **gradient alignment** between log P(y) and log P(y|x) — PreRL is a theoretically valid surrogate for standard RL.
- **Negative Sample Reinforcement (NSR)**: training on wrong examples prunes incorrect reasoning subspaces; increases reflection thoughts by 6.54× and transition thoughts by 14.89×.
- **DSRL (Dual Space RL)**: initialize with NSR-PreRL to expand the reasoning horizon, then transition to standard RL for fine-grained optimization. Consistently outperforms strong baselines.

## Related Pages

- [Reinforcement Learning for LLMs](rl-for-llms.md)
- [../inference-efficiency/knowledge-distillation.md](../inference-efficiency/knowledge-distillation.md)

**Raw source:** [../../raw/huggingface/2026-04-16-from-pyx-to-py-investigating-reinforcement-learning-in-pre-t.md](../../raw/huggingface/2026-04-16-from-pyx-to-py-investigating-reinforcement-learning-in-pre-t.md)
