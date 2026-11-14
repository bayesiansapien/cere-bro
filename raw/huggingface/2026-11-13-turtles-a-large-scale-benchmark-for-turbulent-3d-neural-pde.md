---
source: farmer/huggingface
farmed: 2026-11-14T05:10:36.530484+00:00
arxiv_id: 2611.09567
url: https://huggingface.co/papers/2611.09567
arxiv_url: https://arxiv.org/abs/2611.09567
date: 2026-11-13
---

# TurtLES: A Large-Scale Benchmark for Turbulent 3D Neural PDE Surrogates

Machine-learning surrogates are increasingly used to accelerate computational fluid dynamics, yet progress is limited by the lack of benchmarks capturing realistic, time-dependent turbulent flows. We introduce TurtLES, a 14 TB dataset of 3D turbulent cylinder wakes in the shear-layer transition regime, computed via high-fidelity implicit large-eddy simulations. The dataset contains 400 trajectories of 400 time steps each, with 3-11 million points per frame, spanning variations in geometry, Reynolds number, and angle of attack. Unlike existing datasets, TurtLES combines (i) physically realistic turbulence with an active energy cascade driven by vortex stretching, (ii) dense irregular meshes, and (iii) long-horizon temporal dynamics. We benchmark state-of-the-art neural operators on autoregressive rollouts and identify key failure modes, including temporal instability, loss of small-scale energy, and challenges in learning on large irregular domains. TurtLES provides a new benchmark for evaluating surrogate models on 3D turbulent wakes at industrially relevant mesh resolution.
