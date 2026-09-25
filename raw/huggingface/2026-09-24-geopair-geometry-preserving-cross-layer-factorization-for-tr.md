---
source: farmer/huggingface
farmed: 2026-09-25T17:06:04.306887+00:00
arxiv_id: 2609.25963
url: https://huggingface.co/papers/2609.25963
arxiv_url: https://arxiv.org/abs/2609.25963
date: 2026-09-24
upvotes: 13
authors: ["Baher Mohammad", "Ammar Ali", "Stamatios Lefkimmiatis"]
---

# GeoPair: Geometry-Preserving Cross-Layer Factorization for Training-Free Transformer Compression

**Authors:** Baher Mohammad, Ammar Ali, Stamatios Lefkimmiatis

**Upvotes:** 13

**Links:** [HuggingFace](https://huggingface.co/papers/2609.25963) · [arXiv](https://arxiv.org/abs/2609.25963)

Transformer architectures exhibit cross-layer redundancies, yet post-training compression pipelines typically optimize layers in isolation or rely on heuristic grouping strategies that disregard layer-specific activation geometries. We introduce a principled, training-free framework that sequentially optimizes cross-layer weight pairings and shared-dictionary factorizations. Rather than forcing weights of adjacent layers to share a basis or heuristically merging activation statistics, our approach identifies structurally compatible projections and learns a shared representation that better preserves each layer's distinct calibration geometry. Coupled with structured sparsity, this yields highly efficient weight decompositions without sacrificing functional fidelity. Across diverse architectures, scales, and modalities, our method achieves state-of-the-art results, consistently outperforming independent structured weight decompositions and alternative pairwise weight factorizations, which operate under heuristic grouping strategies. By replacing heuristic engineering strategies with a convergent, optimization-driven pipeline, we establish a theoretically grounded foundation for scalable, transformer compression across different modalities.
