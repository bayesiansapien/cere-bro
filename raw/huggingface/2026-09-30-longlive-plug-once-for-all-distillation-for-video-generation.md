---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.38154
url: https://huggingface.co/papers/2609.38154
arxiv_url: https://arxiv.org/abs/2609.38154
date: 2026-09-30
---

# LongLive-Plug: Once-for-All Distillation for Video Generation

Video diffusion models are increasingly developed into specialized models for diverse downstream tasks, and this development often includes a distillation stage, for example to accelerate sampling or to improve long-video generation. This stage is typically repeated for every specialized model. We introduce LongLive-Plug, a once-for-all distillation framework that learns reusable capabilities as LoRAs on a base model for training-free, plug-and-play deployment to compatible downstream models. These capabilities include single-pass classifier-free guidance, few-step sampling, and long-context error correction for autoregressive generation. The adapters remain reusable even when downstream models add conditioning branches, expand output channels. Despite training at a fixed guidance scale, our dedicated CFG LoRA provides text guidance control through its inference weight. Combining it with a few-step LoRA simultaneously preserves few-step generation and CFG controllability on downstream tasks. We verify training-free deployment on 54 downstream models across three backbone families and eight task categories, including world modeling, robotics, editing, and multimodal generation. The approach may support additional compatible models. Each capability can thus be distilled once per backbone family and reused without per-target retraining.
