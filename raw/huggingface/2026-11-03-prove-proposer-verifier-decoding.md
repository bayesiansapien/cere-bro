---
source: farmer/huggingface
farmed: 2026-11-04T11:17:37.426675+00:00
arxiv_id: 2610.27815
url: https://huggingface.co/papers/2610.27815
arxiv_url: https://arxiv.org/abs/2610.27815
date: 2026-11-03
---

# ProVe: Proposer-Verifier Decoding

Speculative decoding accelerates autoregressive (AR) language models by letting a small model draft tokens serially and a large model verify them in parallel. We reverse these roles. Starting from a standard AR checkpoint, we fine-tune the large model into a proposer that predicts a block of future tokens in a single forward pass, then use one additional forward pass to verify the proposed block. This gives ProVe, Proposer-Verifier decoding. The verifier can be a smaller AR model or the proposer itself; the latter gives ProVe-lossless, which reproduces the proposer's greedy AR decoding. Block proposals already provide substantial room for acceleration: with a block size of 16, the proposed block has an average AR-matching prefix of 6.6 tokens on GSM8K. Across six benchmarks with a 32B proposer, ProVe-lossless reaches 2.5x average AR throughput without training a separate draft head. With a small 3B verifier, ProVe reaches 2.7x average throughput at 2.6 accuracy points below AR on the six-task average, providing a controllable tradeoff between speed and accuracy.
