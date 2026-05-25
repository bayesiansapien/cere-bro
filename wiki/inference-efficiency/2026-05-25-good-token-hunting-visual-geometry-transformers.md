# Good Token Hunting: training-free token selection for Visual Geometry Transformers

**arXiv:** [2605.23892](https://arxiv.org/abs/2605.23892) · **HF Daily Papers:** [page](https://huggingface.co/papers/2605.23892) · **Date:** 2026-05-25
**Authors:** Shuhong Zheng (U. Toronto / Vector Institute), Michael Oechsle, Erik Sandström, Marie-Julie Rakotosaona, Federico Tombari (Google / TUM), Igor Gilitschenski (Toronto)
**Raw:** [farmer file](../../raw/huggingface/2026-05-25-good-token-hunting-a-hitchhikers-guide-to-token-selection-fo.md)

## TL;DR

Visual Geometry Transformers (VGTs) like VGGT and pi3 do multi-view 3D reconstruction in a single forward pass, but their global attention scales quadratically in the number of input frames, which kills them above ~100 images. Good Token Hunting is a training-free two-stage sparsification: an inter-frame selector picks a diverse subset of frames, then an intra-frame selector drops more redundant tokens guided by attention entropy. The choice is layer-aware. The result is over 85 percent acceleration on 500-image scenes with maintained or improved performance.

```
500 input frames ─► Stage 1: inter-frame selector (diversity)
                              │
                              ▼
                    kept frames (cover the scene)
                              │
                              ▼
                    Stage 2: intra-frame selector, layer-aware

       ┌──────────────────────┼──────────────────────┐
       ▼                      ▼                      ▼
   high-entropy layer    mid-entropy layer    low-entropy layer
   keep most tokens      keep some tokens     drop aggressively
                              │
                              ▼
                    VGT global attention runs over selected K/V
                    (training-free, drop-in, over 85 pct speedup)
```

## Key claims

- The quadratic cost is O(N^2 * L^2) in frames N and tokens-per-frame L; with N=500 the global attention is the dominant cost.
- Two-stage selection beats single-stage: pick which frames to keep first (diversity-based, so the kept subset covers the scene), then prune intra-frame tokens within the chosen frames.
- The intra-frame selection is layer-aware. Different layers have different attention entropy, so a uniform sparsification policy across layers is wrong. Layers with high entropy keep more tokens; layers with low entropy aggressively drop.
- Training-free: no retraining, no fine-tuning, no architectural change to the underlying VGT. The method is a runtime modification of the attention computation.
- Speedup is over 85 percent for 500-image scenes while maintaining or improving baseline performance.

## Relation to prior wiki content

This paper is the third in a month-long pattern: attention sparsification is moving from a model-architecture choice to a runtime control surface. [LiveEditor](2026-05-07-liveditor-in-context-sparse-attention.md) (the 05-07 paper on in-context sparse attention) showed that runtime sparsification on text transformers preserves quality when the selector is learned. [MISA](2026-05-11-misa-mixture-of-indexer-sparse-attention.md) (the 05-11 mixture-of-indexer sparse attention paper) added a learned routing layer over multiple sparsification policies. Good Token Hunting extends the same idea to visual geometry transformers and does it training-free, which is a stronger claim than either text predecessor.

It also connects to the broader [KV cache](kv-cache.md) thread: the cache is the right design surface for almost every efficiency problem, and the policy that selects what to keep or discard is the lever. Good Token Hunting is a key/value selection policy, just applied to multi-view 3D reconstruction instead of language modeling.

## Research angle

The layer-aware policy is the most interesting design choice. It points at a generalization: different layers in a transformer have systematically different roles, and a one-size-fits-all sparsification budget is wrong. This connects to [MoE BEAM](../ai-routing/2026-05-16-beam-binary-expert-activation-masking-moe.md) (the 05-16 paper on binary expert activation masking) where the same insight drove a per-layer expert routing policy. The pattern is consolidating: depth-axis specialization, not just width-axis, is now the standard frame.

The training-free claim is the practical lever: VGT deployments are stuck on huge feed-forward 3D reconstruction passes, and a 85 percent speedup with zero retraining cost is the kind of plug-in that ships. The 500-image regime in particular maps directly to autonomous driving, visual relocalization, and 4D reconstruction stacks.
