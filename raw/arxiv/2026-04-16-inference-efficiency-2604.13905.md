---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13905
category: cs.CV
concept: inference-efficiency
url: https://arxiv.org/abs/2604.13905
published: 2026-04-16
authors: Zhiyuan Xu, Jiuming Liu, Yuxin Chen
---

# Rethinking Image-to-3D Generation with Sparse Queries: Efficiency, Capacity, and Input-View Bias

**arXiv:** https://arxiv.org/abs/2604.13905
**Authors:** Zhiyuan Xu, Jiuming Liu, Yuxin Chen

## Abstract

arXiv:2604.13905v1 Announce Type: new  Abstract: We present SparseGen, a novel framework for efficient image-to-3D generation, which exhibits low input-view bias while being significantly faster. Unlike traditional approaches that rely on dense volumetric grids, triplanes, or pixel-aligned primitives, we model scenes with a compact sparse set of learned 3D anchor queries and a learned expansion operator that decodes each transformed query into a small local set of 3D Gaussian primitives. Trained under a rectified-flow reconstruction objective without 3D supervision, our model learns to allocate representation capacity where geometry and appearance matter, achieving significant reductions in memory and inference time while preserving multi-view fidelity. We introduce quantitative measures of input-view bias and utilization to show that sparse queries reduce overfitting to conditioning views while being representationally efficient. Our results argue that sparse set-latent expansion is a principled, practical alternative for efficient 3D generative modeling.
