---
source: farmer/huggingface
farmed: 2026-11-20T05:04:58.144098+00:00
arxiv_id: 2611.14848
url: https://huggingface.co/papers/2611.14848
arxiv_url: https://arxiv.org/abs/2611.14848
date: 2026-11-19
---

# Tideway: Phase-Aware Tiered Memory Management for MoE Inference on Consumer Devices

Large language model (LLM) agents are rapidly becoming a dominant paradigm for AI applications. Recently, there is a growing demand to deploy large-scale Mixture-of-Experts (MoE) models locally on consumer PCs to balance data privacy, API costs, and inference efficiency. However, unlike datacenter servers with abundant DRAM, consumer devices are tightly constrained in both GPU VRAM and host RAM, forcing massive MoE weights to spill across VRAM, host RAM, and SSD. Under such spilling, we observe that existing systems fail to fully utilize this memory hierarchy, treating the tiers as independent caches and thrashing in inference.
  We present TIDEWAY, a system for efficient inference of large MoE models on memory-constrained consumer devices. Our core insight is to manage host RAM and GPU VRAM as a unified memory pool. Within this pool, TIDEWAY couples phase-aware memory layouts, which adapt to the distinct access patterns of prefill and decode, with an execution engine that optimizes CUDA Graph execution under expert paging. Our evaluations on representative consumer hardware with frontier MoE models demonstrate that TIDEWAY significantly outperforms state-of-the-art systems. On average, TIDEWAY achieves speedups of 1.97x in end-to-end latency and 2.40x in Time-to-First-Token (TTFT), along with 1.61x higher decode throughput against the fastest baseline.
  Our source code is publicly available at https://github.com/Afterglow231/Tideway .
