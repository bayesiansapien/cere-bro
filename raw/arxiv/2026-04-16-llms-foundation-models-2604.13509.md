---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13509
category: cs.CV
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13509
published: 2026-04-16
authors: Hengye Lyu, Zisu Li, Yue Hong
---

# DiT as Real-Time Rerenderer: Streaming Video Stylization with Autoregressive Diffusion Transformer

**arXiv:** https://arxiv.org/abs/2604.13509
**Authors:** Hengye Lyu, Zisu Li, Yue Hong

## Abstract

arXiv:2604.13509v1 Announce Type: new  Abstract: Recent advances in video generation models has significantly accelerated video generation and related downstream tasks. Among these, video stylization holds important research value in areas such as immersive applications and artistic creation, attracting widespread attention. However, existing diffusion-based video stylization methods struggle to maintain stability and consistency when processing long videos, and their high computational cost and multi-step denoising make them difficult to apply in practical scenarios. In this work, we propose RTR-DiT (DiT as Real-Time Rerenderer), a steaming video stylization framework built upon Diffusion Transformer. We first fine-tune a bidirectional teacher model on a curated video stylization dataset, supporting both text-guided and reference-guided video stylization tasks, and subsequently distill it into a few-step autoregressive model via post-training with Self Forcing and Distribution Matching Distillation. Furthermore, we propose a reference-preserving KV cache update strategy that not only enables stable and consistent processing of long videos, but also supports real-time switching between text prompts and reference images. Experimental results show that RTR-DiT outperforms existing methods in both text-guided and reference-guided video stylization tasks, in terms of quantitative metrics and visual quality, and demonstrates excellent performance in real-time long video stylization and interactive style-switching applications.
