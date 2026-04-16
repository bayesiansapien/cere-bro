---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2507.09503
category: cs.LG
concept: inference-efficiency
url: https://arxiv.org/abs/2507.09503
published: 2026-04-16
authors: Zhentong Shao, Jingtao Qin, Nanpeng Yu
---

# Neural Two-Stage Stochastic Optimization for Solving Unit Commitment Problem

**arXiv:** https://arxiv.org/abs/2507.09503
**Authors:** Zhentong Shao, Jingtao Qin, Nanpeng Yu

## Abstract

arXiv:2507.09503v4 Announce Type: replace-cross  Abstract: This paper proposes a neural stochastic optimization method for efficiently solving the two-stage stochastic unit commitment (2S-SUC) problem under high-dimensional uncertainty scenarios. The proposed method approximates the second-stage recourse problem using a deep neural network trained to map commitment decisions and uncertainty features to recourse costs. The trained network is subsequently embedded into the first-stage UC problem as a mixed-integer linear program (MILP), allowing for explicit enforcement of operational constraints while preserving the key uncertainty characteristics. A scenario-embedding network is employed to enable dimensionality reduction and feature aggregation across arbitrary scenario sets, serving as a data-driven scenario reduction mechanism. Numerical experiments on IEEE 5-bus, 30-bus, and 118-bus systems demonstrate that the proposed neural two-stage stochastic optimization method achieves solutions with an optimality gap of less than 1%, while enabling orders-of-magnitude speedup compared to conventional MILP solvers and decomposition-based methods. Moreover, the model's size remains constant regardless of the number of scenarios, offering significant scalability for large-scale stochastic unit commitment problems.
