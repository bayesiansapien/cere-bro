---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2405.20836
category: cs.LG
concept: agents-tool-use
url: https://arxiv.org/abs/2405.20836
published: 2026-04-16
authors: Chinmay Datar, Taniya Kapoor, Abhishek Chandra
---

# Fast training of accurate physics-informed neural networks without gradient descent

**arXiv:** https://arxiv.org/abs/2405.20836
**Authors:** Chinmay Datar, Taniya Kapoor, Abhishek Chandra

## Abstract

arXiv:2405.20836v3 Announce Type: replace-cross  Abstract: Solving time-dependent Partial Differential Equations (PDEs) is one of the most critical problems in computational science. While Physics-Informed Neural Networks (PINNs) offer a promising framework for approximating PDE solutions, their accuracy and training speed are limited by two core barriers: gradient-descent-based iterative optimization over complex loss landscapes and non-causal treatment of time as an extra spatial dimension. We present Frozen-PINN, a novel PINN based on the principle of space-time separation that leverages random features instead of training with gradient descent, and incorporates temporal causality by construction. On eight PDE benchmarks, including challenges such as extreme advection speeds, shocks, and high dimensionality, Frozen-PINNs achieve superior training efficiency and accuracy over state-of-the-art PINNs, often by several orders of magnitude. Our work addresses longstanding training and accuracy bottlenecks of PINNs, delivering quickly trainable, highly accurate, and inherently causal PDE solvers, a combination that prior methods could not realize. Our approach challenges the reliance of PINNs on stochastic gradient-descent-based methods and specialized hardware, leading to a paradigm shift in PINN training and providing a challenging benchmark for the community.
