---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.37868
url: https://huggingface.co/papers/2609.37868
arxiv_url: https://arxiv.org/abs/2609.37868
date: 2026-09-30
---

# Learning Beyond What You Sample: Off-Policy-Aware Cross-Model Trajectory Exchange for RLVR

Reinforcement Learning with Verifiable Rewards (RLVR) methods such as GRPO rely on successful self-generated trajectories, but finite rollout budgets can produce all-fail groups with no reward-based policy-gradient signal. While additional rollouts improve the chance of success at higher cost, successful trajectories missing from one model's rollouts may already have been discovered by another. Indeed, we observe that heterogeneous models often succeed on complementary prompts, creating opportunities for mutual learning without a designated stronger teacher. To exploit this complementarity, we propose GRAFT (Gated Replacement of Answer-Failed groups with peer Trajectories), an off-policy-aware framework that replaces all-fail groups with informative peer groups. GRAFT transfers both successful and unsuccessful peer responses with peer-computed advantages, while controlling cross-model mismatch through sequence-level compatibility weighting and token-level importance ratio clipping. Across three heterogeneous model pairs and five mathematical reasoning benchmarks, GRAFT consistently improves both models over GRPO with the same per-model rollout budget, gaining 2.1 points on average and up to 4.5 points in model-level average performance. Stored peer trajectories preserve most of the gains, improving over GRPO by 1.8 points on average without simultaneous co-training.
