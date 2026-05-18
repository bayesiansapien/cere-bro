---
source: farmer/huggingface
farmed: 2026-05-18T04:19:52Z
arxiv_id: 2605.15726
url: https://huggingface.co/papers/2605.15726
arxiv_url: https://arxiv.org/abs/2605.15726
date: 2026-05-18
---

# Nudging Beyond the Comfort Zone: Efficient Strategy-Guided Exploration for RLVR

Reinforcement learning with verifiable rewards (RLVR) has emerged as a scalable paradigm for improving the reasoning capabilities of large language models. However, its effectiveness is fundamentally limited by exploration: the policy can only improve on trajectories it has already sampled. While increasing the number of rollouts alleviates this issue, such brute-force scaling is computationally expensive, and existing approaches that modify the optimization objective provide limited control over what is explored. In this work, we propose NudgeRL, a framework for structured and diversity-driven exploration in RLVR. Our approach introduces Strategy Nudging, which conditions each rollout on lightweight, strategy-level contexts to induce diverse reasoning trajectories without relying on expensive oracle supervision. To effectively learn from such structured exploration, we further propose a unified objective, which decomposes the reward signal into inter- and intra-context components and incorporates a distillation objective to transfer discovered behaviors back to the base policy. Empirically, NudgeRL outperforms standard GRPO with up to 8x larger rollout budgets, while outperforming oracle-guided RL baseline on average across five challenging math benchmarks. These results demonstrate that structured, context-driven exploration can serve as an efficient and scalable alternative to both brute-force rollout scaling and feasibility-oriented methods based on privileged information.
