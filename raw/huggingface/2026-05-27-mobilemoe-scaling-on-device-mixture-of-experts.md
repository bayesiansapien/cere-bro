---
source: farmer/huggingface
farmed: 2026-05-27T07:52:03Z
arxiv_id: 2605.27358
url: https://huggingface.co/papers/2605.27358
arxiv_url: https://arxiv.org/abs/2605.27358
date: 2026-05-27
upvotes: 4
---

# MobileMoE: Scaling On-Device Mixture of Experts

Mixture-of-Experts (MoE) has become the de facto architecture for hundred-billion-parameter language models, yet its advantages at sub-billion scales for on-device deployment remain largely unexplored. To close this gap, we present MobileMoE, a family of on-device MoE language models with sub-billion active parameters (0.3-0.9B active and 1.3-5.3B total) that establish a new Pareto frontier for on-device LLMs. We first formulate an on-device MoE scaling law that jointly optimizes MoE architecture under mobile memory and compute constraints, identifying an on-device sweet spot - moderate sparsity with fine-grained and shared experts - that is simultaneously memory and compute-optimal. Building on the derived architectures, we train MobileMoE with a four-stage recipe covering pre-training, mid-training, instruction fine-tuning, and quantization-aware training, all on open-source datasets. Across 14 benchmarks, MobileMoE matches or exceeds leading on-device dense LLMs with 2-4x fewer inference FLOPs, and matches or surpasses the state-of-the-art MoE OLMoE-1B-7B with up to 60% fewer parameters. To bridge the last mile to mobile deployment, we provide the first efficient MoE inference on commodity smartphones with comprehensive on-device profiling. At comparable INT4 weight memory, MobileMoE-S delivers 1.8-3.8x faster prefill and 2.2-3.4x faster decode than the dense baseline MobileLLM-Pro.
