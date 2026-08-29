---
source: farmer/huggingface
farmed: 2026-08-29T05:40:38.746243Z
arxiv_id: 2608.27123
url: https://huggingface.co/papers/2608.27123
arxiv_url: https://arxiv.org/abs/2608.27123
date: 2026-08-28
---

# EditaLive! Unified Character Video Editing for Live Streaming

Conventional video editing primarily focuses on scene-level content, whereas live streaming places greater emphasis on the human subject. However, directly applying existing video-editing methods to human-centric live streaming remains challenging, as they may introduce facial-expression inconsistencies and typically depend on multiple offline inference steps, making them unsuitable for real-time interaction. We propose EditaLive, a novel framework for real-time streaming character video editing. In detail, we start from a pretrained image animation model (Wan-Animate), which naturally decouples appearance from motion, and repurpose it as the base model for instruction-based human-centric video editing by reference frame editing and video reconstruction via the collected CharEdit-50K dataset. Besides, we adapt the model from offline bidirectional to causal streaming generation, and design an aligned self-rollout distillation strategy that compresses the model into a two-step sampler, where fixed RoPE and align forcing reduce training--inference discrepancies, and first-frame preserved sparse attention filters redundant historical information to mitigate appearance drift. Extensive experiments demonstrate that EditaLive delivers state-of-the-art editing performance with faithful preservation of facial expressions and low-latency real-time streaming inference.
