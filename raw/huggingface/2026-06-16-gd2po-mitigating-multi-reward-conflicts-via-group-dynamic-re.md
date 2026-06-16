---
source: farmer/huggingface
farmed: 2026-06-16T00:00:00Z
arxiv_id: 2606.16771
url: https://huggingface.co/papers/2606.16771
arxiv_url: https://arxiv.org/abs/2606.16771
date: 2026-06-16
---

# GD^2PO: Mitigating Multi-Reward Conflicts via Group-Dynamic reward-Decoupled Policy Optimization

As LLMs advance, post-training reinforcement learning (RL) increasingly relies on multi-dimensional rewards to cultivate comprehensive capabilities. This shift demands new algorithms capable of optimizing diverse and potentially competing objectives simultaneously. To address this, existing methods such as Group reward-Decoupled Policy Optimization (GDPO) decompose the overall score into independent reward groups, then compute the RL loss separately within each group. However, this strategy still encounters multi-reward conflicts: a single rollout can yield positive advantages on certain reward dimensions but negative ones on others, causing opposing signals to cancel each other out during aggregation, further hindering RL training efficiency. Inspired by Dynamic sAmpling Policy Optimization (DAPO), which improves RL training efficiency by filtering out ineffective rollouts with near-zero advantages, we propose Group-Dynamic reward-Decoupled Policy Optimization (GD^2PO). Specifically, GD^2PO employs a conflict-aware filtering mechanism to mask out rollouts suffering from severe reward-wise disagreement. By preventing conflicting signals from canceling each other out, this masking strategy preserves and enhances the magnitude of effective RL advantages, thereby significantly accelerating learning efficiency. Furthermore, we introduce query-level reweighting to dynamically adjust the update intensity of each query based on its overall reward consensus. Experiments on various multi-reward scenarios, including tool calling and human preference alignment, demonstrate that GD^2PO consistently and significantly outperforms existing baselines. The code is available at https://github.com/Qwen-Applications/GD2PO.
