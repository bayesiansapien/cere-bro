---
source: farmer/huggingface
farmed: 2026-05-25T08:23:16Z
arxiv_id: 2605.23902
url: https://huggingface.co/papers/2605.23902
arxiv_url: https://arxiv.org/abs/2605.23902
date: 2026-05-25
---

# PiD: Fast and High-Resolution Latent Decoding with Pixel Diffusion

Most practical high-resolution text-to-image systems, including latent diffusion and autoregressive models, perform generation in a compact latent space, and a decoder maps the generated latents back to pixels. Yet the latent-to-pixel decoder is reconstruction-oriented, optimized to invert the encoder rather than synthesize more details, and becomes increasingly costly at megapixel scale. This drawback calls for a more expressive and efficient decoding paradigm. Motivated by recent progress in scalable pixel-space diffusion, we introduce PiD, a Pixel diffusion Decoder that reformulates latent decoding as conditional pixel diffusion, unifying decoding and upsampling into one generative module. By denoising directly in high-resolution pixel space, PiD synthesizes 4times and even 8times upscaled images with low latency. For latent conditioning, a lightweight sigma-aware adapter injects noise-corrupted latents into the pixel diffusion backbone, enabling PiD to decode partially denoised latents and terminate the latent diffusion process early. To further improve efficiency, we distill the model using DMD2, reducing inference to just 4 steps. PiD applies to both conventional VAE latents and semantic latents (e.g., SigLIP, DINOv2) used in recent RAE-based models. PiD decodes latents of 512 times 512 images into 2048 times 2048 pixels in under 1 second with 13 GB peak memory on a consumer RTX 5090, and as fast as 210 ms on a GB200 GPU, about 6times faster than cascaded diffusion-based super-resolution pipelines with better visual fidelity.
