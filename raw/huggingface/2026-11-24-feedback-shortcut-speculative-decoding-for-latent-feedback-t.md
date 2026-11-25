---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.928134+00:00
arxiv_id: 2611.28227
url: https://huggingface.co/papers/2611.28227
arxiv_url: https://arxiv.org/abs/2611.28227
date: 2026-11-24
---

# Feedback Shortcut: Speculative Decoding for Latent Feedback Transformers

Feeding each position's top-layer hidden state back into the next position's input improves Transformer performance. However, this feedback breaks speculative decoding, since verifying a drafted token requires the top-layer state from its preceding position, which forces the draft to rely on an approximate stand-in. Training the model to adapt to this stand-in can lower the exact-decoding performance ceiling, while using it at inference time further introduces approximation error. We propose Feedback Shortcut to address both bottlenecks. First, state alignment trains a lightweight projection from multi-token prediction head states to stand-ins, leaving base model training untouched. Second, pipelined correction re-evaluates each draft using its predecessor's newly computed state, a much closer proxy to true feedback. Running this correction inside the verification pass of subsequent drafts improves accuracy with zero extra calls. Across 135M and 780M scales, Feedback Shortcut stays within 10^{-4} bits per byte of the exact-decoding ceiling on Paloma and accelerates decoding by 2.4-2.8x with about 2% more training compute than the latent feedback Transformer. At large batch sizes, skipping correction still preserves Transformer speed and over 80% of latent feedback's gains.
