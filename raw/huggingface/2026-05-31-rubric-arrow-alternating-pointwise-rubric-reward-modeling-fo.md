---
source: farmer/huggingface
farmed: 2026-05-31T09:25:04Z
arxiv_id: 2605.29156
url: https://huggingface.co/papers/2605.29156
arxiv_url: https://arxiv.org/abs/2605.29156
date: 2026-05-31
---

# RUBRIC-ARROW: Alternating Pointwise Rubric Reward Modeling for LLM Post-training in Non-verifiable Domains

Pointwise reward modeling offers critical signals for LLM post-training, yet struggles with absolute scoring in subjective, non-verifiable settings. Rubric-based methods address this by decomposing evaluation into explicit criteria, but existing approaches typically depend on frontier LLMs and suffer from ties caused by hard Boolean aggregation. We present RUBRIC-ARROW, an alternating framework that jointly trains a rubric generator and a rubric-conditioned judge, with its RL stage using only pairwise preference data. Our method couples a probability-based scoring rule that reduces ties with phase-specific preference-based rewards and an alternating GRPO scheme that together train the pointwise evaluator. Extensive experiments show that RUBRIC-ARROW achieves competitive reward-modeling accuracy and yields consistent gains for downstream policy post-training.
