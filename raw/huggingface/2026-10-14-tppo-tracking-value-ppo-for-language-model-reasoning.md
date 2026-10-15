---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.501015+00:00
arxiv_id: 2610.16794
url: https://huggingface.co/papers/2610.16794
arxiv_url: https://arxiv.org/abs/2610.16794
date: 2026-10-14
---

# TPPO: Tracking-Value PPO For Language Model Reasoning

Proximal Policy Optimization (PPO) is widely used in reinforcement learning with verifiable rewards for language-model reasoning. While value evolution along trajectory characterizes relative token-level credit, yet standard critics often fail to track it under sparse terminal rewards. To model this evolution, we analyze the relation between successive prefix values and show that they admit a Bayesian decomposition with additive updates in log-odds space. We use this additive structure to construct Tracking-Value PPO (\method), a cumulative value parameterization that sums position-wise scalar outputs into value logits. These outputs are learned through terminal-outcome supervision on the reconstructed values. \method improves aggregate mathematical reasoning scores over PPO by 7.0 and 8.4 points on Qwen3-4B-Base and Qwen3-8B-Base, respectively, while improving out-of-distribution generalization. Gains extend to Qwen3-4B, Qwen2.5-Math-1.5B, Qwen3.5-9B and to countdown, and scientific coding tasks. Further analysis shows more accurate tracking of value evolution and more reliable advantage estimates. Our code is publicly available in https://github.com/LINs-lab/TPPO.
