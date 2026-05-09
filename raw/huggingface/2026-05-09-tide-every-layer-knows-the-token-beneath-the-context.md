---
source: farmer/huggingface
farmed: 2026-05-09T03:37:34Z
arxiv_id: 2605.06216
url: https://huggingface.co/papers/2605.06216
arxiv_url: https://arxiv.org/abs/2605.06216
date: 2026-05-09
---

# TIDE: Every Layer Knows the Token Beneath the Context

We revisit a universally accepted but under-examined design choice in every modern LLM: a token index is looked up once at the input embedding layer and then permanently discarded. This single-injection assumption induces two structural failures: the Rare Token Problem, where rare-token embeddings are chronically under-trained due to a Zipf-type gradient distribution, and the Contextual Collapse Problem, where limited-parameter models map distributionally similar tokens to indistinguishable hidden states. We propose TIDE, which augments the standard transformer with EmbeddingMemory: an ensemble of K lightweight token-specific memory blocks that are injected at every layer.
