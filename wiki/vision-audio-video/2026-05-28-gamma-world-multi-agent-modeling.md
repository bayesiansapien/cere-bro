# Gamma-World: Generative Multi-Agent World Modeling Beyond Two Players

**Date ingested:** 2026-05-28
**Source:** HuggingFace Daily Papers
**Links:** [arxiv 2605.28816](https://arxiv.org/abs/2605.28816) · [HuggingFace](https://huggingface.co/papers/2605.28816) · [raw](../../raw/huggingface/2026-05-28-gamma-world-generative-multi-agent-world-modeling-beyond-two.md)

## TL;DR

Interactive world models so far have mostly handled one or two agents. Gamma-World pushes to many. Two design moves do most of the work: Simplex Rotary Agent Encoding (SRAE), a parameter-free extension of 3D RoPE that places each agent at a vertex of a regular simplex in rotary-angle space, giving each a distinct phase while keeping all agents permutation-equivalent and allowing scalable agent identity without learned slot embeddings; and Sparse Hub Attention, where a small set of learnable hub tokens mediate cross-agent interactions so attention cost goes from quadratic to linear in agent count. For real-time rollout, the full-context diffusion teacher is distilled into a causal student that generates temporal blocks sequentially with KV caching, running at 24 FPS. The model improves video fidelity, action controllability, and inter-agent consistency over slot-based and dense-attention baselines, and generalizes from two to four players without retraining.

```
Cross-agent attention cost:
  Dense all-to-all:    O(N²) — quadratic in agent count, doesn't scale
  Sparse hub:          O(N)  — learnable hub tokens mediate
                       ●─┐ ┌─●
                          └●┘   ← hub token
                       ●─┘ └─●

Agent identity:
  Slot embedding:      learned per-agent — breaks permutation symmetry
  SRAE:                each agent → simplex vertex in rotary phase
                       parameter-free, permutation-equivalent, scales
```

## Key findings

- SRAE makes agent identity scalable and permutation-symmetric without per-slot learned embeddings.
- Sparse Hub Attention reduces cross-agent attention from O(N²) to O(N).
- The dense-teacher → causal-student distillation runs at 24 FPS with KV caching.
- Generalizes from two-player to four-player at inference without retraining.
- Improves on slot-based and dense-attention baselines on video fidelity, controllability, and inter-agent consistency.

## How this fits prior wiki state

The Sparse Hub Attention idea is the same architectural pattern as MISA (mixture-of-indexer sparse attention, 2026-05-11) and the broader "token-mediated cross-stream attention" line: bottleneck tokens carry the cross-stream signal instead of dense pairwise mixing. SRAE is a parameter-free identity-encoding trick that fits with the wiki's growing collection of RoPE extensions and is conceptually adjacent to the simplex-tied positional encodings that show up in equivariant networks.

## Related pages

- [[2026-05-11-misa-mixture-of-indexer-sparse-attention]] — sparse attention mediated by indexer tokens
- [[2026-05-22-worldkv-world-memory-retrieval-compression]] — world model KV compression
- [[2026-05-19-longlive-2-nvfp4-parallel-infrastructure-long-video]] — long-video parallel infrastructure

## Research angle

The four-player generalization without retraining is the strongest claim and deserves stress-testing at higher N. If a model trained at two agents really does generalize to four via permutation-symmetric encoding, then the practical ceiling on simulation-rich world models is much higher than expected. SRAE may be the more transferable contribution: it could plug into any agent-conditioned world model and into multi-stream long-context models (multi-camera, multi-document) without architectural changes.
