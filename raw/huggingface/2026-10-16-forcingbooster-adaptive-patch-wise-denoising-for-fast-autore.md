---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.12625
url: https://huggingface.co/papers/2610.12625
arxiv_url: https://arxiv.org/abs/2610.12625
date: 2026-10-16
---

# ForcingBooster: Adaptive Patch-wise Denoising for Fast Autoregressive Video Diffusion

Autoregressive video diffusion models have become a leading approach to real-time interactive video generation and video world modeling. However, existing methods typically allocate computation uniformly across space when generating the next video chunk, updating all patches with the same denoising schedule and number of function evaluations. This ignores the spatial heterogeneity of video content: static, simple, or recurring regions are often easier to denoise, while other regions require further refinement or additional context. A uniform budget thus leads to redundant computation on easy patches, whereas reducing the fixed step count can leave difficult patches insufficiently refined. We introduce , a general framework that dynamically allocates denoising steps to individual patches: easy patches stop early to improve efficiency, while difficult patches receive more refinement steps. This design accelerates generation with negligible quality degradation. Our method is compatible with most existing few-step autoregressive diffusion models, requiring only a lightweight routing module with modest training. Experiments demonstrate that  reduces the total number of denoising steps applied across video patches by about 50\% while maintaining visual quality comparable to the four-step baseline.
