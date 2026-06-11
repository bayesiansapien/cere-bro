---
source: farmer/huggingface
farmed: 2026-06-11T08:27:36Z
arxiv_id: 2606.12397
url: https://huggingface.co/papers/2606.12397
arxiv_url: https://arxiv.org/abs/2606.12397
date: 2026-06-11
---

# Redesign Mixture-of-Experts Routers with Manifold Power Iteration

Router is the cornerstone component to the Mixture-of-Experts models. Serving as expert proxies, the rows of the router matrix compute their similarity to the MoE inputs to determine which subset of experts is activated. Ideally, each router row is designed to encode the expert matrix into this representative vector, such that its dot-product with token can better reflect token-expert affinity. However, there exists no design principles to enforce this condensation. In this paper, we propose to align each router row with the principal singular direction of the associated expert, as this direction provides the most expressive mathematical description of a matrix. Based on this principle, we propose a router redesign with Manifold Power Iteration (MPI). Specifically, it introduces a "Power-then-Retract" paradigm, where a power iteration step is performed on the router weights, followed by a retraction to impose a norm constraint to ensure both efficiency and stability. Theoretically, we show that MPI drives router rows to converge toward the principal singular directions of associated experts. Empirically, we pretrain MoE model across scales from 1B to 11B parameters to confirm that this alignment facilitates more effective MoE models.
