---
source: farmer/huggingface
farmed: 2026-11-10T05:05:44.203609+00:00
arxiv_id: 2611.01182
url: https://huggingface.co/papers/2611.01182
arxiv_url: https://arxiv.org/abs/2611.01182
date: 2026-11-09
---

# Fast and Exact Relative-Position Attention via Structure-Aware Kernels

Relative-position attention mechanisms offer compelling alternatives to RoPE across various transformer architectures, delivering superior performance in domains such as audio. These mechanisms typically modify attention scores by adding content-position or bias-position terms. Unlike RoPE, which encodes position via per-token rotations directly on the queries and keys, relative-position terms generally require pairwise offset-dependent computation or lookups, complicating their integration into fused attention kernels and introducing severe memory, bandwidth, and compute overheads as sequences scale. To address this bottleneck, we propose an exact attention algorithm that incorporates additive relative-position terms into FlashAttention-style tiled computation. Our method (1) uses offset-aware tiling to avoid redundant indexing and memory accesses, (2) computes only the necessary key/query-relation products and reuses them across token pairs in both forward and backward passes, and (3) uses offset-based gradient sharding and aggregation, eliminating atomic contention. We provide a unified, efficient Triton implementation across diverse relative-position attention mechanisms and evaluate it against naive and specialized implementations. For 8K-token sequences, our method speeds up the forward (backward) pass by 1.8-6.4times (2.0-21times) and reduces peak memory up to 2.9-128times (1.4-54times) over the strongest baseline for each mechanism, enabling long-context end-to-end transcription that is 1.8times faster and uses 2.4times less memory. Our method thus provides a drop-in, hardware-efficient solution for scaling relative-position attention transformers.
