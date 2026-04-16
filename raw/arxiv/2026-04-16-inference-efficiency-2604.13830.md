---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13830
category: cs.LG
concept: inference-efficiency
url: https://arxiv.org/abs/2604.13830
published: 2026-04-16
authors: Haoning Dang, Fei Wang, Yifan Chen
---

# Randomized Neural Networks for Integro-Differential Equations with Application to Neutron Transport

**arXiv:** https://arxiv.org/abs/2604.13830
**Authors:** Haoning Dang, Fei Wang, Yifan Chen

## Abstract

arXiv:2604.13830v1 Announce Type: cross  Abstract: Integro-differential equations arise in a wide range of applications, including transport, kinetic theory, radiative transfer, and multiphysics modeling, where nonlocal integral operators couple the solution across phase space. Such nonlocality often introduces dense coupling blocks in deterministic discretizations, leading to increased computational cost and memory usage, while physics-informed neural networks may suffer from expensive nonconvex training and sensitivity to hyperparameter choices. In this work, we present randomized neural networks (RaNNs) as a mesh-free collocation framework for linear integro-differential equations. Because the RaNN approximation is intrinsically dense through globally supported random features, the nonlocal integral operator does not introduce an additional loss of sparsity, while the approximate solution can still be represented with relatively few trainable degrees of freedom. By randomly fixing the hidden-layer parameters and solving only for the linear output weights, the training procedure reduces to a convex least-squares problem in the output coefficients, enabling stable and efficient optimization. As a representative application, we apply the proposed framework to the steady neutron transport equation, a high-dimensional linear integro-differential model featuring scattering integrals and diverse boundary conditions. Extensive numerical experiments demonstrate that, in the reported test settings, the RaNN approach achieves competitive accuracy while incurring substantially lower training cost than the selected neural and deterministic baselines, highlighting RaNNs as a robust and efficient alternative for the numerical simulation of nonlocal linear operators.
