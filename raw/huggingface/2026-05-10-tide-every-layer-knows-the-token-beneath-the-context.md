---
source: farmer/huggingface
farmed: 2026-05-10T03:37:12Z
arxiv_id: 2605.06216
url: https://huggingface.co/papers/2605.06216
arxiv_url: https://arxiv.org/abs/2605.06216
date: 2026-05-10
---

# TIDE: Every Layer Knows the Token Beneath the Context

We revisit a universally accepted but under-examined design choice in every modern LLM: a token index is looked up once at the input embedding layer and then permanently discarded. This single-injection assumption induces two structural failures: (i) the Rare Token Problem, where a Zipf-type distribution of vocabulary causes rare-token embeddings to be chronically under-trained; and (ii) the Contextual Collapse Problem, where limited parameter models map distributionally similar tokens to indistinguishable hidden states. We propose TIDE, which augments the standard transformer with EmbeddingMemory: an ensemble of K independent MemoryBlocks that map token indices to context-free semantic vectors, computed once and injected into every layer through a depth-conditioned softmax router.
