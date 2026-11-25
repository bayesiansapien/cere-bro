---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.923091+00:00
arxiv_id: 2611.26358
url: https://huggingface.co/papers/2611.26358
arxiv_url: https://arxiv.org/abs/2611.26358
date: 2026-11-24
---

# Beam Model Technical Report

Beam is a sparse Mixture-of-Experts (MoE) model with 501.3B total parameters and 23.4B active parameters, specifically built and optimized for coding, reasoning, and agentic workloads. Beam delivers frontier level reasoning, while requiring 3-4x less inference compute than many models of its class. Pretrained on 23.8T diverse, curated, high-quality tokens, Beam features a 1M-token context window achieved through a novel two-stage midtraining phase, built on verifiable, correctness-anchored data. Post-training leveraged a large-scale, fully asynchronous reinforcement learning (RL) campaign across 10.5K GB300 GPUs, generating over 100M rollouts over 4 weeks of training. We believe this is one of the largest scale RL runs conducted by any open lab to date. Across our evaluation suite, capabilities continued to improve as we increased RL compute, with no sign of a plateau. Supported by deep hardware-model co-design, FP8/NVFP4 quantization, and a 1.93B-parameter speculative decoding drafter (DFlash 2), Beam maximizes serving throughput with efficient, flexible deployment. Averaged across conversation turns and harm categories, Beam refuses or pivots on 88.9% of harmful requests while complying with 81.5% of harmless requests, achieving the highest refusal/pivot rate on harmful requests among open-weight models on the Pareto frontier.
