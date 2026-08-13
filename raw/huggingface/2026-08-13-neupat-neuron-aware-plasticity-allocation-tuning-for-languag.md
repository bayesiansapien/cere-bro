---
source: farmer/huggingface
farmed: 2026-08-13T03:36:17.258300+00:00
arxiv_id: 2608.08107
url: https://huggingface.co/papers/2608.08107
arxiv_url: https://arxiv.org/abs/2608.08107
date: 2026-08-13
---

# NeuPAT: Neuron-aware Plasticity Allocation Tuning for Language-Preserving MLLMs

Multimodal expansion of large language models (LLMs) enables new perceptual capabilities but often compromises the language intelligence acquired during pretraining. In this work, we investigate this phenomenon from the perspective of internal adaptation dynamics and discover that neurons in pretrained LLMs exhibit heterogeneous plasticity during multimodal learning: some neurons are critical for preserving language capabilities, while others are more adaptive to multimodal knowledge. Based on this insight, we propose NeuPAT (Neuron-aware Plasticity Allocation Tuning), a lightweight and architecture-agnostic framework that allocates neuron-wise update constraints during multimodal instruction tuning. NeuPAT uses a small-scale probing stage to estimate neuron adaptation patterns and selectively protects language-sensitive neurons while promoting multimodal adaptation through more plastic neurons. Experiments across diverse LLM families demonstrate that NeuPAT recovers 94.5\% of the language capability degradation caused by vanilla tuning on 11 language benchmarks while maintaining comparable multimodal performance, providing an effective approach for capability-preserving multimodal expansion.
