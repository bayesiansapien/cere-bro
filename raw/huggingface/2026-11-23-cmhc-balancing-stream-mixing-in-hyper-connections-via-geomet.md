---
source: farmer/huggingface
farmed: 2026-11-24T05:05:48.245833+00:00
arxiv_id: 2611.27193
url: https://huggingface.co/papers/2611.27193
arxiv_url: https://arxiv.org/abs/2611.27193
date: 2026-11-23
---

# cmHC: Balancing Stream Mixing in Hyper-Connections via Geometric Contraction

Manifold-constrained Hyper-Connections (mHC) extends residual connections to multiple streams and stabilizes residual propagation by constraining stream-mixing residual matrices to the Birkhoff polytope, the set of doubly stochastic matrices. In this work, we investigate how to effectively mix residual streams within the Birkhoff polytope. We reveal a mixing trade-off: when under-mixed residual matrices stay close to the vertices of the Birkhoff polytope, hyper-connections will degenerate into a set of nearly independent streams; when over-mixed residual matrices are concentrated around the uniform barycenter of the polytope, streams will become less distinguishable from each other. We theoretically validate our findings by bounding the cumulative residual mixing, stream difference and gradient difference of mixing coefficients across layers. Motivated by these findings, we propose Contraction for Manifold-Constrained Hyper-Connections (cmHC), an exact doubly stochastic method which geometrically contracts the Birkhoff polytope toward its interior. This contraction mitigates under-mixing by forcing the residual matrices to explore deeper into the polytope, with a provable stream mixing bound and no new parameterization. Moreover, we apply a moderate contraction at the shallow layers to prevent over-mixing, enabling stable gradient propagation on extremely large-scale model pretraining. Extensive experiments across dense and mixture-of-experts models at various parameter scales demonstrate the effectiveness and scalability of cmHC. We also develop fused operators for cmHC on Ascend NPUs, reducing hyper-connection execution latency by up to 44.8%.
