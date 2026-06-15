---
source: farmer/huggingface
farmed: 2026-06-15T06:21:28Z
arxiv_id: 2606.14694
url: https://huggingface.co/papers/2606.14694
arxiv_url: https://arxiv.org/abs/2606.14694
date: 2026-06-15
---

# AdaSR: Adaptive Streaming Reasoning with Hierarchical Relative Policy Optimization

Large reasoning models typically follow a read-then-think paradigm: they observe the complete input, reason over a static context, and then produce the answer. Yet many real-world scenarios are inherently dynamic, such as audio and video stream, where information arrives as a continuous stream and models must reason, update, and respond under partial observations. Recent streaming reasoning methods allow models to think while reading, but they largely rely on supervised imitation of pre-constructed trajectories, which limits their flexibility. In this paper, we propose AdaSR, an adaptive streaming reasoning framework that enables models to reason during input streaming and perform final deliberation once the stream is complete, learning when to think, and how much computation to allocate across different stages. To optimize this hierarchical reasoning process, we introduce Hierarchical Relative Policy Optimization (HRPO), which decomposes policy optimization into streaming reasoning and deep reasoning phases, providing more fine-grained advantage assignment instead of uniformly distributing a single sequence-level advantage over all tokens. HRPO integrates format, accuracy, and adaptive thinking rewards to enforce valid reasoning protocols, preserve final task performance, and encourage latency-aware computation allocation. Experiments show that AdaSR achieves a better balance among reasoning accuracy, computational efficiency, and streaming latency compared with supervised fine-tuning baseline. We release our code at https://github.com/EIT-NLP/StreamingLLM/tree/main/AdaSR.
