# LIVEditor: Lightning Unified Video Editing via In-Context Sparse Attention (ISA)

**Source:** HuggingFace Daily Papers (2026-05-07)
**Paper:** [arXiv 2605.04569](https://arxiv.org/abs/2605.04569) · [HF](https://huggingface.co/papers/2605.04569)
**Raw:** [raw](../../raw/huggingface/2026-05-07-lightning-unified-video-editing-in-context-sparse-attention.md)

## TL;DR

In-Context Learning has become the dominant paradigm for video editing, but the quadratic attention cost over long context windows is now the binding bottleneck. ISA (In-context Sparse Attention) is the first near-lossless empirical sparse attention framework specifically for ICL video editing. Two structural insights drive the design: context tokens have substantially lower saliency than source tokens, and Query sharpness correlates with attention approximation error. The result is LIVEditor, a video editor that achieves a ~60% reduction in attention-module latency while surpassing state-of-the-art on EditVerseBench, IVE-Bench, and VIE-Bench.

## Mechanism

```
Stage 1 — Context Pre-Selection
  Score context tokens by saliency
  Prune low-saliency context before attention runs

Stage 2 — Dynamic Query Routing
  Compute Query sharpness score per query
  High-error queries  → full attention (correctness matters)
  Low-error queries   → 0-th order Taylor sparse attention (cheap approximation)
```

The 0-th order Taylor sparse attention is the budget channel: low-error queries get the cheap path, high-error queries pay full price. The routing decision is based on the empirically validated correlation between Query sharpness and approximation error, so the policy is information-theoretic rather than heuristic.

## Why it matters

LIVEditor is the **video-editing analogue of routing-by-difficulty** that has appeared in language model serving. The same principle that drives speculative decoding (the easy tokens take the cheap path; the hard tokens pay full cost) now applies to attention itself within video editing. The 60% latency reduction comes from the routing layer, not from kernel optimisation, which makes it composable with FlashAttention-style improvements.

## Connections

This is the second paper this week (after MotionCache on 05-05) showing that **video diffusion attention is over-budgeted on uniform schedules**. MotionCache reused denoising steps where motion was low; ISA reuses sparse attention where Query error is low. Both are heterogeneous-information-density allocators inside video diffusion.

ISA's Query-sharpness signal is structurally similar to the Query-importance signals that have appeared in language model attention pruning, but the empirical claim that sharpness predicts approximation error is sharper than the loose attention-magnitude proxies that the language-side literature uses.

The combination with Stream-T1 (also 05-07) is interesting. Stream-T1 routes KV evictions by reward feedback. ISA routes attention by query sharpness. A combined policy would route both *what stays in cache* and *which queries get full attention* by orthogonal signals. Neither paper composes them.

## Research angle

Two questions. First, whether Query sharpness as a routing signal generalises to language model attention pruning, where the current state of the art still uses attention magnitude or learned gating. Second, whether the 0-th order Taylor approximation is a tight bound or whether higher-order terms matter for high-resolution editing tasks. The paper validates the first-order regime; nobody has tested where it breaks.

## Related

- [2026-05-05-motion-aware-caching-video.md](2026-05-05-motion-aware-caching-video.md)
- [kv-cache.md](kv-cache.md)
- [2026-05-07-stream-t1-test-time-scaling-streaming-video.md](2026-05-07-stream-t1-test-time-scaling-streaming-video.md)
