---
source: farmer/huggingface
farmed: 2026-11-24T05:05:48.246418+00:00
arxiv_id: 2611.27963
url: https://huggingface.co/papers/2611.27963
arxiv_url: https://arxiv.org/abs/2611.27963
date: 2026-11-23
---

# Non-penetrating World Models

We study a new problem of preventing object penetration in interactive video world models. To understand how existing models handle this, we introduce NoPeBench, a benchmark that evaluates how world models respond to physical obstacles. Our evaluation reveals that none of the open-source models can reliably prevent such failures. Surprisingly, however, these models already encode the information needed to predict such violations. We find that the hidden states of diffusion transformers (DiTs) can predict whether a candidate action will penetrate an obstacle. Building on this, we introduce NoPeWorld, a lightweight framework that detects and prevents penetration. Specifically, we train a small prediction head on top of a frozen DiT's hidden states to read out if a candidate action is safe or not. Unsafe actions are then replaced with safe ones that best preserve the original intent. Despite its simplicity, NoPeWorld substantially reduces the physical violation rate, averaged over six video world models, from 74% to 16%. Remarkably, our method shows zero-shot generalization to open-domain imagery, third-person viewpoints, and moving obstacles. We publicly release our code, the NoPeBench benchmark, and model weights. Project Page: https://nopeworld.github.io .
