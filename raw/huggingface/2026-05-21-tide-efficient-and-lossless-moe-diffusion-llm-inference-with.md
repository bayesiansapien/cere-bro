---
source: farmer/huggingface
farmed: 2026-05-22T10:21:55.060746+00:00
arxiv_id: 2605.20179
url: https://huggingface.co/papers/2605.20179
arxiv_url: https://arxiv.org/abs/2605.20179
date: 2026-05-21
---

# TIDE: Efficient and Lossless MoE Diffusion LLM Inference with I/O-aware Expert Offload

Diffusion Large Language Models (dLLMs) have emerged as a competitive alternative to autoregressive (AR) models, offering better hardware utilization and bidirectional context through parallel block-level decoding. However, as dLLMs continue to scale up with mixture-of-experts (MoE) architectures, their deployment on resource-constrained devices remains an open challenge. Existing AR-based methods often incur either prohibitive I/O overhead or significant compute bottlenecks. In this work, we propose TIDE, a novel resource-efficient inference system that leverages the temporal stability of expert activations during the diffusion process within the block. Specifically, we leverage the temporal stability of expert activations during the diffusion process within the block and introduce an interval-based expert refresh strategy that updates the expert placement in an I/O-aware fashion. To ensure optimal performance, we formulate the inference scheduling as a mathematical programming problem, solving for the optimal interval that minimizes I/O traffic and CPU computation. Most importantly, TIDE is a lossless optimization that requires no model training, providing a "free lunch" acceleration for dLLM inference. In a single GPU-CPU system, we demonstrate that TIDE achieves up to 1.4times and 1.5times throughput improvements over prior baselines on LLaDA2.0-mini and LLaDA2.0-flash models, respectively.
