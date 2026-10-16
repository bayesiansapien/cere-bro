---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.234176+05:30
arxiv_id: 2610.14162
url: https://huggingface.co/papers/2610.14162
arxiv_url: https://arxiv.org/abs/2610.14162
date: 2026-10-15
---

# Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text Generation

Diffusion language models (DLMs) offer parallel sampling for faster generation than autoregressive models, an increasingly important advantage as inference becomes a dominant computational workload. However, DLMs degrade quickly with fewer sampling steps, process the full sequence at every step, and require many passes over the dataset to reach good quality. We introduce Next-Concept Modeling (NCM), a two-stage, coarse-to-fine framework: a multiscale residual VQ-VAE encodes text into a hierarchy of discrete codes, and a transformer generates one level at a time, predicting all codes within a level in parallel. At matched parameter scales, NCM achieves better generative perplexity than the strongest DLM baseline on LM1B while running 21times faster. On OpenWebText, NCM is competitive with the strongest DLM while running 10times faster; on XSum, it matches the strongest DLM's ROUGE-L while being 31times faster. On the reasoning task of Sudoku, NCM outperforms autoregressive and diffusion baselines across all difficulty levels, using fewer function evaluations. On the reasoning task of Sudoku, NCM outperforms autoregressive and diffusion baselines across all difficulty levels, using fewer function evaluations.
