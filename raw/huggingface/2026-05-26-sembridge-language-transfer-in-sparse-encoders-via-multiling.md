---
source: farmer/huggingface
farmed: 2026-05-26T06:42:03Z
arxiv_id: 2605.26002
url: https://huggingface.co/papers/2605.26002
arxiv_url: https://arxiv.org/abs/2605.26002
date: 2026-05-26
---

# SemBridge: Language Transfer in Sparse Encoders via Multilingual Semantic Bridges

Sparse encoders offer high-precision retrieval by representing term importance within a vocabulary space, yet their English-centric structures pose a critical impediment to language transfer for non-English languages. To overcome this structural limitation, we propose SemBridge, a novel embedding initialization method designed for cross-lingual adaptation in sparse encoders by leveraging multilingual bridge models. SemBridge establishes semantic alignments between source and target vocabularies using multilingual dense embeddings as a bridge. Rather than directly relying on all source tokens, SemBridge selects a small set of semantically related source-language tokens and uses them to initialize each target-language token, effectively filtering out semantic noise and reconstructing target tokens as precise linear combinations of core synonyms. This accelerates convergence during fine-tuning and improves training efficiency. Extensive experiments across five languages and four sparse architectures demonstrate that SemBridge achieves superior zero-shot retrieval performance and consistently improves retrieval performance after fine-tuning compared to existing baselines. These results validate SemBridge as a practical solution for deploying high-performance sparse retrieval systems in diverse linguistic environments.
