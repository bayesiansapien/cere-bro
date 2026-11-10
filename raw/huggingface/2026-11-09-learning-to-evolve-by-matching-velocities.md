---
source: farmer/huggingface
farmed: 2026-11-10T05:05:44.207966+00:00
arxiv_id: 2611.00448
url: https://huggingface.co/papers/2611.00448
arxiv_url: https://arxiv.org/abs/2611.00448
date: 2026-11-09
---

# Learning to evolve by matching velocities

Learning the continuous-time evolution of nonlinear dynamical systems relies on trajectory-based objectives, which require simulating the learned dynamics during training and backpropagating through the numerical scheme, at a cost that grows with the rollout horizon. We show that trajectory-based objectives degenerate as the rollout horizon increases, hindering gradient-based optimization, and that the numerical scheme biases the learned dynamics by constraining the spectrum of the learned Jacobian to its absolute stability region. To overcome these limitations, we introduce Velocity Matching (VM), a simulation-free objective that relies on piecewise-linear interpolation and stochastic collocation, and approximates the velocity population risk to second order in the sampling step. We develop a theoretical framework for velocity-based learning, introducing stability estimates that control trajectory errors in terms of velocity errors, which enable us to establish universal and continuous-time approximation results when the learned velocity field is parameterized by deep neural networks. Building on a bias-variance decomposition of the VM objective, we show that its higher-order approximation of the velocity population risk yields a consistent minimizer; that it relates to the residual of an A-stable continuous-stage Runge-Kutta scheme, thus connecting VM to implicit integration without requiring any implicit solve; and that it implicitly matches the action of the learned Jacobian to that of the true one along the observed trajectories, without requiring access to the underlying velocity field or its Jacobian. Numerical experiments on nonlinear ordinary differential equations and semi-discretized time-dependent partial differential equations show that VM improves accuracy over trajectory-based objectives, while avoiding both the cost of simulation and the instabilities of long rollouts.
