---
source: farmer/huggingface
farmed: 2026-08-05T09:04:08.705882+00:00
arxiv_id: 2608.03457
url: https://huggingface.co/papers/2608.03457
arxiv_url: https://arxiv.org/abs/2608.03457
date: 2026-08-05
---

# LLaDA MoE v2: Scaling Mixture-of-Experts Diffusion Language Models

Diffusion language models (dLLMs) offer an alternative to autoregressive (AR) language modeling, yet the scaling behavior of Mixture-of-Experts (MoE) dLLMs remains poorly understood. We systematically characterize how optimization hyperparameters, compute allocation, and architecture scale for MoE dLLMs, identifying quantitative differences from scaling trends previously reported for AR models. Specifically, for optimization, the optimal nominal batch size grows faster, while the optimal learning rate decays more rapidly with compute. For model--data allocation, IsoFLOP analysis reveals a slight data-side tilt: the optimal token budget grows faster than activated model-side computation. For MoE architecture, larger scales increasingly favor larger expert pools at fixed activated capacity, while moderate expert granularity remains consistently effective and the preferred fraction of activated capacity assigned to shared experts remains stable across scales. Guided by these findings, we train LLaDA MoE v2, a 30B-A3B dLLM, from scratch on 23.5T tokens. With approximately 65\% as many pretraining tokens as Qwen3, LLaDA MoE v2 approaches Qwen3 on several knowledge, reasoning, and coding benchmarks. After supervised fine-tuning alone, it outperforms SDAR Chat on seven of eight reasoning and coding benchmarks and remains close to Qwen3 on several tasks. These results establish practical scaling laws and design principles for MoE dLLMs.
