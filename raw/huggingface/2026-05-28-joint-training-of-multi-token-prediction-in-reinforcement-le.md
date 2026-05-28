---
source: farmer/huggingface
farmed: 2026-05-28T03:40:35Z
arxiv_id: 2605.28184
url: https://huggingface.co/papers/2605.28184
arxiv_url: https://arxiv.org/abs/2605.28184
date: 2026-05-28
---

# Joint Training of Multi-Token Prediction in Reinforcement Learning via Optimal Coefficient Calibration

Reinforcement Learning from Verifiable Rewards (RLVR) has emerged as the standard paradigm for improving reasoning capability of large language models, while Multi-Token Prediction (MTP) has been a widely adopted module in pretraining. Combining them is a natural approach, yet current RL practices detach MTP gradients because joint training degrades the performance. We revisit this failure from an optimization perspective. We show that the per-step effect of MTP on the RL objective can be decomposed into two terms: a first-order correlation and a second-order perturbation penalty. This decomposition unifies three MTP training regimes: Detach, Cross-Entropy loss, and Policy loss, and explains why each succeeds or fails. Further analysis of policy loss reveals that, although it aligns with intuition, performance still degrades: the correlation term decays while the quadratic penalty persists. Guided by the analysis, we propose Optimal Coefficient Calibration (OCC), an adaptive scheme that tracks the optimal coefficient online via a log-probability proxy at negligible cost. Across six competition-level mathematical reasoning benchmarks, OCC consistently matches or exceeds the detach baseline, delivering improved joint MTP-RL training performance.
