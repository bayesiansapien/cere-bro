---
source: farmer/huggingface
farmed: 2026-10-24T12:49:20.887884+00:00
arxiv_id: 2610.26252
url: https://huggingface.co/papers/2610.26252
arxiv_url: https://arxiv.org/abs/2610.26252
date: 2026-10-23
---

# SEAM: Spectral Embedding Alignment and Merging for Low-Resource TTS

Expanding the vocabulary of conditional text-to-speech (TTS) models typically requires extensive fine-tuning with paired audio, creating a major bottleneck for low-resource and cross-lingual adaptation. To address this, we introduce SEAM, a zero-audio initialization method that constructs embeddings for unseen tokens from known subtokens. Unlike standard pooling strategies that ignore sequential structure, SEAM applies a spectral filter to preserve temporal phonetic order and uses closed-form ridge regression to align the new embeddings with the pretrained conditioning manifold. Across three languages and two TTS architectures, SEAM approaches or matches baseline performance using up to four times less training data, reducing sample complexity by 75\% compared to random initialization and mean pooling. Our approach provides a lightweight, reproducible, and theoretically grounded solution for vocabulary expansion in low-resource speech synthesis.
