# The Hamilton-Jacobi Theory of Deep Learning

## TL;DR

This paper claims that training a neural network is, exactly, a search through Hamilton-Jacobi initial-value problems. A Hamilton-Jacobi equation is a partial differential equation (PDE) from classical mechanics that describes how a wavefront or value function propagates. The paper says each gradient step selects the initial data of a viscous Hamilton-Jacobi equation whose Hopf-Cole propagator (a known solution formula) best fits the data, and at inference the input is just the spatial point where that solution is evaluated, with the trained weights encoding the initial condition. The correspondence is exact for log-sum-exp layers and structural for broader families: residual networks, transformers, and recurrent architectures (RNNs, LSTMs, SSMs) all discretize the same class of viscous Hamilton-Jacobi PDE, each with its own architecture-dependent Hamiltonian and viscosity. A single deformation parameter epsilon ties together four views of the same object, network, tropical algebra, viscous PDE, and convex optimization, in one commutative diagram, and yields quantitative consequences like a minimax-optimal generalization rate, robustness controlled by epsilon, and backpropagation reinterpreted as the co-state equation of the Hamiltonian system.

```
   training = choose Hamilton-Jacobi INITIAL DATA (encoded in the weights)
   inference = EVALUATE the HJ solution at the input point

        [ Neural Network ] ◄──── ε ────► [ Tropical Algebra ]
               ▲                                  ▲
               │ ε                                │ ε
               ▼                                  ▼
   [ Viscous Hamilton-Jacobi PDE ] ◄── ε ──► [ Convex Optimization ]

   each architecture = a DISCRETIZATION of the same PDE,
   with its own Hamiltonian + viscosity (ResNet / Transformer / RNN / LSTM / SSM)
```

## Key points

- A single deformation parameter epsilon unifies four perspectives, network, tropical algebra, viscous Hamilton-Jacobi PDE, and convex optimization, in one commutative diagram closed under Lipschitz conditions; exact for log-sum-exp layers, structural for transformers, RNNs, and SSMs.
- Derives a minimax-optimal generalization rate of O(n^(-1/(d+2))) for fixed time t, with scaling exponents that track the data's intrinsic dimension via PDE quadrature.
- Adversarial robustness is controlled by the viscosity parameter epsilon, giving a single knob that connects smoothing to robustness.
- Backpropagation is identified as the co-state equation of the Hamiltonian system for residual networks, that is, the Pontryagin Maximum Principle from optimal control.
- Yields a closed-form O(N) influence function whose softmax attribution weights have an entropy landscape that undergoes fold bifurcations as epsilon increases, each merging attribution basins.

## How this relates to prior wiki pages

This is a foundational theory paper rather than a method, so it connects to the wiki's architecture-and-optimizer-codesign thread at the framing level. The wiki has tracked the idea that the optimizer is not separable from the architecture, a theme in [attention-mechanisms.md](attention-mechanisms.md) and in spectral-shaping work like [DynMuon spectral shaping (2026-05-21)](2026-05-21-dynmuon-spectral-shaping.md) and [same-architecture optimizer-induced spectral scaling (2026-05-23)](2026-05-23-same-architecture-optimizer-induced-spectral-scaling.md). The Hamilton-Jacobi framing pushes that further: it says ResNets, transformers, and SSMs are not different model families but different discretizations of one viscous PDE, which would unify many of the per-architecture observations the wiki records separately. It also gives a principled home for generalization-rate and influence-function results that prior pages treated empirically. No prior page is contradicted; this paper would, if it holds up, supply the underlying theory several of them have been circling.

## Gaps

The correspondence is described as exact only for log-sum-exp layers and merely structural for transformers, RNNs, and SSMs, so how much of the quantitative payoff (the generalization rate, the robustness bound) actually transfers to real transformer architectures rather than the idealized PDE is the central open question. The minimax-optimal rate O(n^(-1/(d+2))) is a worst-case statement for fixed t and may not describe the regimes large models actually train in. The paper is theoretical; there are no experiments validating that the predicted epsilon-robustness tradeoff or the fold-bifurcation influence landscape match measured behavior in trained networks.

**Source:** [arXiv 2605.28983](https://arxiv.org/abs/2605.28983) · [raw file](../../raw/huggingface/2026-06-02-the-hamilton-jacobi-theory-of-deep-learning.md)
