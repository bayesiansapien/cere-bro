---
source: farmer/huggingface
farmed: 2026-06-14T07:38:18Z
arxiv_id: 2606.10896
url: https://huggingface.co/papers/2606.10896
arxiv_url: https://arxiv.org/abs/2606.10896
date: 2026-06-14
---

# Flash-GMM: A Memory-Efficient Kernel for Scalable Soft Clustering

We present Flash-GMM, a fused Triton kernel for efficient computation of Gaussian Mixture Models (GMMs) over large-scale data in a single GPU pass. By eliminating the need to materialize the full responsibility matrix in GPU memory, Flash-GMM achieves a 20times speedup over existing implementations and enables training on datasets more than 100times larger than previously feasible on one device. To demonstrate its impact, we integrate Flash-GMM into the IVF coarse quantizer for approximate nearest-neighbor (ANN) search. We show that soft GMM clustering is now a viable drop-in replacement for k-means, and that GMM responsibilities can be leveraged to assign border vectors to multiple clusters. Our approach reaches fixed recall targets with up to 1.7times fewer distance computations, or equivalently, yields +2--12 recall@10 at matched computational cost. We release the kernel as an open-source project.
