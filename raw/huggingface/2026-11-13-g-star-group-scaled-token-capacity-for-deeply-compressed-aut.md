---
source: farmer/huggingface
farmed: 2026-11-14T05:10:36.526947+00:00
arxiv_id: 2611.13004
url: https://huggingface.co/papers/2611.13004
arxiv_url: https://arxiv.org/abs/2611.13004
date: 2026-11-13
---

# G-STAR: Group-Scaled Token Capacity for Deeply Compressed Autoregressive Generation

Discrete autoregressive models offer a scalable framework for image generation. However, they face a fundamental trade-off: long token sequences preserve representation quality but slow generation, while aggressive spatial compression reduces representation capacity. Based on product quantization, we show that, under a fixed nominal information budget, group size should scale quadratically with the per-axis spatial compression factor. Building on this principle, we propose GSTAR, a spatial--group co-scaling framework that enables \(32\times\) and even effective \(64\times\) compression while preserving strong reconstruction, understanding, and generation performance. Since larger groups introduce intra-group dependencies that must be modeled efficiently, we analyze their impact on inference latency and generation quality and introduce a semi-autoregressive decoder that combines parallel feature computation with lightweight causal modeling. With these designs, our highly compressed models perform competitively with leading models across five representative text-to-image benchmarks (GenEval, DPG-Bench, PRISM, LongText-Bench, and Qwen-Image-Bench). At \(1024\times1024\) resolution, our model delivers a \(20\times\) speedup over prior discrete autoregressive models, generating each image in 2.5 seconds on a single NVIDIA H200. Together, these results show that highly compressed discrete representations can enable high-quality autoregressive generation at low latency.
