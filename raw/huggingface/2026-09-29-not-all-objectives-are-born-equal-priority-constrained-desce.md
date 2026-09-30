---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.936669+00:00
arxiv_id: 2606.29521
url: https://huggingface.co/papers/2606.29521
arxiv_url: https://arxiv.org/abs/2606.29521
date: 2026-09-29
---

# Not All Objectives Are Born Equal: Priority-Constrained Descent for Hierarchical Multi-Objective Optimization

Deep learning problems rarely involve objectives that are equal in importance. A primary objective defines the goal, whilst secondary objectives, such as sparsity, compression, or robustness constrain the solution. While existing multi-objective methods have proven effective in practice, they have a clear symmetry problem and neglect the inherent objective hierarchy built into these objective spaces. We introduce Priority-Constrained Descent (PCD), a gradient-based optimization framework designed to explicitly exploit hierarchical objective structures. PCD preserves the direction of primary descent whilst allowing for the minimal distortion necessary to guarantee progress on secondary objectives, controlled by a single τin [0, 1] that dictates the strength of the distortion. The resulting formulation is invariant to objective scaling and admits exact closed-form solutions for problems with two and three objectives. We evaluate PCD within structured network compression settings, unstructured sparsity and low-rankness, and across a variety of synthetic experiments, showing Pareto dominance and better per-objective performance with secondary progress guarantees over existing methods, further exhibiting the interpretable trade-off that τ provides.
