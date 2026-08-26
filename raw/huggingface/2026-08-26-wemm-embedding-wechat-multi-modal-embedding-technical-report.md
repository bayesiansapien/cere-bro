---
source: farmer/huggingface
farmed: 2026-08-26T12:46:47.908232
arxiv_id: 2608.24053
url: https://huggingface.co/papers/2608.24053
arxiv_url: https://arxiv.org/abs/2608.24053
date: 2026-08-26
upvotes: 43
---

# WeMM-Embedding: WeChat Multi-Modal Embedding Technical Report

Universal multimodal embeddings are becoming a core component of modern AI systems, enabling heterogeneous content to be represented in a shared space for applications such as retrieval, recommendation, classification, and agentic systems. In this report, we present WeMM-Embedding, a family of universal multimodal embedding models supporting text, images, videos, visual documents, and arbitrarily interleaved multimodal inputs with flexible output dimensions. The family comprises 2B, 4B, and 9B variants and is trained in two stages: a large-scale multimodal alignment stage, followed by a refinement stage using curated data, fine-grained relevance supervision, and cross-scale knowledge transfer. Across extensive evaluations, WeMM-Embedding achieves leading performance on multiple public benchmarks. Notably, the 2B variant already surpasses the previously leading 8B open-source baseline on MMEB-v2, while the 9B variant further achieves a new state-of-the-art overall score of 80.6. WeMM-Embedding also demonstrates strong practical performance across WeChat applications, with substantial gains on a 26-task in-house benchmark and consistent improvements across 14 online A/B tests. It has been deployed at scale across recommendation and search applications, including WeChat Channels, Official Accounts, Moments, and e-commerce services. We have released the model weights and code to facilitate future research at https://github.com/Tencent/WeMM-Embedding.
