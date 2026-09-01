---
source: farmer/huggingface
farmed: 2026-09-01T08:46:18.970698+00:00
arxiv_id: 2608.29335
url: https://huggingface.co/papers/2608.29335
arxiv_url: https://arxiv.org/abs/2608.29335
date: 2026-09-01
---

# GenFirst: Generation Before Reconstruction for Stable End-to-End Latent Generative Modeling

Latent generative models typically follow a two-stage pipeline, training a variational autoencoder for reconstruction and then a generative model on the frozen latent space. Since reconstruction-optimized latents are not necessarily generation-friendly, jointly training both models is an appealing alternative. However, direct end-to-end training remains challenging, as it is prone to latent collapse and faces a generation-reconstruction conflict. We revisit this problem by analyzing how different objectives shape the latent space and identify two key insights. First, the entropy term in the Kullback-Leibler divergence objective is essential for preventing collapse: reconstruction and prior fitting tend to shrink the posterior, while entropy preserves non-degenerate latent uncertainty. Second, reconstruction and generation exhibit asymmetric learning dynamics: reconstruction is fast and strongly supervised, whereas generation is slower and harder to optimize. Based on these insights, we achieve the first direct end-to-end training without latent collapse and propose GenFirst, a simple generation-before-reconstruction strategy. The generative objective first shapes the latent space under weak reconstruction pressure, after which reconstruction is progressively strengthened to recover visual details. We validate GenFirst with continuous autoregressive priors with exact likelihoods and SiT priors with implicit likelihoods. With our end-to-end objective and GenFirst, SiT achieves a gFID of 0.97 with CFG and 1.45 without CFG on ImageNet-256, while MMDiT reaches a GenEval score of 0.90 on text-to-image generation. Beyond image generation, we extend the framework to shared visual latents for generation and representation learning, and to continuous unified text-image generation. These results demonstrate the generality of stable end-to-end latent learning across generative priors and modalities.
