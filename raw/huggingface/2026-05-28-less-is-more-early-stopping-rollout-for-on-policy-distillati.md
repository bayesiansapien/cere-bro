---
source: farmer/huggingface
farmed: 2026-05-28T03:40:35Z
arxiv_id: 2605.27028
url: https://huggingface.co/papers/2605.27028
arxiv_url: https://arxiv.org/abs/2605.27028
date: 2026-05-28
---

# Less is More: Early Stopping Rollout for On-Policy Distillation

On-policy distillation has recently emerged as a promising alternative to standard sequence-level imitation, training a student by scoring its own rollouts with a teacher model. However, we observe ``Off-policy Teacher Decay'' problem in this paradigm: for the later tokens, with student's earlier trajectory as context that is off-policy to the teacher, the teacher's ability to produce a corrective score would decay, and may fall back to token-completion behavior learned in the pre-training stage. We empirically verify this problem, and we propose Early Stopping Rollout (ESR) to fix it: a simple yet effective distillation strategy that simply restricts the rollout generation to the first
  response tokens. We show that ESR both surpasses the full rollout OPD performance across model size, family, tasks and training regime, and exhibit much higher GPU efficiency and training stability, especially under cross model family scenarios. We further investigate the mechanism behind this surprising performance and discovered "Cascading Alignment" and "Sub-mode Commitment" effect of ESR that may explain why it works effectively and even sometimes exceeding the teacher model performance. Besides, we show that this position-based token selection strategy cannot be fully explainable by KL divergence and entropy signals.
