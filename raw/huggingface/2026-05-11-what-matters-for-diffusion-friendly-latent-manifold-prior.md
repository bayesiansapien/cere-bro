---
source: farmer/huggingface
farmed: 2026-05-11T00:00:00
arxiv_id: 2605.07915
url: https://huggingface.co/papers/2605.07915
arxiv_url: https://arxiv.org/abs/2605.07915
date: 2026-05-11
---

# What Matters for Diffusion-Friendly Latent Manifold? Prior-Aligned Autoencoders for Latent Diffusion

Tokenizers are a crucial component of latent diffusion models, as they define the latent space in which diffusion models operate. However, existing tokenizers are primarily designed to improve reconstruction fidelity or inherit pretrained representations, leaving unclear what kind of latent space is truly friendly for generative modeling. In this paper, we study this question from the perspective of latent manifold organization. By constructing controlled tokenizer variants, we identify three key properties of a diffusion-friendly latent manifold: coherent spatial structure, local manifold continuity, and global manifold semantics. We find that these properties are more consistent with downstream generation quality than reconstruction fidelity. Motivated by this finding, we propose the Prior-Aligned AutoEncoder (PAE), which explicitly shapes the latent manifold instead of leaving diffusion-friendly manifold to emerge indirectly from reconstruction or inheritance. Specifically, PAE leverages refined priors derived from VFMs and perturbation-based regularization to turn spatial structure, local continuity, and global semantics into explicit training objectives. On ImageNet 256x256, PAE improves both training efficiency and generation quality over existing tokenizers, reaching performance comparable to RAE with up to 13x faster convergence under the same training setup and achieving a new state-of-the-art gFID of 1.03. These results highlight the importance of organizing the latent manifold for latent diffusion models.
