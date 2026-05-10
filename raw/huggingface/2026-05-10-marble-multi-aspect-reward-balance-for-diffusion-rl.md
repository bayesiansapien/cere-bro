---
source: farmer/huggingface
farmed: 2026-05-10T03:37:12Z
arxiv_id: 2605.06507
url: https://huggingface.co/papers/2605.06507
arxiv_url: https://arxiv.org/abs/2605.06507
date: 2026-05-10
---

# MARBLE: Multi-Aspect Reward Balance for Diffusion RL

Reinforcement learning fine-tuning has become the dominant approach for aligning diffusion models with human preferences. We find that failure stems from using a naive weighted-sum reward aggregation. We propose MARBLE (Multi-Aspect Reward BaLancE), a gradient-space optimization framework that maintains independent advantage estimators for each reward, computes per-reward policy gradients, and harmonizes them into a single update direction without manually-tuned reward weighting, by solving a Quadratic Programming problem. On SD3.5 Medium with five rewards, MARBLE improves all five reward dimensions simultaneously.
