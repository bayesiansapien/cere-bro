---
source: farmer/huggingface
farmed: 2026-05-11T00:00:00
arxiv_id: 2605.08078
url: https://huggingface.co/papers/2605.08078
arxiv_url: https://arxiv.org/abs/2605.08078
date: 2026-05-11
---

# Normalizing Trajectory Models

Diffusion-based models decompose sampling into many small Gaussian denoising steps - an assumption that breaks down when generation is compressed to a few coarse transitions. Existing few-step methods address this through distillation, consistency training, or adversarial objectives, but sacrifice the likelihood framework in the process. We introduce Normalizing Trajectory Models (NTM), which models each reverse step as an expressive conditional normalizing flow with exact likelihood training. Architecturally, NTM combines shallow invertible blocks within each step with a deep parallel predictor across the trajectory, forming an end-to-end network trainable from scratch or initializable from pretrained flow-matching models. Its exact trajectory likelihood further enables self-distillation: a lightweight denoiser trained on the model's own score produces high-quality samples in four steps. On text-to-image benchmarks, NTM matches or outperforms strong image generation baselines in just four sampling steps while uniquely retaining exact likelihood over the generative trajectory.
