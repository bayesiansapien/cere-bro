---
source: farmer/huggingface
farmed: 2026-06-16T00:00:00Z
arxiv_id: 2606.16396
url: https://huggingface.co/papers/2606.16396
arxiv_url: https://arxiv.org/abs/2606.16396
date: 2026-06-16
---

# SP^3: Spherical Priors for Plug-and-Play Restoration

In this paper, we introduce SP^3, a novel Plug-and-Play algorithm that accelerates maximum a posteriori image restoration by replacing denoisers with Spherical Encoders (SE) as generative priors. SP^3 approximates the intractable proximal prior step by utilizing the SE tightly structured latent space as a robust projection onto the natural image manifold. Alternating this projection with a closed-form data-consistency step, via Half-Quadratic Splitting, achieves stable convergence without requiring gradient computation during inference. This unique formulation unlocks anytime restoration capabilities, producing sharp, plausible images from the first iteration. Evaluations across a variety of image restoration tasks demonstrate that SP^3 achieves perceptual quality comparable to state-of-the-art zero-shot diffusion and flow methods while being 3-630x faster.
