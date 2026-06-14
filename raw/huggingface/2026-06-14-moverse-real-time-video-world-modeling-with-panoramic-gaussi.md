---
source: farmer/huggingface
farmed: 2026-06-14T07:38:18Z
arxiv_id: 2606.13376
url: https://huggingface.co/papers/2606.13376
arxiv_url: https://arxiv.org/abs/2606.13376
date: 2026-06-14
---

# MoVerse: Real-Time Video World Modeling with Panoramic Gaussian Scaffold

We present MoVerse, a real-time video world model that creates an interactively navigable scene from a single narrow-field-of-view image. This setting is challenging because the input observes only a small fraction of the environment, while interactive roaming requires a complete surrounding world, persistent geometry, controllable camera motion, and temporally coherent high-fidelity observations. MoVerse addresses this problem by separating world construction from observation rendering. It first expands the input into a gravity-aligned 360^circ panorama with topology-aware diffusion, closing the missing field of view before 3D reasoning. It then lifts the panorama into a persistent 3D Gaussian scaffold using panoramic geometry-aware residual prediction, yielding a dense and directly renderable spatial memory. Finally, a Gaussian-conditioned video renderer translates scaffold renderings along user-specified camera trajectories into photorealistic video. To make this renderer practical for interaction, we train a bidirectional diffusion teacher for high-quality conditional rendering and distill it into a causal autoregressive student for bounded-latency streaming. This design combines the controllability and long-range consistency of explicit 3D representations with the perceptual quality of generative video models. MoVerse supports real-time scene roaming at 8~FPS on a single NVIDIA RTX~4090 GPU, demonstrating a practical path toward single-image world creation with interactive video output.
