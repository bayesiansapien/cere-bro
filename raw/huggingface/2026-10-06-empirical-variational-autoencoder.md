---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.06545
url: https://huggingface.co/papers/2610.06545
arxiv_url: https://arxiv.org/abs/2610.06545
date: 2026-10-06
---

# Empirical Variational Autoencoder

We present Empirical Variational Autoencoder, a general generative framework for continuous-valued (i.e., non-vector-quantized) sequences. EVA is based on the evidence lower bound of the Variational Autoencoder (VAE) but learns autoregressive latent priors empirically from training data, which can be implemented only by an additional single linear layer on top of VAEs. By replacing the conventional standard-Gaussian constraint with the self-predicted priors, EVA significantly alleviates the latent distribution gap between prior and posterior which is typically observed in conventional VAEs, and leads to high-fidelity ancestral sampling for sequential data generation. Extensive experiments on image and sound synthesis demonstrate that EVA achieves competitive generation quality with autoregressive diffusion baselines despite its much faster inference time.
