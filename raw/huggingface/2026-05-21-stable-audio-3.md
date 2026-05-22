---
source: farmer/huggingface
farmed: 2026-05-22T10:21:55.060746+00:00
arxiv_id: 2605.17991
url: https://huggingface.co/papers/2605.17991
arxiv_url: https://arxiv.org/abs/2605.17991
date: 2026-05-21
---

# Stable Audio 3

Stable Audio 3 is a family of fast latent diffusion models (small, medium, large) for variable-length audio generation and editing. Since our models can generate several minutes of audio, variable-length generations are key to avoid the cost of producing full-length generations for short sounds. We also support inpainting, enabling targeted audio editing and the continuation of short recordings. Our latent diffusion models operate on top of a novel semantic-acoustic autoencoder that projects audio into a compact latent space, enabling efficient diffusion-based generation while preserving audio fidelity and encouraging semantic structure in the latent. Finally, we run adversarial post-training to both accelerate inference and improve generation quality, reducing the number of inference steps while improving fidelity and prompt adherence. Stable Audio 3 models are trained on licensed and Creative Commons data to generate music and sounds in less than a 2s on an H200 GPU and less than a few seconds on a MacBook Pro M4. We release the weights of small and medium, that can run on consumer-grade hardware, together with their training and inference pipeline.
