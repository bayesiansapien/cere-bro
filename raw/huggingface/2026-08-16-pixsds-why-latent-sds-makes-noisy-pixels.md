---
source: farmer/huggingface
farmed: 2026-08-16T13:39:51.900697+05:30
arxiv_id: 2608.12997
url: https://huggingface.co/papers/2608.12997
arxiv_url: https://arxiv.org/abs/2608.12997
date: 2026-08-16
---

# PixSDS: Why Latent SDS Makes Noisy Pixels

Score Distillation Sampling (SDS) enables text-to-3D generation by optimizing rendered images with a pretrained diffusion prior, but latent SDS often produces structured color artifacts and high-frequency texture noise. We identify a failure mode of latent SDS caused by VAE-induced pixel drift: the optimized image can move along pixel-space directions that are weakly constrained by the VAE encoder, so its latent representation remains clean and semantically meaningful while the image itself accumulates visible artifacts. We support this diagnosis with controlled 2D SDS experiments, VAE-only optimization, and a simplified analysis showing that encoder-like latent objectives can amplify image-space noise when the inverse mapping to pixels is underconstrained. Motivated by this observation, we propose PixSDS, a lightweight VAE-consistent gradient repair method. PixSDS decodes a latent SDS lookahead step and uses the decoded image as a clean direction for pixel-space optimization, reducing motion in VAE-inconsistent directions without retraining the diffusion model, changing the renderer, or replacing the SDS objective. Experiments in 2D optimization and text-to-3D generation show that PixSDS substantially reduces structured artifacts while preserving semantic content. Code is publicly available at https://sevashasla.github.io/pixsds-webpage/.
