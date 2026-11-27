---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.902704+00:00
arxiv_id: 2611.30844
url: https://huggingface.co/papers/2611.30844
arxiv_url: https://arxiv.org/abs/2611.30844
date: 2026-11-26
---

# DyLoMo-DiT: Dynamic Looped Mixture-of-Experts Diffusion Transformers

Diffusion Transformers (DiTs) scale model capacity by increasing both parameter count and computation. Mixture-of-Experts (MoE) variants expand parameter capacity while keeping per-token computation roughly fixed, but still require substantial parameter storage. In this paper, we propose Dynamic Looped MoE DiT (DyLoMo-DiT), which reuses parameters rather than adding them: a weight-shared loop repeatedly applies the middle layers, while sparse experts allocate parameter capacity across tokens. This design deepens the network without adding parameters, freeing the parameter budget for other uses, such as more experts or more distinct layers. It also allocates compute dynamically, varying the number of passes across noise levels. Experiments show that DyLoMo-DiT makes more effective use of parameter and compute budgets, with further gains from assigning more passes to low-noise steps. On ImageNet 256times256, DyLoMo-DiT reduces FID by 11-24% relative to DiT and 36-56% relative to DiT-MoE at matched parameter and compute budgets. For text-to-image generation, a scaled DyLoMo-DiT achieves a higher GenEval score than FLUX.1 (0.714 vs. 0.673), with less than one tenth of its active parameters (1.05B vs. 12B).
