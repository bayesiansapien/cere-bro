---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.503413+00:00
arxiv_id: 2610.12843
url: https://huggingface.co/papers/2610.12843
arxiv_url: https://arxiv.org/abs/2610.12843
date: 2026-10-14
---

# APEX: Asynchronous Prefix Denoising for Extreme Compression

Fewer latent tokens promise cheaper diffusion. Yet aggressive latent compression creates a reconstruction-generation dilemma: adding channels improves reconstruction but makes generation harder. We introduce APEX, short for Asynchronous Prefix denoising for EXtreme compression, which pairs a hierarchical latent space with asynchronous denoising over channel groups. Our autoencoder orders channel prefixes from structure to detail, while one shared denoiser generates them at staggered local times without adding tokens. On ImageNet-512, APEX outperforms existing methods at every evaluated channel count under 64x and 128x compression. At matched training and guided sampling compute, it also outperforms a 256-token model at every evaluated budget, with larger gains at lower compute. Code is available at https://daviddinkevich.github.io/APEX.
