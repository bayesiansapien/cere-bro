---
source: farmer/huggingface
farmed: 2026-05-22T10:21:55.060746+00:00
arxiv_id: 2605.21343
url: https://huggingface.co/papers/2605.21343
arxiv_url: https://arxiv.org/abs/2605.21343
date: 2026-05-21
---

# OcclusionFormer: Arranging Z-Order for Layout-Grounded Image Generation

Recent layout-to-image models have achieved remarkable progress in spatial controllability. However, they still struggle with inter-object occlusion. When bounding boxes overlap, most existing methods lack explicit occlusion information, which makes the generation in intersection regions inherently ambiguous and hinders the determination of complex occlusion relationships. As a result, they often produce entangled textures or physically inconsistent layering in the overlapped areas. To address this issue, we first construct SA-Z, a large-scale dataset enriched with explicit occlusion ordering and pixel-level annotations. Building upon our proposed dataset, we introduce OcclusionFormer, a novel occlusion-aware Diffusion Transformer framework that explicitly models Z-order priority by decoupling instances and compositing them via volume rendering. Furthermore, to ensure fine-grained spatial precision, we introduce a queried alignment loss that explicitly supervises individual instances and enhances semantic consistency. The proposed method effectively reduces ambiguity in overlapping regions, enforces correct occlusion dependencies, and preserves structural integrity, leading to substantial accuracy gains across diverse scenes.
