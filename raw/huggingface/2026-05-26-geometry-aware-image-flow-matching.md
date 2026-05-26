---
source: farmer/huggingface
farmed: 2026-05-26T06:42:03Z
arxiv_id: 2605.25294
url: https://huggingface.co/papers/2605.25294
arxiv_url: https://arxiv.org/abs/2605.25294
date: 2026-05-26
---

# Geometry-Aware Image Flow Matching

Recent advances in generative models highlight the power of geometry-aware modeling in manifold-constrained settings. Yet, for natural images, the field remains confined to Euclidean assumptions, failing to exploit the potential of intrinsic geometric structures within the data. In this work, we investigate the geometry of natural images and observe that semantic information is predominantly encoded in directional components, while norm components can be approximated by the global average. This property holds across both RGB and latent spaces, suggesting that natural images can be effectively modeled on a hypersphere. Building on this finding, we introduce Spherical Optimal Transport Flow Matching (SOT-CFM), which utilizes angular distance, and Spherical Flow Matching (SFM), which constrains dynamics directly on the manifold. Our experiments demonstrate that these geometry-aware methods achieve superior performance against Euclidean baselines. Ultimately, this work provides a novel perspective that bridges the gap between Riemannian manifold-based modeling and natural image generation.
