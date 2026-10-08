---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2609.13730
url: https://huggingface.co/papers/2609.13730
arxiv_url: https://arxiv.org/abs/2609.13730
date: 2026-10-07
---

# JumpStart Your Policy Learning with Lessons from 160,000 Training Runs

Reliable progress in offline policy learning depends on careful reporting, well-tuned baselines, and evaluation across diverse conditions. Prior work has shown that results can be sensitive to reporting choices, hyperparameter tuning, and dataset properties, but these sources of variability have not been systematically investigated together at the scale needed to understand how they shape conclusions. To address this gap, we present a large-scale empirical study of offline reinforcement and imitation learning, training over 160,000 policies across 114 datasets. At this scale, no algorithm dominates: aggregate performance among the strongest methods is often close, but the leaders differ substantially across environments. We find that proper hyperparameter tuning frequently reshuffles perceived algorithm rankings and that benchmark composition can produce conflicting conclusions. We also study hyperparameter sensitivity and transfer across environments, identifying a simple strategy for deriving strong default configurations. We use our findings to develop a dataset-conditioned recommender that provides task-specific algorithm recommendations for practitioners. Finally, we release JumpStart: a resource suite containing every trained policy, per-model scores and hyperparameters, strong baselines across all environments, training and evaluation code, and an extensible website for retrieving, analyzing, and contributing results. Together, these resources aim to make offline policy-learning research more reliable and enable future work beyond the scope of this study.
