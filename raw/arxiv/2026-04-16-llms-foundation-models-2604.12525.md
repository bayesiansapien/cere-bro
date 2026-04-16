---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.12525
category: cs.CV
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.12525
published: 2026-04-16
authors: Zhaoyang Jia, Naifu Xue, Zihan Zheng
---

# CoD-Lite: Real-Time Diffusion-Based Generative Image Compression

**arXiv:** https://arxiv.org/abs/2604.12525
**Authors:** Zhaoyang Jia, Naifu Xue, Zihan Zheng

## Abstract

arXiv:2604.12525v2 Announce Type: replace  Abstract: Recent advanced diffusion methods typically derive strong generative priors by scaling diffusion transformers. However, scaling fails to generalize when adapted for real-time compression scenarios that demand lightweight models. In this paper, we explore the design of real-time and lightweight diffusion codecs by addressing two pivotal questions. First, does diffusion pre-training benefit lightweight diffusion codecs? Through systematic analysis, we find that generation-oriented pre-training is less effective at small model scales whereas compression-oriented pre-training yields consistently better performance. Second, are transformers essential? We find that while global attention is crucial for standard generation, lightweight convolutions suffice for compression-oriented diffusion when paired with distillation. Guided by these findings, we establish a one-step lightweight convolution diffusion codec that achieves real-time $60$~FPS encoding and $42$~FPS decoding at 1080p. Further enhanced by distillation and adversarial learning, the proposed codec reduces bitrate by 85\% at a comparable FID to MS-ILLM, bridging the gap between generative compression and practical real-time deployment. Codes are released at https://github.com/microsoft/GenCodec/tree/main/CoD_Lite
