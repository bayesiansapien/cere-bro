---
source: farmer/huggingface
farmed: 2026-11-18T05:07:04.114545+00:00
arxiv_id: 2611.19649
url: https://huggingface.co/papers/2611.19649
arxiv_url: https://arxiv.org/abs/2611.19649
date: 2026-11-17
---

# LoopFill: Pipelined Multi-Token Speculative Decoding for Looped Transformers

Looped Transformers improve parameter efficiency by repeatedly applying the same Transformer layers. During autoregressive decoding, however, generating each token requires several sequential passes through these layers, leading to high decoding latency. Pipelined self-speculative methods use shallow-loop predictions to process tokens at different loops in the same batch, but each token must reach the drafting depth before the next can enter the pipeline. We introduce LoopFill, a training-free speculative decoding algorithm for looped LLM that combines multi-token suffix drafts with shallow-loop predictions in a single draft tree. Both drafters contribute to one tree, so a suffix lookup can immediately extend a shallow prediction and several future tokens can enter the pipeline together. The shared block computes the highest-scoring draft candidates at different loop depths in one batch, and full-depth verification preserves the model's autoregressive output distribution. Across seven benchmarks, LoopFill's average speedup over greedy autoregressive decoding is 5.85times on Ouro-2.6B and 5.13times on Huginn-3.5B. The speedups exceed those of LoopAhead, the strongest baseline, by \(40\%\) on Ouro-2.6B and \(25\%\) on Huginn-3.5B.
