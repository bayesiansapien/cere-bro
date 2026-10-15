---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.512767+00:00
arxiv_id: 2610.16172
url: https://huggingface.co/papers/2610.16172
arxiv_url: https://arxiv.org/abs/2610.16172
date: 2026-10-14
---

# EventLens: Event-Structure Reinforcement Learning for Video Understanding

Recent multimodal large language models (MLLMs) achieve strong results on video question answering, yet often fail to recover the temporal structure that makes a video coherent. They may merge neighboring events, miss single-event progression, or infer implausible relations across events. We study structured temporal understanding as the ability to recover event structure from visual evidence, including event boundaries, single-event progression, and multi-event relations. We argue that this gap arises from a mismatch between current post-training objectives and temporal reasoning, where caption-style supervision allows models to rely on language shortcuts rather than visual temporal grounding. To address this, we propose EventLens, a vision-centric reinforcement learning framework that learns video understanding through event-structure recovery. Instead of reconstructing captions, EventLens trains models to recover temporal structure under controlled perturbations, such as altered temporal granularity, reversed progression, and shuffled event order. We instantiate this framework with a three-level temporal ontology and derive three verifiable task families: event segmentation, progression discrimination, and multi-event relation reasoning. These tasks admit deterministic rewards, enabling task-specialized GRPO training without human preference labels or learned reward models. We further introduce multi-teacher on-policy distillation (MT-OPD) to consolidate specialized policies into a unified model. Experiments on Qwen3-VL backbones show consistent improvements on temporal grounding and event-sensitive reasoning benchmarks, while preserving general video-QA performance. Learning curves further demonstrate that EventLens achieves comparable downstream transfer with significantly reduced training cost compared to direct mixed RL optimization.
