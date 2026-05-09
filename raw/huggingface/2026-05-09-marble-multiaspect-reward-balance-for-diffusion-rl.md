---
source: farmer/huggingface
farmed: 2026-05-09T03:37:34Z
arxiv_id: 2605.06507
url: https://huggingface.co/papers/2605.06507
arxiv_url: https://arxiv.org/abs/2605.06507
date: 2026-05-09
---

# MARBLE: Multi-Aspect Reward Balance for Diffusion RL

Reinforcement learning (RL) fine-tuning has become the dominant approach for aligning diffusion models with human preferences. However, assessing images is intrinsically a multi-dimensional task, and multiple evaluation criteria need to be optimized simultaneously. We propose MARBLE (Multi-Aspect Reward Balance for diffusion RL), a gradient-space optimization framework that maintains independent advantage estimators for each reward, computes per-reward policy gradients, and harmonizes them into a single update direction without manually-tuned reward weighting by solving a Quadratic Programming problem. On SD3.5 Medium with five rewards, MARBLE improves all five reward dimensions simultaneously and runs at 0.97x the training speed of baseline training.
