---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.933835+00:00
arxiv_id: 2609.34754
url: https://huggingface.co/papers/2609.34754
arxiv_url: https://arxiv.org/abs/2609.34754
date: 2026-09-29
---

# Draft-KV: Learning Useful Latent Communication Between Language Models

Latent communication passes internal states between language models instead of decoded text, but higher receiver accuracy does not show that the receiver used the message content. Across five method-dataset pairs, replacing each message with one from an unrelated question changes accuracy by at most 0.60 points, even when communication adds 15.44 points over the receiver alone. Thus the interface can supply the gain while making the sharer dispensable. Draft-KV instead sends the key-value states formed while the sharer drafts an answer to the current question. Linear projections place these states in a side memory read through a gated attention branch, and progressive training moves from message reconstruction to answer supervision under a guard on harm from mismatched messages. Both models remain frozen and the interface trains 1.05M parameters, 348x fewer than C2C. With a Qwen3-8B sharer, a frozen Qwen2.5-0.5B-Instruct receiver reaches 78.04% on MMLU-Redux, versus 37.45% alone and 36.40% with reassigned messages. At fixed interface size, scaling the sharer from 0.6B to 8B raises accuracy from 46.11% to 78.04%; communication also transfers to held-out tasks and can exceed both models when each holds different evidence.
