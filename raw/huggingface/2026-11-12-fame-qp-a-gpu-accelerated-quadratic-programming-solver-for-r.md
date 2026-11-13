---
source: farmer/huggingface
farmed: 2026-11-13T13:09:18.382594+05:30
arxiv_id: 2611.13766
url: https://huggingface.co/papers/2611.13766
arxiv_url: https://arxiv.org/abs/2611.13766
date: 2026-11-12
---

# FAME-QP: A GPU-Accelerated Quadratic-Programming Solver for Real-Time Model Predictive Control

We present FAME-QP, a GPU-accelerated solver for dense quadratic programs arising in linear model predictive control. FAME-QP combines constraint-dependent operator representations with fused single- and two-kernel iterations replayed through CUDA graphs, automatically selecting the execution configuration through device calibration and problem-specific timing. It probes a cached operator bank to select the initial penalty and updates operators lazily when problem matrices change. Numerical benchmarks and simulated humanoid and quadrotor control experiments demonstrate reduced latency relative to competing GPU solvers while maintaining solution accuracy and control performance.
