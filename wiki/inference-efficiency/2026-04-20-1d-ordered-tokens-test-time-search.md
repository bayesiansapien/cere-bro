---
date: 2026-04-20
source: raw/huggingface/2026-04-20-1d-ordered-tokens-enable-efficient-test-time-search.md
arxiv: https://arxiv.org/abs/2604.15453
tier: 2 — Inference Efficiency / Test-Time Scaling
---

# 1D Ordered Tokens Enable Efficient Test-Time Search

## TL;DR

Coarse-to-fine 1D token ordering outperforms classical 2D grid tokenization for test-time search in autoregressive image generation. Intermediate states in a coarse-to-fine sequence carry semantic meaning that verifiers can evaluate; 2D grid intermediate states do not. Key insight: token structure determines how well test-time search can steer generation, independently of model capability.

## Key Findings

**The hypothesis:** 1D ordered (coarse-to-fine) tokenizers produce intermediate generation states that are semantically meaningful — a verifier can tell if the generation is heading in the right direction after seeing 20% of tokens. 2D grid tokenizers produce intermediate states that are spatially incomplete patches — not semantically interpretable at any prefix.

**Controlled experiment:** Identical AR models trained on (a) coarse-to-fine 1D tokens vs. (b) standard 2D grid tokens, evaluated under best-of-N, beam search, and lookahead search. 1D tokens consistently improve under all three search algorithms; 2D tokens show minimal benefit from search.

**Training-free text-to-image generation:** Because 1D ordered structure makes token sequences searchable without training, pure test-time search (no trained AR model) can generate images guided by an image-text verifier. This is genuinely novel — inference-time compute substituting for training-time compute.

**Practical guidance:** The paper systematically studies how AR prior quality, verifier quality, and token structure interact. Better AR priors help; better verifiers help; but token structure is the prerequisite — you can't search effectively without semantically evaluable intermediate states.

## Connection to Test-Time Scaling Debate

This paper contributes a different perspective to the inference-time scaling discussion that started with AIMO 3 (04-17).

AIMO 3: model capability is 4x more important than prompt-level optimization; diversity doesn't close the pass@20 gap.
VGF (04-19): transport-step refinement as alternative to wider sampling.
STOP (04-20): path pruning at the prefix level.
1D Tokens (04-20): token structure determines whether search is *possible* at all.

These aren't competing — they operate at different levels. 1D tokens is a prerequisite: without searchable intermediate states, STOP and VGF-style refinement have nothing to work with.

## Relations to Prior Wiki Pages

- **AIMO 3 / model-capability-dominates (04-17)**: AIMO 3 focused on prompting-level diversity. 1D tokens operates at the architecture level (tokenizer design) — the claim is that architectural choices upstream determine inference-time scaling capability downstream.
- **KV Cache**: Coarse-to-fine generation changes the KV cache reuse pattern. Early tokens (coarse) are more reusable across diverse continuations than late tokens (fine). This could intersect with KV Packet (04-17).

## Raw Source

→ [raw/huggingface/2026-04-20-1d-ordered-tokens-enable-efficient-test-time-search.md](../../raw/huggingface/2026-04-20-1d-ordered-tokens-enable-efficient-test-time-search.md)
