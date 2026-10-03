---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.818257+00:00
arxiv_id: 2609.37533
url: https://huggingface.co/papers/2609.37533
arxiv_url: https://arxiv.org/abs/2609.37533
date: 2026-10-02
---

# E-MoE: Enhanced Mixture-of-Experts for Non-Factorized Diffusion Language Models

Masked diffusion models (MDMs) generate sequences by progressively unmasking several tokens per denoising step, but their reverse process is typically factorized over positions, limiting sample quality in the few-step regime where diffusion's speed advantage over autoregressive decoding matters most. A recent line of work introduces a continuous Gaussian latent, trained as a variational autoencoder, to capture correlations across positions, but such approaches are prone to posterior collapse, where the latent is silently ignored. We propose Enhanced Mixture-of-Experts (E-MoE), which builds the reverse process as a mixture of factorized distributions over a discrete shared latent given by the expert-routing decisions of a Mixture-of-Experts (MoE) backbone, without increasing active parameters over the factorized baseline. Across synthetic multi-modal benchmarks, binarized MNIST, and LM1B, E-MoE improves few-step generation over factorized baselines.
