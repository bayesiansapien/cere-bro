---
source: farmer/huggingface
farmed: 2026-05-22T10:21:55.060746+00:00
arxiv_id: 2605.19804
url: https://huggingface.co/papers/2605.19804
arxiv_url: https://arxiv.org/abs/2605.19804
date: 2026-05-21
---

# Stitched Value Model for Diffusion Alignment

For practical use, diffusion- or flow-based generative models must be aligned with task-specific rewards, such as prompt fidelity or aesthetic preference. That alignment is challenging because the reward is defined for clean output images, but the alignment procedure requires value function estimates at noisy intermediate latents. Existing methods resort to Tweedie-style or Monte Carlo approximations, trading off estimator bias against computational cost: Tweedie estimates are efficient but biased, while Monte Carlo estimates are more accurate but require expensive rollouts. A natural alternative would be a learned value function, but it remains an open question how to effectively train a strong and general value model specifically for noisy latents. Here, we propose StitchVM, a model stitching framework that efficiently transfers reward models pretrained for clean images to the noisy latent regime. StitchVM starts from an existing, truncated pixel-space reward model and attaches a frozen diffusion backbone to it as its head. From the pixel-space model, the resulting hybrid retains a carefully pretrained, robust reward capability; from the diffusion backbone, it inherits its native ability to handle noisy latents. The stitching procedure is exceptionally lightweight, e.g., stitching and finetuning CLIP ViT-L and SD 3.5 Medium takes only 10 GPU-hours. By lifting powerful pixel-space reward models to latent space, StitchVM opens up a new style of diffusion alignment: instead of rough, yet costly per-sample approximation of the value function, the correct function for the actual, noisy latents is constructed once and then amortized over many samples and iterations. We show that this approach yields improvements across a broad range of downstream steering and post-training methods: DPS becomes 3.2times faster while halving peak GPU memory, and DiffusionNFT becomes 2.3times faster.
