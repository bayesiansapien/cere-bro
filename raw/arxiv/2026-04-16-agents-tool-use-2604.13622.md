---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13622
category: cs.LG
concept: agents-tool-use
url: https://arxiv.org/abs/2604.13622
published: 2026-04-16
authors: Seiki Ubukata, Akira Notsu, Katsuhiro Honda
---

# Self-Organizing Maps with Optimized Latent Positions

**arXiv:** https://arxiv.org/abs/2604.13622
**Authors:** Seiki Ubukata, Akira Notsu, Katsuhiro Honda

## Abstract

arXiv:2604.13622v1 Announce Type: new  Abstract: Self-Organizing Maps (SOM) are a classical method for unsupervised learning, vector quantization, and topographic mapping of high-dimensional data. However, existing SOM formulations often involve a trade-off between computational efficiency and a clearly defined optimization objective. Objective-based variants such as Soft Topographic Vector Quantization (STVQ) provide a principled formulation, but their neighborhood-coupled computations become expensive as the number of latent nodes increases. In this paper, we propose Self-Organizing Maps with Optimized Latent Positions (SOM-OLP), an objective-based topographic mapping method that introduces a continuous latent position for each data point. Starting from the neighborhood distortion of STVQ, we construct a separable surrogate local cost based on its local quadratic structure and formulate an entropy-regularized objective based on it. This yields a simple block coordinate descent scheme with closed-form updates for assignment probabilities, latent positions, and reference vectors, while guaranteeing monotonic non-increase of the objective and retaining linear per-iteration complexity in the numbers of data points and latent nodes. Experiments on a synthetic saddle manifold, scalability studies on the Digits and MNIST datasets, and 16 benchmark datasets show that SOM-OLP achieves competitive neighborhood preservation and quantization performance, favorable scalability for large numbers of latent nodes and large datasets, and the best average rank among the compared methods on the benchmark datasets.
