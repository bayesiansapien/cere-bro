---
source: farmer/huggingface
farmed: 2026-10-23T08:19:34.192951+00:00
arxiv_id: 2610.13177
url: https://huggingface.co/papers/2610.13177
arxiv_url: https://arxiv.org/abs/2610.13177
date: 2026-10-22
---

# CompactSplat: Spatially Adaptive Gaussian Distribution for Feedforward Scene Reconstruction

Reconstructing 3D scenes from sparse views without per-scene optimization remains highly challenging, especially for recovering accurate geometry and fine textures. While recent feedforward approaches leverage generalizable 3D Gaussian Splatting (3DGS) for scene generation, they typically assign one or multiple Gaussians to each pixel. Such uniform allocation not only produces highly redundant representations by wasting primitives in homogeneous areas, but also fails to exploit the inherent geometric priors of planar surfaces, often resulting in sub-optimal structural modeling. To address these limitations, we present CompactSplat, a novel feedforward framework that enables a content-aware allocation of 3D Gaussians. By integrating texture-guided spatial partitioning with hierarchical sampling, CompactSplat adaptively distributes primitives - concentrating dense Gaussians in complex regions while tiling flat areas with expanded, scale-modulated primitives. Moreover, our framework inherently supports dynamic sparsity control at inference time, enabling seamless trade-offs between rendering fidelity and memory footprint without requiring network retraining. Extensive experiments on RealEstate10K, DL3DV, and ScanNet demonstrate that CompactSplat consistently outperforms prior methods on both standard metrics and high-resolution rendering consistency, achieving high-fidelity reconstructions with significantly fewer primitives.
