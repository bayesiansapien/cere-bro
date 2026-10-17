---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.22311
url: https://huggingface.co/papers/2610.22311
arxiv_url: https://arxiv.org/abs/2610.22311
date: 2026-10-16
---

# Velox: Spatial Memory Makes World Models Efficient

Video world models turn actions and camera motion into long visual rollouts, making video a natural interface for interactive simulation. Such interaction requires responsive generation, yet coherent rollouts must retain visual memory of what has already been generated. Chunked video diffusion models usually keep this context in growing KV caches, so later chunks become progressively slower. To address this bottleneck, we introduce Velox, a training-free attention router for region-level context selection using frustum slab correspondences from streaming geometry. Velox represents historical blocks as camera frustum slabs with depth intervals and obtains current-block depth through recency-priority multiwarp. For well-covered regions, frustum slab overlap softly modulates each layer's model-derived block importance. Uncovered regions retain the model-derived route without geometric bias. The fixed token-block granularity matches FlashAttention-style tiled execution and reduces the attention term that grows with rollout length. Frustum slab construction runs asynchronously with denoising on the same H200. At chunk 48, Velox accelerates attention by 4.36times and denoising by 2.43times. On the full 158-case WBench navigation split, it remains within 0.15 API-free average points of dense LingBot-Fast-Cam. Please see our project page at https://velox-world.com/velox/ for more details.
