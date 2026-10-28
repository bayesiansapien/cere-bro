---
source: farmer/huggingface
farmed: 2026-10-28T10:37:11+05:30
arxiv_id: 2610.23928
url: https://huggingface.co/papers/2610.23928
arxiv_url: https://arxiv.org/abs/2610.23928
date: 2026-10-27
---

# miniTE: Diagnosing and Bridging the Execution Gap in Native NVFP4 Reinforcement Learning

Native NVFP4 promises to accelerate reinforcement learning (RL) for large language models (LLMs), but achieving stable learning across separate training and sampling engines remains challenging. We show that matching model weights and numerical formats is insufficient to ensure consistent policy evaluation, highlighting the importance of cross-engine numerical execution. We introduce miniTE, a lightweight framework that combines execution diagnostics, cross-engine numerical alignment, and efficient native W4A4 (4-bit weights and activations) GEMM computation for LLM RL. It improves numerical execution consistency without modifying the RL objective, while reducing implementation overhead to realize the benefits of native low-bit computation. Long-horizon RL experiments on Qwen3-30B-A3B demonstrate stable training and benchmark performance close to BF16, outperforming naive Transformer Engine (TE) NVFP4 in evaluation quality. On single NVIDIA B300 GPU node, the optimized learner reaches 33,540 tokens/s, yielding 1.39x and 1.47x the throughput of BF16 and TE NVFP4, respectively, for complete learner updates. We released the framework, kernels, diagnostics, and training configurations to make native low-bit RL easier.
