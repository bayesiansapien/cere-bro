---
source: farmer/huggingface
farmed: 2026-05-17T00:00:00Z
arxiv_id: "2605.15055"
url: "https://huggingface.co/papers/2605.15055"
arxiv_url: "https://arxiv.org/abs/2605.15055"
date: 2026-05-17
---

# DiffusionOPD: A Unified Perspective of On-Policy Distillation in Diffusion Models

Reinforcement learning has emerged as a powerful tool for improving diffusion-based text-to-image models, but existing methods are largely limited to single-task optimization. Extending RL to multiple tasks is challenging: joint optimization suffers from cross-task interference and imbalance, while cascade RL is cumbersome and prone to catastrophic forgetting. We propose DiffusionOPD, a new multi-task training paradigm for diffusion models based on Online Policy Distillation (OPD). DiffusionOPD first trains task-specific teachers independently, then distills their capabilities into a unified student along the student's own rollout trajectories. This decouples single-task exploration from multi-task integration and avoids the optimization burden of solving all tasks jointly from scratch. Theoretically, we lift the OPD framework from discrete tokens to continuous-state Markov processes, deriving a closed-form per-step KL objective that unifies both stochastic SDE and deterministic ODE refinement via mean-matching. We formally and empirically demonstrate that this analytic gradient provides lower variance and better generality compared to conventional PPO-style policy gradients.
