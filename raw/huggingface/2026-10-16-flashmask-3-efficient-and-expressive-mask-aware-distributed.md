---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.17901
url: https://huggingface.co/papers/2610.17901
arxiv_url: https://arxiv.org/abs/2610.17901
date: 2026-10-16
---

# FlashMask-3: Efficient and Expressive Mask-Aware Distributed Attention

Long-context training of large language and multimodal models couples structured attention masks (document, prefix-LM, share-question, sliding-window, block-sparse) with multi-node context parallelism, making the mask a dominant bottleneck. FlashMask's column-wise sparse mask compresses them from O(n^2) to O(n) via four query-axis boundary vectors, covering broad structured patterns. Implemented for Ampere GPUs, it neither exploits FlashAttention-3's TMA/WGMMA warp-specialized pipeline on Hopper nor supports distribution. The column-wise sparse mask is indexed by key positions but stores query-axis interval boundaries. Under any multi-chunk context-parallel assignment, it reduces per-rank mask localization to a provably zero-communication clip--shift--max on the boundary vectors, compatible with the single-GPU kernel. FlashMask-3 introduces a mask-aware Hopper kernel with three-role warp specialization atop FlashAttention-3's TMA/WGMMA pipeline, plus a mask-aware distributed extension: zero-communication mask localization, a sparsity-aware load balancer (HCC-IPO), and a mask-aware compute-communication overlap with mask-driven communication pruning, whose forward all-gather uses topology-aware hierarchical routing. On a single H100 across 12 masks at 4K--128K context, it improves achieved TFLOPs over FlashMask, FlexAttention, and MagiAttention by 45--141%, 34--71%, and 2--44%. At context-parallel degrees 4--32 with 8K sequence per device, it attains 31--75% compute-communication overlap efficiency and improves throughput over Megatron-Core CP ring, Megatron-Core CP all-gather, and MagiAttention by 1.80times--3.71times, 1.71times--2.92times, and 1.09times--1.46times. In end-to-end training of a 118B-A14B MoE at 128K on 128 H100 GPUs, it raises throughput by 7.3--11.0% over a Dual Chunk all-gather baseline, with attention forward+backward 24.5--44.9% faster.
