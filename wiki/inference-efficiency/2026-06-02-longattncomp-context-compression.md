# LongAttnComp: Cross-Family Context Compression for Long-Context Reasoning

**Source:** HuggingFace Daily Papers · [arXiv 2606.01336](https://arxiv.org/abs/2606.01336)
**Raw:** [raw/huggingface/2026-06-02-longattncomp-cross-family-context-compression-for-long-conte.md](../../raw/huggingface/2026-06-02-longattncomp-cross-family-context-compression-for-long-conte.md)
**Date:** 2026-06-02

## TL;DR

As applications push past 100k-token inputs, the gap between context length and inference cost has become a hard bottleneck. Context compression cuts prefill cost while trying to preserve accuracy, but training-free attention-based methods leave big gaps on demanding tasks like code reasoning. LongAttnComp fine-tunes a lightweight cross-attention scoring layer and adds token-level chunking, a token-budget top-p selection algorithm, positional reordering, and a format-agnostic query parser. A two-stage fine-tuning recipe (Stage 1: NIAH-style retrieval foundation; Stage 2: multi-hop and reasoning data) lets it match or exceed full-context accuracy on InfiniteBench Code-Debug and transfer across four target models from three families.

## Diagram

```
Full context (100k+):   prefill ALL tokens ─► quadratic prefill cost, the bottleneck
Training-free attn comp: drop low-attention tokens ─► big gaps on code reasoning

LongAttnComp:
  lightweight CROSS-ATTENTION scoring layer (fine-tuned, not training-free)
    + token-level chunking
    + token-budget top-p selection
    + positional reordering
    + format-agnostic query parser
  two-stage recipe:
    Stage 1: NIAH retrieval foundation ─► Stage 2: + multi-hop & reasoning data
  ─► matches/exceeds FULL-context on InfiniteBench Code-Debug
  ─► transfers across 4 target models / 3 families
```

## Key points

- **Trades training-free for trained, and it pays off.** Prior attention-based compressors are training-free but leave large gaps on code reasoning. LongAttnComp fine-tunes a small cross-attention scorer instead, closing those gaps.
- **The recipe is the contribution.** Token-level chunking, a token-budget top-p algorithm (keep the highest-scoring tokens up to a budget), positional reordering, and a format-agnostic query parser together make the scorer robust across task formats.
- **Two-stage fine-tuning.** Stage 1 builds a general retrieval foundation from needle-in-a-haystack-style data; Stage 2 extends it to multi-hop and reasoning tasks, largely closing the Stage-1 gap on multi-document reasoning while preserving Code-Debug performance.
- **Cross-family transfer.** The compressor transfers across four target models from three families — it is not glued to one base model.

## Relation to prior wiki knowledge

LongAttnComp sits in the **prefill-cost / context-compression** corner of the wiki's efficiency map, the input-side complement to the KV-cache work. Where VideoMLA (2026-06-02, shared low-rank latent KV) and StateKV (2026-06-01, fixed recurrent state for video) compress what is *kept* during generation, LongAttnComp compresses what is *fed in* before generation starts. Its key design choice — keep only the tokens the query actually needs — is the same "locate the load-bearing part, drop the rest" instinct the wiki has now logged across experts (dMoE, 2026-06-01), attention (StateKV), and distillation tokens (TA-OPD, 2026-06-01). See [kv-cache.md](kv-cache.md).

The notable nuance is its rejection of the training-free orthodoxy that dominated earlier attention-based compression: LongAttnComp argues a small *trained* scorer is needed to handle code reasoning, where pure attention heuristics fail. Worth tracking whether the trained-scorer approach becomes the new default for hard long-context tasks.

Related: [kv-cache.md](kv-cache.md) · [attention-mechanisms.md](../llms-foundation-models/attention-mechanisms.md)
