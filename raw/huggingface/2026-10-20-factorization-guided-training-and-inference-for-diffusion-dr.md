---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.23935
url: https://huggingface.co/papers/2610.23935
arxiv_url: https://arxiv.org/abs/2610.23935
date: 2026-10-20
---

# Factorization-Guided Training and Inference for Diffusion-Drafted Speculative Decoding

Speculative decoding accelerates large language model inference through parallel verification of tokens proposed by a drafter. Diffusion drafters further parallelize proposal generation, but greater proposal capacity or higher mean accepted tokens (MAT) need not yield higher throughput. Because verification accepts only a consecutive prefix, early rejections can render later correct predictions ineffective, limiting MAT gains, while even higher MAT may not improve throughput if per-round latency increases. We introduce DScout, which uses two complementary factorizations to guide diffusion drafter training and inference for higher throughput. For training, DScout factorizes position-wise loss into inclusion, weighting, and prediction loss. This guides the design and combination of mixed-horizon training, intra-block unmasking, and acceptance-weighted loss to align supervision with prefix acceptance and improve MAT. For inference, DScout factorizes throughput as the ratio of MAT to per-round latency, guiding target-conditioning depth, drafter depth, and inference block size selection to identify a high-throughput configuration for each workload. Across six benchmarks, DScout achieves 3.84times and 4.14times mean speedups over autoregressive decoding on Qwen3-4B and Qwen3-8B, respectively, improving mean speedup over the state-of-the-art baseline by 9.1% and 7.1%. Across models and concurrency settings, our inference configuration policy provides up to 9.75% additional mean speedup over DScout's fixed configuration.
