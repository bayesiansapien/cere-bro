---
source: farmer/huggingface
farmed: 2026-11-10T05:05:44.201179+00:00
arxiv_id: 2611.08264
url: https://huggingface.co/papers/2611.08264
arxiv_url: https://arxiv.org/abs/2611.08264
date: 2026-11-09
---

# SplatAnything: Gaussian Spacing Normalization for Feed-forward 3DGS across Arbitrary Scenes

We identify a key limitation of existing feed-forward 3DGS methods: Gaussian attributes are typically predicted in a radial-distance-normalized space that canonicalizes a global radial statistic of the reconstructed geometry, while the spacing between neighboring Gaussian centers can still vary substantially across scene scales and camera configurations. This mismatch induces systematic shifts in Gaussian-scale targets, leading to ambiguous supervision. To address this, we propose SplatAnything with Gaussian Spacing Normalization (GSNorm), which canonicalizes a robust scene-level statistic of Gaussian spacing to provide a more consistent spatial reference for Gaussian prediction. To rigorously assess our method, we further establish a systematic benchmark spanning diverse datasets, input sparsity levels, and challenging extrapolated viewpoints. Extensive experiments demonstrate that SplatAnything achieves state-of-the-art performance, with particularly strong gains under substantial variations in scene scale and viewpoint.
