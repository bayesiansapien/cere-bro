---
source: farmer/huggingface
farmed: 2026-07-27T13:15:36.767293
arxiv_id: 2607.21848
url: https://huggingface.co/papers/2607.21848
arxiv_url: https://arxiv.org/abs/2607.21848
date: 2026-07-27
---

# Closing the Loop: Training-Free Revisit Consistency for Autoregressive Generative Rendering

Recent conditional video generation models have shown promising potentials to transform 3D engine renderings, such as depth maps and untextured geometry, into photorealistic videos for gaming and immersive content creation. These applications require long-horizon auto-regressive generation that continuously synthesizes new frames while preserving a persistent 3D world. Auto-regressive generators synthesize video chunk by chunk with a bounded KV cache, so when the camera revisits a location after its context has been evicted, the model often regenerates inconsistent appearance, even though the conditioning renderings (e.g., depth) remain perfectly aligned with the underlying geometry.We address this revisit inconsistency without any post-training by exploiting correspondences the 3D engine already provides: temporal correspondence retrieves pose-matched historical latent chunks into the KV cache as loop-closure memory, while spatial correspondence from camera pose and depth reprojection biases token-level attention toward geometrically corresponding regions of the retrieved chunks. We demonstrate our method on loop-closure trajectories mined from TartanAir and TartanGround dataset to mirror complicate real-world application scenarios, where it outperforms existing training-free baselines on revisit consistency without losing overall video quality. Project Page: https://wenchao-m.github.io/ClosetheLoop.github.io/
