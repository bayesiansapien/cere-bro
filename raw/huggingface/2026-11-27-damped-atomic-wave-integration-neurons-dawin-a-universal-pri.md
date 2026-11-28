---
source: farmer/huggingface
farmed: 2026-11-28T10:45:04+05:30
arxiv_id: 2611.30025
url: https://huggingface.co/papers/2611.30025
arxiv_url: https://arxiv.org/abs/2611.30025
date: 2026-11-27
---

# Damped Atomic Wave Integration Neurons (DAWIN): A Universal Primitive for Continuous-Time Spatiotemporal Learning

Conventional artificial neurons separate spatial feature aggregation from continuous physical time, limiting their ability to model irregular observations. We introduce the Damped Atomic Wave Integration Neuron (DAWIN), a continuous-time primitive for replacing standard neural layers in MLPs, Transformers, and graph neural networks. DAWIN couples spatial projection with elapsed-time-dependent wave excitation and integrates it into a local complex state through closed-form damped evolution, avoiding numerical differential equation solvers. We show that DAWIN generalizes static sinusoidal and memoryless wave neurons on interval-augmented inputs, derive closed-form gradients, and establish bounded-input bounded-output stability for positive damping and sampling intervals bounded away from zero. An associative Triton prefix-scan implementation, DAWINLinear, uses FP32 accumulation and achieves O(log L) parallel depth for sequence length L. Across 11 parameter-matched tasks covering irregular oscillators, MuJoCo dynamics, pedestrian trajectories, and PhysioNet 2012 clinical sequences, DAWIN outperforms Neural CDE on 9 tasks and ReLU-MLP on 8. It achieves the lowest error on dense clinical dynamics (0.9531 NRMSE, winning across all 10 seeds) and ties for the best mortality prediction (0.9993 AUROC). Shuffling elapsed intervals increases error by 58.2%-77.4% on selected dynamics tasks, versus 0.06% on a time-irrelevant control, supporting reliance on physical timing. On NVIDIA B200 GPUs, parallel wave integration accelerates inference by up to 2,630 times over its serial implementation and reduces peak GPU memory by up to 97.6% relative to Mamba in the tested configurations.
