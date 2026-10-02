---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.353821+05:30
arxiv_id: 2609.38814
url: https://huggingface.co/papers/2609.38814
arxiv_url: https://arxiv.org/abs/2609.38814
date: 2026-10-01
---

# Learning Chaos Without Seeing Chaos: Extrapolation of Global Dynamics in Autoregressive Transformers

Autoregressive models are trained to predict a system's behavior one step at a time, and recursive generation allows the learned dynamics to unfold over long horizons. To what extent can such dynamics learned from local observations recover broader organization of an underlying system that was only partially observed during training? Here we study small autoregressive transformers trained from scratch on trajectories sampled from restricted parameter regimes of several non-linear dynamical systems, including logistic and sine maps, the Lorenz system, and the generalized Hopf system, with control parameters and state trajectories represented as sequences of continuous tokens. Under closed-loop evaluation at parameters far outside the training distribution, the models can recover self-similar period-doubling cascades, chaotic dynamics, and attractor structures with remarkable visual and numerical fidelity. For the logistic map, a transformer reproduces successive period doublings up to period 128, yielding a finite-order scaling ratio of 4.6687, matching the Feigenbaum constant to within 5times10^{-4}. We further investigate how these structures emerge over the course of training, and reveal with causal interventions how control-parameter information is processed through attention into state prediction and shapes the resulting closed-loop dynamics. These results suggest that a surprisingly narrow window into a system's local behavior may suffice for autoregressive transformers to generalize to its unseen global dynamical organization.
