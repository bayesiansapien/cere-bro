---
source: farmer/huggingface
farmed: 2026-08-13T03:36:17.258300+00:00
arxiv_id: 2608.10708
url: https://huggingface.co/papers/2608.10708
arxiv_url: https://arxiv.org/abs/2608.10708
date: 2026-08-13
---

# Self-Geometry: GT-Free and Plug-and-Play Test-Time Adaptation for Geometrically Consistent 3D Vision Foundation Models

Recent Vision Foundation Models (VFMs) predict depth, camera pose, and pointmap in a single forward pass without per-scene optimization, achieving strong generalization. However, enforcing explicit multi-view geometric consistency, e.g., through bundle adjustment, is computationally costly and is thus not imposed during VFM pretraining, so such inconsistency can arise. To address this, implicit self-consistency derived from model outputs (e.g., pointmaps, features), though enforced at test-time in prior work, delivers inherently limited performance gain, especially on scenes where the pretrained VFM is highly inaccurate. In contrast to this implicit signal, we propose Self-Geometry, a plug-and-play test-time adaptation pipeline that directly imposes explicit multi-view geometric constraints using 2D pixel correspondences as pseudo ground-truth. Our proposed Self-Geometry consists of Geometric Disentanglement Optimization, which combines Multi-View Consistency and Epipolar Consistency losses with Gradient Disentanglement to prevent gradient conflict; Frame Angular-Neighbor, a view sampler based on SO(3) geodesic distances for lightly imposing these constraints; and Lightweight TTA, which adapts VFMs via LoRA. Our method achieves consistent improvements in both pose and geometry estimation across six VFMs (VGGT, π^3, DA3-Giant/Large/Base/Small) and four benchmarks (7Scenes, ETH3D, ScanNet++, HiRoom).
