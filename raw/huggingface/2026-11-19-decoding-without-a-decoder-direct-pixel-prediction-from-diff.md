---
source: farmer/huggingface
farmed: 2026-11-20T05:04:58.143559+00:00
arxiv_id: 2611.22287
url: https://huggingface.co/papers/2611.22287
arxiv_url: https://arxiv.org/abs/2611.22287
date: 2026-11-19
---

# Decoding Without a Decoder: Direct Pixel Prediction from Diffusion Transformers

Latent diffusion models rely on a decoder to map denoised latents to pixels, adding complexity and inference cost. We introduce Decoding Without a Decoder (DWD), which lets a finetuned diffusion transformer produce final pixels directly through a linear head. Unlike previous methods, where the denoising output leads to final pixels, DWD separates the two roles: the original denoising head continues to drive sampling, then the new DWD head predicts the pixels at the final step. We extend pretrained latent models with DWD efficiently by finetuning only the last few transformer blocks, training the DWD head with pixel quality losses while anchoring the denoising head to the pretrained model to preserve the sample trajectory. Across latent image and video generators, DWD removes the decoder and reduces inference cost while maintaining or even improving pixel quality. On Wan video generation, it visibly reduces detail distortion and flickering, lowering warping error by 23%. Remarkably, the same separation also improves pixel diffusion models that do not even use a decoder: a final-step DWD head produces substantially better texture detail in text-to-image generation, and improves ImageNet FID from 1.55 to 1.43, a new state of the art among pixel flow models.
