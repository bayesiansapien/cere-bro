---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.229397+05:30
arxiv_id: 2610.18598
url: https://huggingface.co/papers/2610.18598
arxiv_url: https://arxiv.org/abs/2610.18598
date: 2026-10-15
---

# Rethinking Projector Training in Multimodal LLMs

Multimodal LLMs are typically trained by first aligning a vision encoder with a language model via projector training on large image-caption datasets, followed by joint training of the full multimodal model. Despite its widespread use, the role of the projector training stage remains poorly understood. We find that (i) using only 10 to 20% of the data for training the projector already recovers most downstream performance gains, and (ii) projectors trained on different datasets can be linearly interpolated while largely preserving performance. These results suggest that projector training mainly performs a coarse alignment, which many different projectors achieve equally well. Motivated by these findings, we propose PORTAL, a training-free projector initialization that requires neither paired image-caption data nor gradient-based optimization, but only per-modality summary statistics. PORTAL computes an optimal-transport-based map between Gaussian approximations of the vision and language feature distributions on a shared principal subspace, so that the projector training stage can be skipped entirely. Without any paired data, PORTAL matches the standard pipeline trained on 558k image-caption pairs across six LLM backbones, two vision encoders, and 16 benchmarks. It outperforms that pipeline in 3 of 7 (vision encoder, LLM) settings and reaches an average 98% of its score across the other four.
