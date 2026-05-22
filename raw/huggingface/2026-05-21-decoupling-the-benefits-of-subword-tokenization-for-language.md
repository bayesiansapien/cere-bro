---
source: farmer/huggingface
farmed: 2026-05-22T10:21:55.060746+00:00
arxiv_id: 2604.27263
url: https://huggingface.co/papers/2604.27263
arxiv_url: https://arxiv.org/abs/2604.27263
date: 2026-05-21
---

# Decoupling the Benefits of Subword Tokenization for Language Model Training via Byte-level Simulation

Subword tokenization is an essential part of modern large language models (LLMs), yet its specific contributions to training efficiency and model performance remain poorly understood. In this work, we decouple the effects of subword tokenization by isolating them within a controlled byte-level pretraining pipeline. We formulate and test hypotheses across various dimensions, including sample throughput, vocabulary scaling, and the linguistic prior of subword boundaries. By simulating these effects in a byte-level setting, we refine our understanding of why subword models outperform raw byte models and offer insights to improve the pretraining of future byte-level and subword models. Specifically, our experiments highlight the critical role of increased training throughput and the integration of subword boundaries as either explicit priors or inductive biases.
