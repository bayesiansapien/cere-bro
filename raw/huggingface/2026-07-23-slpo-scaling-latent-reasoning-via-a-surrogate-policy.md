---
source: farmer/huggingface
farmed: 2026-07-24T23:47:01.610703+05:30
arxiv_id: 2607.19691
url: https://huggingface.co/papers/2607.19691
arxiv_url: https://arxiv.org/abs/2607.19691
date: 2026-07-23
---

# SLPO: Scaling Latent Reasoning via a Surrogate Policy

Reinforcement learning with verifiable rewards has become the predominant recipe for eliciting test-time scaling in explicit Chain-of-Thought reasoners. Yet this scaling path remains computationally costly, since every intermediate step must be decoded as a language token. Latent reasoning instead carries intermediate computation as continuous vectors and already matches or surpasses explicit CoT at far shorter horizons. Despite this promise, latent reasoners remain largely imitation-bound, while explicit CoT has already moved past imitation via outcome-reward RL. Latent trajectories lack a tractable per-step likelihood and an adaptive stopping interface under fixed thinking budgets, so outcome rewards cannot elicit latent test-time scaling. We introduce Surrogate Latent Policy Optimization (SLPO) to bring outcome-reward RL to autoregressive latent reasoners: an empirical surrogate policy density over latent transitions for trajectory-level credit assignment, and a correctness-supervised stopping head that outcome-reward optimization refines into a variable-horizon policy. Across continuous and soft thinking settings, SLPO improves Pass@k under parallel sampling and allocates longer latent computation to harder instances with higher deterministic accuracy.
