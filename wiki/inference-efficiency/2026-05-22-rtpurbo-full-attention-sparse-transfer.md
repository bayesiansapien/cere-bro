# RTPurbo / Full Attention Strikes Back: Sparse Attention Transfer in Hundreds of Steps

**Source:** HuggingFace daily papers, 2026-05-22.
**arxiv:** [2605.16928](https://arxiv.org/abs/2605.16928)
**Authors:** Yanke Zhou, Yiduo Li, Hanlin Tang (project lead), Maohua Li, Kan Liu, Lan Tao, Lin Qu, Yuan Yao (corresponding), Xiaoxing Ma. Nanjing University and Alibaba Group.

## TL;DR

Long-context inference is bottlenecked by the quadratic cost of full attention. The standard alternatives (native sparse pretraining like Kimi Delta Attention or DeepSeek Sparse Attention, or heuristic token eviction like SnapKV/Quest/RazorAttn/Minference) trade off efficiency, training cost, and accuracy. This paper shows that full-attention LLMs are **already intrinsically sparse**, and can be transformed into highly sparse models with only **hundreds of training steps** of minimal adaptation. The proposed RTPurbo method retains the full KV cache only for the small subset of retrieval heads that truly need long-context information, introduces a 16-dimensional indexer for the rest, and selects tokens dynamically per query with top-p (not fixed top-k). Up to **9.36x prefill speedup at 1M context**, about 2.01x decode speedup, near-lossless accuracy on long-context and reasoning benchmarks.

## Why this is Tier 1 core

This is the cleanest existence proof to date that long-context-class inference efficiency does not require expensive native sparse pretraining. Three mechanism observations:

1. **Only a small subset of attention heads truly requires full long-context processing.** Most heads can operate on a local-window view. This had been observed informally (attention-head ablation studies, e.g., RazorAttn's per-head budget analysis) but had not been turned into a sparse-transfer training recipe.

2. **Long-range retrieval is governed primarily by a low-dimensional subspace.** A 16-dimensional indexer is sufficient to find relevant tokens. This is a remarkable compression: instead of computing full attention scores across all 128 head-dim positions, retrieval routes through 16 dimensions.

3. **The useful token budget is strongly query-dependent.** Top-p (cumulative-probability-mass) selection beats top-k (fixed count). This is the same principle as nucleus sampling, applied to attention-mass allocation rather than next-token sampling.

## The compression chain

```
Full Attention LLM
       │
       │  hundreds of training steps
       │  (minimal adaptation)
       ▼
RTPurbo Sparse LLM
   ┌──────────────────────────────────────┐
   │ Retrieval heads (full KV cache)       │
   │   ◀── small subset, identified during │
   │       adaptation                      │
   ├──────────────────────────────────────┤
   │ Other heads (16-dim indexer)          │
   │   • Token-level dynamic top-p sparse  │
   │     selection                         │
   │   • Routes through low-rank subspace  │
   │     for retrieval                     │
   └──────────────────────────────────────┘

Result:
  • 9.36x prefill speedup at 1M context
  • 2.01x decode speedup
  • near-lossless on long-context + reasoning
```

## Why this matters now

Two reasons:

1. **It removes the "native sparse pretraining" cost barrier.** Until this paper, the offered choice was: spend the order of $10M training a frontier-scale sparse model from scratch, or use heuristic token eviction at inference and accept the accuracy hit. RTPurbo says: take your existing full-attention model, train for hundreds of steps, get a sparse model with near-lossless accuracy and major speedup.

2. **It composes with KV cache compression.** [KVServe (HF top of 2026-05-22)](2026-05-22-kvserve-adaptive-kv-compression-disaggregated-serving.md) compresses the KV cache that gets shipped over the network. RTPurbo reduces the KV cache that needs to exist for non-retrieval heads. These are orthogonal axes. A production stack using both should see multiplicative benefit on long-context throughput, not additive.

## Numbers

- Up to **9.36x prefill speedup** at 1M context.
- About **2.01x decode speedup**.
- Adaptation budget: hundreds of training steps (not thousands, not native pretraining).
- Retrieval-head indexer width: 16 dimensions (compared to typical head-dim of 64-128).

## Connection to prior wiki

- The [TIP paper (2026-04-16)](2026-04-16-tip-token-importance-on-policy-distillation.md) found that most teacher-generated tokens carry no signal and should be skipped. RTPurbo extends the same intuition to attention: most attention scores carry no information and should be skipped.
- The [Delta Attention Residuals paper (2026-05-20)](../llms-foundation-models/2026-05-20-delta-attention-residuals.md) was a related architectural intervention on attention. RTPurbo is the inference-side optimization variant.
- The [Gated DeltaNet-2 paper (2026-05-22, NVIDIA)](2026-05-22-gated-deltanet-2-linear-attention-decoupled-erase-write.md) takes a different approach by replacing attention with linear recurrent state. RTPurbo keeps attention but sparsifies it.

## Open questions

- How does RTPurbo compose with Mixture-of-Experts? The active expert count interacts with attention sparsity.
- The 16-dim indexer is suspicious. Why 16? Is this an empirical sweet spot or derived from a representation-theoretic argument? If derived, that would generalize. If empirical, it may be model-specific.
- Whether the retrieval-head subset is consistent across training runs or has to be re-identified per model.

## Industrial implication

Within 60 days, expect: (a) production deployments of long-context Claude / Mythos / Gemini that switch to a RTPurbo-class sparse-attention transfer; (b) open-source forks of llama.cpp / vLLM that implement the 16-dim indexer; (c) follow-up papers that compose RTPurbo + KVServe + speculative decoding for combined inference throughput.

## Cross-references

- [KVServe (2026-05-22)](2026-05-22-kvserve-adaptive-kv-compression-disaggregated-serving.md)
- [Gated DeltaNet-2 (2026-05-22)](2026-05-22-gated-deltanet-2-linear-attention-decoupled-erase-write.md)
- [WorldKV (2026-05-22)](2026-05-22-worldkv-world-memory-retrieval-compression.md)
- [TIP: token-importance on-policy distillation (2026-04-16)](2026-04-16-tip-token-importance-on-policy-distillation.md)
- [Delta Attention Residuals (2026-05-20)](../llms-foundation-models/2026-05-20-delta-attention-residuals.md)

## Source

Raw: `raw/huggingface/2026-05-22-full-attention-strikes-back-transferring-full-attention-into.md`.
