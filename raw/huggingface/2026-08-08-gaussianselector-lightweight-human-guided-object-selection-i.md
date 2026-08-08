---
source: farmer/huggingface
farmed: 2026-08-08T22:00:12.430322
arxiv_id: 2608.01492
url: https://huggingface.co/papers/2608.01492
arxiv_url: https://arxiv.org/abs/2608.01492
upvotes: 4
date: 2026-08-08
---

# GaussianSelector: Lightweight Human-Guided Object Selection in 3D Gaussian Splatting with Graph Optimization

Selecting a complete 3D object from a reconstructed scene with minimal user effort is essential for practical scene editing and embodied interaction. Existing 3DGS-based methods either retrain the Gaussian representation to embed per-object labels, or build dense multi-view SAM observations, both requiring heavy computation and dense viewpoint coverage that is rarely available in practice. We present GaussianSelector, a training-free framework for interactive 3D object selection from sparse views and sparse scribble guidance. Operating directly on native Gaussian primitives, we coarsen dense Gaussians into geometrically coherent superpoints and construct a continuity-weighted graph using appearance and spatial cues. Sparse user scribbles are lifted into 3D via visibility-aware transmittance coverage, and selection is solved as a global graph-cut energy minimization that propagates sparse evidence to a complete 3D object. This design naturally supports multi-round refinement, where users iteratively correct the selection from additional viewpoints to progressively improve the result. Experiments demonstrate that GaussianSelector achieves competitive selection quality against state-of-the-art multi-view SAM-based methods, while requiring significantly fewer interaction views and substantially lower computational overhead. These properties make it well suited for human-in-the-loop 3D scene editing and 3D asset extraction in real-world deployment scenarios.
