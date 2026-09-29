---
source: farmer/huggingface
farmed: 2026-09-29T05:05:53.597473+00:00
arxiv_id: 2601.06352
url: https://huggingface.co/papers/2601.06352
arxiv_url: https://arxiv.org/abs/2601.06352
date: 2026-09-28
---

# CARD: Cluster-level Adaptation with Reward-guided Decoding for Personalized Text Generation

Adapting large language models to individual users remains challenging due to the tension between fine-grained personalization and scalable deployment. We present CARD, a hierarchical framework that achieves effective personalization through progressive refinement. CARD first clusters users according to shared stylistic patterns and learns group-specific LoRA adapters, enabling robust generalization and strong low-resource performance. To capture individual differences within each cluster, we propose an implicit preference learning mechanism that contrasts user-authored text with cluster-level generations, allowing the model to infer user-specific style preferences without manual annotation. At inference time, CARD injects personalization exclusively at decoding via lightweight user preference vectors and low-rank logit corrections, while keeping the base model frozen. Experiments on the LaMP and LongLaMP benchmarks show that CARD achieves superior generation quality compared to baselines, while significantly improving efficiency and scalability for practical personalized text generation.
