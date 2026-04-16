---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13723
category: cs.LG
concept: agents-tool-use
url: https://arxiv.org/abs/2604.13723
published: 2026-04-16
authors: Kentaro Hoshisashi, Carolyn E Phelan, Paolo Barucca
---

# Physics-Informed Neural Networks for Solving Derivative-Constrained PDEs

**arXiv:** https://arxiv.org/abs/2604.13723
**Authors:** Kentaro Hoshisashi, Carolyn E Phelan, Paolo Barucca

## Abstract

arXiv:2604.13723v1 Announce Type: new  Abstract: Physics-Informed Neural Networks (PINNs) recast PDE solving as an optimisation problem in function space by minimising a residual-based objective, yet many applications require additional derivative-based relations that are just as fundamental as the governing equations. In this paper, we present Derivative-Constrained PINNs (DC-PINNs), a general framework that treats constrained PDE solving as an optimisation guided by a minimum objective function criterion where the physics resides in the minimum principle. DC-PINNs embed general nonlinear constraints on states and derivatives, e.g., bounds, monotonicity, convexity, incompressibility, computed efficiently via automatic differentiation, and they employ self-adaptive loss balancing to tune the influence of each objective, reducing reliance on manual hyperparameters and problem-specific architectures. DC-PINNs consistently reduce constraint violations and improve physical fidelity versus baseline PINN variants, representative hard-constraint formulations on benchmarks, including heat diffusion with bounds, financial volatilities with arbitrage-free, and fluid flow with vortices shed. Explicitly encoding derivative constraints stabilises training and steers optimisation toward physically admissible minima even when the PDE residual alone is small, providing reliable solutions of constrained PDEs grounded in energy minimum principles.
