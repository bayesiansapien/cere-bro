---
source: farmer/huggingface
farmed: 2026-06-09T16:28:21
arxiv_id: 2605.24047
url: https://huggingface.co/papers/2605.24047
arxiv_url: https://arxiv.org/abs/2605.24047
date: 2026-06-09
---

# EMMA: Extracting Multiple physical parameters from Multimodal Data

We introduce EMMA, a physics-informed multimodal framework that recovers all identifiable dynamical parameters of a system directly from raw video, audio, and image-based time-series observations. Unlike prior video-only approaches that struggle with occluded states, hidden actuation inputs, or assumptions about known initial conditions and coordinate frames, EMMA performs joint inference of explicit parameters, implicit dynamical components, and calibration invariants within a unified continuous-time model. EMMA leverages a Liquid Time-Constant (LTC) network to learn latent dynamics from heterogeneous modalities while a physics-constrained loss enforces consistency with the governing differential equations. A unified feature pipeline enables consistent alignment across video trajectories, acoustic signatures, and chart-derived measurements, allowing EMMA to estimate parameters under forced, implicit, and multivariate dynamics without requiring segmentation masks, differentiable rendering, or specialized sensors. Across 100+ scenarios including five standard dynamical benchmarks (75 Delfys videos), real-world rover and quadrotor systems with hidden inputs, and simulation-chart case studies spanning biological and chaotic systems, EMMA delivers robust multi-parameter recovery and significantly outperforms existing single-modality and equation-discovery baselines. Our results establish EMMA as a general, scalable solution for physics-consistent model extraction from opportunistic multimodal data. Code and data are available at: https://github.com/ImpactLabASU/EMMA-CVPR2026
