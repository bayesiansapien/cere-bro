---
source: farmer/huggingface
farmed: 2026-10-23T08:19:34.192185+00:00
arxiv_id: 2610.30023
url: https://huggingface.co/papers/2610.30023
arxiv_url: https://arxiv.org/abs/2610.30023
date: 2026-10-22
---

# RealMe: Immersive Volumetric Video from Minimal Captures

This paper addresses the problem of creating immersive volumetric videos from sparse and low-resolution capture resources. Conventional dense multi-view reconstruction methods can produce high-quality volumetric videos, but their reliance on costly capture setups makes them impractical in real-world scenarios. Recent approaches use generative models to relax capture requirements, but still suffer from limited resolution and 4D inconsistency. To overcome these constraints, we propose RealMe, a unified framework built around a high-resolution video diffusion model that enhances limited captures into high-resolution (2K), 4D-consistent videos for volumetric video reconstruction. Specifically, RealMe constructs auxiliary data from capture videos and encodes them into latents along with layout-aware positional embeddings. The video diffusion model adapts factorized spatio-temporal attention to the multi-view capture layout, denoises these latents across viewpoints and time, and decodes them into enhanced videos to refine the 4D representation. This adaptation helps the model capture temporal dynamics and multi-view relationships, leading to more 4D-consistent generation. To reduce the data gap between generated videos and real captures, we apply a latent frequency loss that provides frequency-domain supervision in latent space. Extensive experiments on the public DNA-Rendering benchmark and our self-captured RealVV dataset demonstrate that RealMe is able to create immersive volumetric videos and outperforms state-of-the-art methods in visual fidelity and 4D consistency.
