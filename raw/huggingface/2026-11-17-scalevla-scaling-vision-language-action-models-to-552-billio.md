---
source: farmer/huggingface
farmed: 2026-11-18T05:07:04.109105+00:00
arxiv_id: 2611.21607
url: https://huggingface.co/papers/2611.21607
arxiv_url: https://arxiv.org/abs/2611.21607
date: 2026-11-17
---

# ScaleVLA: Scaling Vision-Language-Action Models to 552 Billion Parameters

Frontier Vision-Language Models (VLMs) such as GPT-6 Astra have demonstrated remarkable capabilities in robot control, suggesting that broad pretraining provides knowledge valuable for physical action. Yet most Vision-Language-Action (VLA) policies still rely on much smaller VLM backbones, leaving this potential largely untapped. We ask whether frontier-scale representations can provide a stronger foundation for robot learning. We introduce ScaleVLA, which connects a 552B DeepSeek-V4.1-Flash backbone to a trainable action DiT, and systematically compare VLMs from 2B to 552B under a shared training setup. We evaluate three fundamental capabilities of robot foundation models. In sample efficiency, just 10 demonstrations outperform a 2B backbone trained with 50 (87.8% vs. 85.6%). In generalization, LIBERO-PRO success reaches 45.1%, compared with at most 31.3% for smaller backbones. In precise manipulation, real-world charger insertion improves from 4/10 to 9/10 successes, with gains concentrated in contact-sensitive alignment. Despite its scale, ScaleVLA achieves 216 ms median latency per action chunk. Our findings suggest that frontier VLMs can serve not only as reasoning agents, but also as powerful representational foundations for efficient and generalizable robot policies.
