---
source: farmer/huggingface
farmed: 2026-09-10T08:36:11.637058+00:00
arxiv_id: 2609.08650
url: https://huggingface.co/papers/2609.08650
arxiv_url: https://arxiv.org/abs/2609.08650
upvotes: 0
date: 2026-09-10
---

# Difficulty-Adaptive Tree-Structured Policy Optimization for Expanding Reasoning Coverage in RLVR

Reinforcement Learning with Verifiable Rewards (RLVR) has been central to the recent success of Large Reasoning Models. However, while RLVR significantly improves single-sample accuracy, it often fails to expand the model's intrinsic reasoning coverage (pass@k) due to limited exploration during training. To address this, we optimize the structural design of train-time rollouts to enhance pass@k. Our analysis identifies three key design principles: (1) difficulty-adaptive rollout can play an important role in expanding pass@k, beyond serving as an efficiency heuristic; (2) tree-based rollout outperforms parallel sampling in discovering correct answers; and (3) sentence-entropy-guided forking overcomes the localization phenomenon of token-level branching to maximize semantic diversity. Building on these insights, we propose DATPO (Difficulty-Adaptive Sentence-entropy-guided Tree-structured Policy Optimization). DATPO integrates difficulty-adaptive tree search with a sibling-diversity advantage term, explicitly promoting semantic diversity to expand reasoning coverage during training. Experiments on mathematical reasoning benchmarks demonstrate that DATPO outperforms baselines especially in pass@k, which directly translates to superior test-time scaling performance.
