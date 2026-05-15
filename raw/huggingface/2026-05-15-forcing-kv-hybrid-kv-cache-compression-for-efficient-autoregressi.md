---
source: farmer/huggingface
farmed: 2026-05-15T00:00:00Z
arxiv_id: "2605.09681"
url: https://huggingface.co/papers/2605.09681
arxiv_url: https://arxiv.org/abs/2605.09681
date: 2026-05-15
---

# Forcing-KV: Hybrid KV Cache Compression for Efficient Autoregressive Video Diffusion Models

Autoregressive (AR) video diffusion models adopt a streaming generation framework, enabling long-horizon video generation with real-time responsiveness, as exemplified by the Self Forcing training paradigm. However, existing AR video diffusion models still suffer from significant attention complexity and severe memory overhead due to the redundant key-value (KV) caches across historical frames, which limits scalability. In this paper, we tackle this challenge by introducing KV cache compression into autoregressive video diffusion. We observe that attention heads in mainstream AR diffusion models exhibit markedly distinct attention patterns and functional roles that remain stable across samples and denoising steps. Building on our empirical study of head-wise functional specialization, we divide the attention heads into two categories: static heads, which focus on transitions across autoregressive chunks and intra-frame fidelity, and dynamic heads, which govern inter-frame motion and consistency. We then propose Forcing-KV, a hybrid KV cache compression strategy that performs structured static pruning for static heads and dynamic pruning based on segment-wise similarity for dynamic heads. While maintaining output quality, our method achieves a generation speed of over 29 frames per second on a single NVIDIA H200 GPU along with 30% cache memory reduction, delivering up to 1.35x and 1.50x speedups on LongLive and Self Forcing at 480P resolution, and further scaling to 2.82x speedup at 1080P resolution.
