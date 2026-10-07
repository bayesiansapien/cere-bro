---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2605.16817
url: https://huggingface.co/papers/2605.16817
arxiv_url: https://arxiv.org/abs/2605.16817
date: 2026-10-06
---

# Adaptive Fused Prior Transfer for Controllable Generative Image Compression

Learned image compression achieves competitive rate-distortion performance, but very-low-bitrate reconstruction remains challenging because the transmitted representation cannot preserve fine textures and local structures. Perceptual and generative codecs synthesize missing details using reconstruction priors, while controllable codecs allow one model to cover different bitrate and reconstruction preferences. However, existing codebook-based controllable designs generally rely on single-codebook reconstruction priors. We propose Adaptive Fused Prior Transfer for Controllable Generative Image Compression (AFP-GIC), a controllable codec that transfers an adaptive fused prior from a frozen pretrained AdaCode model. Encoder-side fused-prior features guide latent formation, while the decoder predicts a compatible fused prior from the compressed representation and selected control variables, enabling prior-guided reconstruction without transmitting the fused prior itself. A motivating analysis shows that better decoder-side fused-prior alignment tightens a reconstruction-error upper bound and that the fused-prior family contains single-codebook choices as special cases. Under the unified benchmark, AFP-GIC achieves 18.1% lower decoder latency and uses 31.10 million (20.5%) fewer inference parameters than DC-VIC. Experiments on Kodak, CLIC2020, and DIV2K show competitive PSNR and SSIM, with the clearest perceptual gains in NIQE scores and very-low-bitrate visual comparisons.
