---
source: farmer/huggingface
farmed: 2026-06-17T10:05:49Z
arxiv_id: 2606.18208
url: https://huggingface.co/papers/2606.18208
arxiv_url: https://arxiv.org/abs/2606.18208
date: 2026-06-17
---

# Looped World Models

Current world models face a fundamental tension: faithful long-horizon simulation demands deep computation, but deeper models are expensive to deploy and prone to compounding errors. We resolve this by introducing Looped World Models (LoopWM), which are the first looped architectures for world modelling. Our method iteratively refines latent environment states through a parameter-shared transformer block. This yield up to 100x parameter efficiency over conventional approaches with adaptive computation that automatically scales depth to match the complexity of each prediction step. Orthogonal to scaling model size and training data, LoopWM establishes iterative latent depth as a new scaling axis for world simulation, which might significantly push the community forward.
