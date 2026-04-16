---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13495
category: cs.CV
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13495
published: 2026-04-16
authors: Juneyong Lee, Geonwoo Baek, Ikbeom Jang
---

# ADP-DiT: Text-Guided Diffusion Transformer for Brain Image Generation in Alzheimer's Disease Progression

**arXiv:** https://arxiv.org/abs/2604.13495
**Authors:** Juneyong Lee, Geonwoo Baek, Ikbeom Jang

## Abstract

arXiv:2604.13495v1 Announce Type: new  Abstract: Alzheimer's disease (AD) progresses heterogeneously across individuals, motivating subject-specific synthesis of follow-up magnetic resonance imaging (MRI) to support progression assessment. While Diffusion Transformers (DiT), an emerging transformer-based diffusion model, offer a scalable backbone for image synthesis, longitudinal AD MRI generation with clinically interpretable control over follow-up time and participant metadata remains underexplored. We present ADP-DiT, an interval-aware, clinically text-conditioned diffusion transformer for longitudinal AD MRI synthesis. ADP-DiT encodes follow-up interval together with multi-domain demographic, diagnostic (CN/MCI/AD), and neuropsychological information as a natural-language prompt, enabling time-specific control beyond coarse diagnostic stages. To inject this conditioning effectively, we use dual text encoders-OpenCLIP for vision-language alignment and T5 for richer clinical-language understanding. Their embeddings are fused into DiT through cross-attention for fine-grained guidance and adaptive layer normalization for global modulation. We further enhance anatomical fidelity by applying rotary positional embeddings to image tokens and performing diffusion in a pre-trained SDXL-VAE latent space to enable efficient high-resolution reconstruction. On 3,321 longitudinal 3T T1-weighted scans from 712 participants (259,038 image slices), ADP-DiT achieves SSIM 0.8739 and PSNR 29.32 dB, improving over a DiT baseline by +0.1087 SSIM and +6.08 dB PSNR while capturing progression-related changes such as ventricular enlargement and shrinking hippocampus. These results suggest that integrating comprehensive, subject-specific clinical conditions with architectures can improve longitudinal AD MRI synthesis.
