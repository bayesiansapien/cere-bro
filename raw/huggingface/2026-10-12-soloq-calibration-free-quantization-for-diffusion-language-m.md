---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.217689+05:30
arxiv_id: 2610.07121
url: https://huggingface.co/papers/2610.07121
arxiv_url: https://arxiv.org/abs/2610.07121
date: 2026-10-12
---

# SoloQ: Calibration-Free Quantization for Diffusion Language Models

Diffusion large language models dLLMs) have emerged as a promising alternative to autoregressive language models through bidirectional diffusion-based token generation. However, their growing model sizes and high inference costs make efficient deployment challenging: full-sequence denoising repeatedly invokes compute-intensive forward passes, while block-diffusion models additionally introduce a memory-intensive KV-cache. Low-bit weight-activation quantization is therefore attractive, yet existing dLLM post-training quantization methods rely on calibration data despite activation distributions shifting across masking states and denoising steps. We present SoloQ, a calibration-free quantization framework that maps weights and activations into a normalized rotated basis with a predictable marginal distribution, enabling data-independent quantization. SoloQ combines a structured K-RPBH rotation with a lightweight rescaling correction for calibration-free quantization. Its predictable post-rotation distribution supports both distribution-matched codebooks and hardware-native NVFP4. For block-diffusion models, SoloQ further applies commit-time KV-cache quantization to compress persistent states without perturbing the actively denoised block. Across full-sequence dLLMs (LLaDA and Dream) and block-diffusion dLLMs(Fast-dLLM v2 and Nemotron-Labs-Diffusion), SoloQ retains accuracy under 4-bit quantization and outperforms calibration-based baselines on knowledge- and reasoning-intensive benchmarks. With NVFP4, SoloQ reduces peak memory by up to 2.61X and accelerates end-to-end inference by up to 2.24X.
