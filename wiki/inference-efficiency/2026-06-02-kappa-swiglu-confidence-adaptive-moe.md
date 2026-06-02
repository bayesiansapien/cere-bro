# κ-SwiGLU: Confidence-Adaptive SwiGLU for Mixture-of-Experts

**Source:** HuggingFace Daily Papers · [arXiv 2606.00761](https://arxiv.org/abs/2606.00761)
**Raw:** [raw/huggingface/2026-06-02-confidence-adaptive-swiglu-for-mixture-of-experts.md](../../raw/huggingface/2026-06-02-confidence-adaptive-swiglu-for-mixture-of-experts.md)
**Date:** 2026-06-02

## TL;DR

SwiGLU is the standard gated activation in modern Transformer MLPs, but its gate sharpness (how smooth or selective the gate is) is fixed for all of training. κ-SwiGLU makes that sharpness a learnable function of the router logit in a Mixture-of-Experts (MoE) model, so each expert gate can interpolate between smooth/broadly-active and sharp/selective gating depending on the token's routing confidence. Across MoE Transformers of 8 to 28 layers on FineWeb-Edu, it improves mean CORE performance with negligible extra parameters and small compute overhead.

## Diagram

```
Standard SwiGLU MoE:  SiLU gate sharpness κ = FIXED for every token, all of training
κ-SwiGLU:             κ = learnable f(router logit)  (token-level routing confidence)
   low confidence ─► smoother, broadly-active gate
   high confidence ─► sharper, more selective gate
   ─► +mean CORE on 8–28-layer MoE (FineWeb-Edu), ~negligible params, small overhead
```

## Key points

- **One knob, made adaptive.** SwiGLU's SiLU gate has an implicit sharpness coefficient; κ-SwiGLU exposes it and ties it to the router logit so the gate's selectivity tracks how confident the router is about the token's expert assignment.
- **Confidence-aware gating.** Confident tokens get sharp, selective gates; uncertain tokens get smoother, broadly-active gates. The mechanism is per-expert-gate-unit and learnable.
- **Cheap.** Negligible added parameters and only small compute overhead, while improving mean CORE across model depths from 8 to 28 layers.
- Code at github.com/askerlee/kappa-swiglu.

## Relation to prior wiki knowledge

κ-SwiGLU is the second MoE-efficiency paper in two days to argue that **MoE machinery should adapt to routing confidence rather than treat every token's routing identically.** dMoE (2026-06-01, aggregates a diffusion block's token-level expert choices into one block vote, cutting activated experts from 69.5 to 14.6) made *which* experts load coherent across a block; κ-SwiGLU makes the *gate sharpness within* the chosen experts adapt to confidence. Both refuse the uniform-treatment default — the dominant efficiency instinct the wiki has been logging — but at different points in the MoE pipeline: routing breadth vs gate selectivity.

It also rhymes with Conf-KV (2026-05-30, sets a per-step KV-cache budget from model confidence): both turn a model's own confidence signal into an adaptive resource allocation, one over cache budget, one over gate sharpness. Confidence-as-an-allocation-signal is becoming a recurring pattern worth a concept note.

> Note: the wiki has no standalone Mixture-of-Experts concept page yet, despite MoE appearing in dMoE, MISA, κ-SwiGLU, and the Kurate-surfaced "How to Scale MoE: muP to Maximally Scale-Stable Parameterization." This is a flagged gap for the next lint pass.

Related: [2026-06-01-dmoe-block-level-moe-diffusion-llm.md](2026-06-01-dmoe-block-level-moe-diffusion-llm.md) · [attention-mechanisms.md](../llms-foundation-models/attention-mechanisms.md) · [kv-cache.md](kv-cache.md)
