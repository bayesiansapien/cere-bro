---
source: farmer/huggingface
farmed: 2026-10-31T08:06:35.158683+00:00
arxiv_id: 2610.21143
url: https://huggingface.co/papers/2610.21143
arxiv_url: https://arxiv.org/abs/2610.21143
date: 2026-10-30
---

# CoSTA: Compressed Speech Token Adaptation for Efficient Spoken Dialogue Models

Spoken Dialogue Models (SDMs) typically share a speech-token space for generation and synthesis, leading to long autoregressive sequences and costly inference. Lower-rate speech tokenizers shorten sequences but may introduce compression-quality trade-offs and costly replacement without breaking this coupling. To address this limitation, we propose CoSTA, a compatibility-preserving post-hoc framework that decouples generation and synthesis token spaces while retaining the original speech tokenizer and decoder. CoSTA extends the generation token space with compressed representations via mean-initialized vocabulary extension, pronunciation adaptation, and dialogue adaptation, followed by deterministic expansion back to the original speech-token space before synthesis. On bilingual speech-dialogue benchmarks, CoSTA achieves approximately 1.7times expanded speech-token generation speed, lower full-response latency, and higher throughput while preserving response quality. Analyses show more sustained interaction under limited budgets and a practical trade-off among compression, decoding efficiency, and quality. Further experiments demonstrate cross-architecture transfer and complementarity to low-rate tokenization.
