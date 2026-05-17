---
source: farmer/huggingface
farmed: 2026-05-17T00:00:00Z
arxiv_id: "2605.15190"
url: "https://huggingface.co/papers/2605.15190"
arxiv_url: "https://arxiv.org/abs/2605.15190"
date: 2026-05-17
---

# RAVEN: Real-time Autoregressive Video Extrapolation with Consistency-model GRPO

Causal autoregressive video diffusion models support real-time streaming generation by extrapolating future chunks from previously generated content. Distilling such generators from high-fidelity bidirectional teachers yields competitive few-step models, yet a persistent gap between the history distributions encountered during training and those arising at inference constrains generation quality over long horizons. We introduce the Real-time Autoregressive Video Extrapolation Network (RAVEN), a training-time test framework that repacks each self rollout into an interleaved sequence of clean historical endpoints and noisy denoising states. This formulation aligns training attention with inference-time extrapolation and allows downstream chunk losses to supervise the history representations on which future predictions depend. We further propose Consistency-model Group Relative Policy Optimization (CM-GRPO), which reformulates a consistency sampling step as a conditional Gaussian transition and applies online Reinforcement Learning (RL) directly to this kernel, avoiding the Euler-Maruyama auxiliary process adopted in prior flow-model RL formulations.
