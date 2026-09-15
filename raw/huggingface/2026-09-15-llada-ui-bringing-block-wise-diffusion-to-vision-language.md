---
source: farmer/huggingface
farmed: 2026-09-15T10:58:02.142912
arxiv_id: 2609.13287
url: https://huggingface.co/papers/2609.13287
arxiv_url: https://arxiv.org/abs/2609.13287
date: 2026-09-15
---

# LLaDA-UI: Bringing Block-wise Diffusion to Vision-Language GUI Agents

Diffusion large language models (dLLMs) achieve high decoding efficiency through block-parallel, arbitrary-order generation, making them attractive for latency-sensitive applications. GUI agents represent a natural testbed for this paradigm, as they must repeatedly perceive screen states and emit structured, spatially grounded actions in real time. However, whether dLLMs can be extended into capable multimodal GUI agents while preserving their parallel decoding advantage remains an open question. We present LLaDA-UI, a 16.7B-parameter MoE-based, block-wise diffusion vision-language GUI agent. LLaDA-UI follows a two-stage training pipeline: general multimodal pre-training aligns a native-resolution vision encoder with the LLaDA2.0-mini-base diffusion language backbone, followed by GUI-agent supervised fine-tuning on diverse mobile, desktop, web, and grounding data. Across widely adopted grounding benchmarks and navigation benchmarks spanning multiple platforms, LLaDA-UI substantially outperforms Qwen2.5-VL-7B and surpasses Qwen3-VL-8B on four of six reported GUI benchmarks. These results establish block-wise diffusion as a practical generative paradigm for multimodal GUI agents.
