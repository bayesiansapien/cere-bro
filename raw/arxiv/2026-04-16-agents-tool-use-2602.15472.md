---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2602.15472
category: cs.LG
concept: agents-tool-use
url: https://arxiv.org/abs/2602.15472
published: 2026-04-16
authors: Ramansh Sharma, Matthew Lowery, Houman Owhadi
---

# Fluids You Can Trust: Property-Preserving Operator Learning for Incompressible Flows

**arXiv:** https://arxiv.org/abs/2602.15472
**Authors:** Ramansh Sharma, Matthew Lowery, Houman Owhadi

## Abstract

arXiv:2602.15472v4 Announce Type: replace-cross  Abstract: We present a novel property-preserving kernel-based operator learning method for incompressible flows governed by the incompressible Navier--Stokes equations. Traditional numerical solvers incur significant computational costs to respect incompressibility. Operator learning offers efficient surrogate models, but current neural operators fail to exactly enforce physical properties such as incompressibility, periodicity, and turbulence. Our kernel method maps input functions to expansion coefficients of output functions in a property-preserving kernel basis, ensuring that predicted velocity fields $\textit{analytically}$ and $\textit{simultaneously}$ preserve the aforementioned physical properties. Our method leverages efficient numerical linear algebra, simple rootfinding, and streaming to allow for training at-scale on desktop GPUs. We also present universal approximation results and both pessimistic and more realistic $\textit{a priori}$ convergence rates for our framework. We evaluate the method on challenging 2D and 3D, laminar and turbulent, incompressible flow problems. Our method achieves up to six orders of magnitude lower relative $\ell_2$ errors upon generalization and trains up to five orders of magnitude faster compared to neural operators, despite our method being trained on desktop GPUs and neural operators being trained on cutting-edge GPU servers. Moreover, while our method enforces incompressibility analytically, neural operators exhibit very large deviations. Our results show that our method provides an accurate and efficient surrogate for incompressible flows.
