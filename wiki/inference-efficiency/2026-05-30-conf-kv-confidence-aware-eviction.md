# Conf-KV: Confidence-Aware KV Cache Eviction with Mixed-Precision Storage

**Source:** HuggingFace Daily Papers (2026-05-30) · arxiv 2605.24786
**Raw:** [raw/huggingface/2026-05-30-conf-kv-confidence-aware-kv-cache-eviction-with-mixed-precis.md](../../raw/huggingface/2026-05-30-conf-kv-confidence-aware-kv-cache-eviction-with-mixed-precis.md)

## TL;DR

Conf-KV uses the model's own next-token confidence to dynamically set the KV-cache eviction budget at every decoding step. When the next-token distribution is uncertain, the cache holds more context. When the model is confident, it prunes aggressively. Within each budget, tokens are ranked by accumulated attention mass plus recency, a protected recent window preserves local coherence, and storage is FP16 for the active set with INT8 for evicted-but-kept entries. On Needle-in-a-Haystack at 32K tokens, retrieval reaches 91.4% versus 53.8% for a fixed 512-token sliding window and 80.6% for H2O. VisualWebArena retains 95.3% of full-KV success at 2.8x lower peak memory. The new axis is uncertainty-driven budget allocation, where prior eviction policies all used static or attention-history signals only.

## Architecture

```
At each decoding step t:

  next-token distribution ──► confidence c_t (1 - entropy / ln V)
                                    │
                                    ▼
                          per-step cache budget B_t
                          (low c_t → large B_t;  high c_t → small B_t)
                                    │
                                    ▼
            ┌──────────────── ranking inside B_t ────────────────┐
            │  score = α·accumulated_attention + β·recency       │
            │  PROTECTED: last W tokens always kept              │
            │  ACTIVE set: FP16          EVICTED tail: INT8      │
            └────────────────────────────────────────────────────┘
                                    │
                                    ▼
              blockwise online-softmax attention over kept KV
                  + pyramidal per-layer budget (shallow ≪ deep)
```

## Key claims

- Perplexity within 1.5–2.1 points of full KV across four model families up to 4K generation, at the footprint of a fixed 512-token sliding window.
- Needle-in-a-Haystack @ 32K: **91.4% retrieval** vs 53.8% sliding window vs 80.6% H2O.
- VisualWebArena: **95.3% of full-KV success** at 2.8x lower peak memory.
- Mixed FP16/INT8 storage cuts the active footprint without forcing a single global quantization choice.

## How this composes with the wiki

This is the first KV eviction paper in the wiki to use the *model's own uncertainty* as the budget signal. Prior eviction work in the wiki ranged across:

- **Make Each Token Count (05-12)**, which used a learned, globally calibrated retention gate. Conf-KV is training-free; the signal is read off the next-token distribution.
- **H2O / sliding-window family**, which uses attention history or pure recency. Both signals are *backward-looking*. Conf-KV adds a *forward-looking* signal (confidence about the next token).
- **TurboQuant (04-22)** and **NVFP4 KV** (LongLive-2.0, 05-19) for ultra-low-bit quantization. Conf-KV uses a coarser FP16/INT8 split.
- **WorldKV (05-24)** which kept evicted chunks in a tiered store and retrieved them by scene similarity. Conf-KV keeps a single per-step active set; the retrieval angle is not the focus.
- **KVServe (05-24)** which framed compression as a Bayesian-Pareto control surface. Conf-KV is the per-step decode-time analogue: the budget itself is the control surface.

The thread now has three orthogonal signals for eviction: learned retention (Make-Each-Token-Count), policy-aware role (Forcing-KV), and now confidence-driven budget (Conf-KV). All three argue that the full cache is not the ceiling.

## Gaps and limits

- Tested up to 4K generation and 32K NIH. Behavior at 128K+ context with multi-turn agent runs is not characterized.
- The protected recent window W is a hyperparameter and the paper does not study its sensitivity beyond the headline ablations.
- Mixed FP16/INT8 is a coarse precision policy. Composing with NVFP4 quantization on Blackwell is implied but not tested.

## Research angle

If confidence is a budget signal, the next question is whether it is also a *routing* signal. Two of yesterday's papers (Parallax architecture, Why-Larger-Models capacity) point to gradient and resource competition as the bottleneck. Conf-KV adds a third lens: at decode time, the model knows when it needs more context. If the same confidence signal could drive head-axis routing (MISA-style), full-attention escalation (RTPurbo full-to-sparse), and cache budget jointly, the entire long-context inference stack could be confidence-conditioned.

## Related concept pages

- [KV Cache](kv-cache.md)
- [Speculative decoding](speculative-decoding.md)
