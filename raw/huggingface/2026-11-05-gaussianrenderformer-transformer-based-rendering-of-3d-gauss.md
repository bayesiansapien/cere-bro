---
source: farmer/huggingface
farmed: 2026-11-06T05:50:41.306366+00:00
arxiv_id: 2611.05593
url: https://huggingface.co/papers/2611.05593
arxiv_url: https://arxiv.org/abs/2611.05593
date: 2026-11-05
---

# GaussianRenderFormer: Transformer-based Rendering of 3D Gaussian Splats

Can a neural network learn to render 3D Gaussian splats on its own, with no rasterizer in the renderer? We present GaussianRenderFormer, a transformer that takes a set of Gaussians and a camera and outputs the image directly. Each Gaussian becomes one token in a view-independent encoder, and a view-dependent decoder turns small patches of camera rays into pixels by attending to those tokens. Trained on 26,820 Objaverse objects pruned to 20,000 Gaussians each, GaussianRenderFormer renders 300 unseen objects at 38.08 dB PSNR against the full, unpruned splats, while rasterizing the same pruned input reaches 44.02 dB. The gap is not one of generalization, and our diagnostics are consistent with a bottleneck in the view decoder: telling it the projected footprint of each Gaussian, which it could in principle infer, adds 1.4 dB. Under-training is not ruled out. Code, trained models and videos: https://svlwoof.github.io/gaussianrenderformer
