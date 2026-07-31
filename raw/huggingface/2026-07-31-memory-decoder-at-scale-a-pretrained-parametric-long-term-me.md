---
source: farmer/huggingface
farmed: 2026-07-31T19:58:50.731985
arxiv_id: 2607.27919
url: https://huggingface.co/papers/2607.27919
arxiv_url: https://arxiv.org/abs/2607.27919
date: 2026-07-31
---

# Memory Decoder at Scale: A Pretrained, Parametric Long-Term Memory

Decoder-only language models entangle long-term memory and reasoning in a single parameter set, making it difficult to scale memory capacity independently. Memory Decoder introduces a parametric long-term memory module but only studies it at a relatively small scale. In this work, we present Memory Decoder at Scale, scaling memory models up to 6.9B parameters and pretraining them on 300B tokens. At this data scale, the combined cost of indexing and search makes a standard Faiss pipeline infeasible. We address this bottleneck with a distributed pipeline for Faiss indexing and retrieval, together with sparse, batch-wise loading of kNN distributions. Across model scales, we find that allocating more parameters to memory yields a better parameter-performance tradeoff than scaling the base model alone. On 17 benchmarks, pairing a 6.9B general memory with Pythia-410M raises its average score from 29.86 to 37.34, surpassing Pythia-12B (37.24) with 39% fewer total parameters. For Qwen3 Base models ranging from 0.6B to 14B, 1.7B domain memories improve the average score across the three domains by more than 9 points at every scale. Overall, our results demonstrate that independently scaling pretrained memory offers a more parameter efficient path to improving language model performance.
