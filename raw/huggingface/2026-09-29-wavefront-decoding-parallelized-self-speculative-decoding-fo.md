---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.933083+00:00
arxiv_id: 2609.23033
url: https://huggingface.co/papers/2609.23033
arxiv_url: https://arxiv.org/abs/2609.23033
date: 2026-09-29
---

# WaveFront Decoding: Parallelized Self-Speculative Decoding for Looped Language Models

Looped language models repeatedly apply a weight-shared block to increase effective depth without increasing parameter count, but the resulting T sequential recurrent-block calls per generated token substantially increase decoding latency. To address the issue, we introduce Wavefront Decoding (WFD), a training-free self-speculative decoding framework designed for looped language models. WFD exploits two properties of these architectures: intermediate recurrence outputs provide effective draft predictions, and weight sharing allows token states at different positions and recurrence depths to be processed in one batched recurrent-block call. WFD organizes these mixed-depth states into a diagonal wavefront, continuously drafting new positions at shallow depth while advancing earlier positions toward full-depth verification. Unlike the phase-separated draft-then-verify schedule, WFD therefore concurrently batches drafting and verification within the same recurrent calls, while rejected drafts are corrected using full-depth predictions. Across six Spec-Bench task categories, WFD achieves 2.42x speedup on Ouro-2.6B and 3.54x on Huginn-3.5B over autoregressive decoding, consistently outperforming draft-then-verify. Cross-recurrence KV sharing further reduces wavefront KV traffic and increases WFD's speedup to 4.81x on Huginn-3.5B. The code is available at https://github.com/summerbro-hhj/wavefront-decoding.
