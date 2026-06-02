---
source: farmer/huggingface
farmed: 2026-06-02T10:59:39Z
arxiv_id: 2605.28983
url: https://huggingface.co/papers/2605.28983
arxiv_url: https://arxiv.org/abs/2605.28983
date: 2026-06-02
---

# The Hamilton-Jacobi Theory of Deep Learning

In this paper, training a neural network is identified, exactly, as a search through Hamilton--Jacobi initial-value problems: each gradient step selects the initial data of a viscous Hamilton--Jacobi equation whose Hopf--Cole propagator best fits the observations; at inference, the input is the spatial point at which that solution is evaluated and the initial condition is already encoded in the weights. The correspondence is exact for log-sum-exp layers and structural for broader architectures: residual networks, transformers, and recurrent architectures (RNNs, LSTMs, SSMs) each discretize the same class of Hamilton--Jacobi equations, with architecture-dependent Hamiltonian and viscosity. A single deformation parameter varepsilon unifies all four perspectives (network, tropical algebra, viscous PDE, convex optimization) in a commutative diagram closed under Lipschitz conditions. Quantitative consequences include: the minimax optimal generalization rate O(n^{-1/(d+2)}) for fixed t; adversarial robustness controlled by varepsilon; backpropagation as the co-state equation of the Hamiltonian system for residual networks (Pontryagin Maximum Principle); scaling exponents consistent with data intrinsic dimension via PDE quadrature; and a closed-form O(N) influence function (softmax attribution weights π_j) whose entropy landscape undergoes fold bifurcations as varepsilon increases, each merging attribution basins.
