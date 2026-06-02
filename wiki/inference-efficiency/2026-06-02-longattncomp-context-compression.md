# LongAttnComp: Cross-Family Context Compression for Long-Context Reasoning

## TL;DR

As applications push past 100k-token inputs, the gap between context length and inference efficiency has become a hard bottleneck. Context compression cuts prefill cost (the up-front compute of running attention over the whole input before any token is generated) while trying to preserve task accuracy. But existing training-free attention-based compressors, which drop tokens by raw attention heuristics with no learned component, leave large gaps on demanding tasks like code reasoning. LongAttnComp is a long-context adaptation of AttnComp that fine-tunes a lightweight cross-attention scoring layer rather than relying on attention heuristics alone. Around that scorer it adds token-level chunking, a token-budget top-p selection algorithm (keep the highest-scoring tokens up to a fixed budget), positional reordering, and a format-agnostic query parser. A two-stage fine-tuning recipe trains the compressor: Stage 1 builds a general retrieval foundation from needle-in-a-haystack (NIAH) style data, Stage 2 extends it with multi-hop and reasoning data. On InfiniteBench Code-Debug it matches or exceeds full-context accuracy, substantially beats training-free baselines, and transfers across four target models from three families. On LongBench v2 the two-stage recipe largely closes the multi-document reasoning gap that Stage 1 alone left open.

```
long input (100k+) ─► token-level CHUNKING ─► query parser extracts the query
                                                       │
   ┌───────────────────────────────────────────────────▼──────────────┐
   │ trained CROSS-ATTENTION scorer: score each chunk against the query │
   └───────────────────────────────┬──────────────────────────────────┘
                                    ▼ token-budget top-p selection ─► positional reorder
                          compressed context ─► FROZEN target LLM ─► answer

Training (scorer only):  Stage 1: NIAH retrieval ──► Stage 2: + multi-hop & reasoning
```

## Key points

- **Trained beats training-free where it is hard.** Prior attention-based compressors are training-free but leave big gaps on code reasoning. LongAttnComp fine-tunes only a lightweight cross-attention scorer, leaving the target LLM frozen, and closes those gaps.
- **The recipe is the contribution.** Token-level chunking, a token-budget top-p selection algorithm, positional reordering, and a format-agnostic query parser together make the scorer robust across task formats rather than glued to one prompt layout.
- **Two-stage fine-tuning.** Stage 1 establishes a retrieval foundation on NIAH-style data; Stage 2 adds multi-hop and reasoning data, largely closing the Stage-1 gap on multi-document reasoning while preserving Code-Debug performance.
- **Results:** matches or exceeds full-context accuracy on InfiniteBench Code-Debug, substantially outperforms training-free baselines, and transfers across four target models from three families, so the compressor is not tied to one base model.

## How this relates to prior wiki pages

LongAttnComp is the input-side complement to the day's generation-side cache work. Where [VideoMLA](2026-06-02-videomla-low-rank-latent-kv-cache.md) (2026-06-02, shared low-rank latent that cuts per-token KV memory 92.7%) and [StateKV](2026-06-01-statekv-linear-video-vlm.md) (2026-06-01, fixed recurrent state for linear-time video prefill) compress what is *kept during generation*, LongAttnComp compresses what is *fed in before generation starts*. Its core move, keep only the tokens the query actually needs, is the same "locate the load-bearing part, drop the rest" instinct the wiki has logged across cache eviction, expert routing, and distillation-token selection; see [kv-cache.md](kv-cache.md). The distinctive claim is its rejection of the training-free orthodoxy: it argues a small *trained* cross-attention scorer is required for hard tasks like code reasoning where pure attention heuristics fail. That makes it a trained alternative to the training-free attention-based compressors, and it is worth tracking whether the trained-scorer approach becomes the default for demanding long-context tasks.

## Gaps

Wins are reported on InfiniteBench Code-Debug and LongBench v2; coverage of other long-context regimes (very long summarization, long-form generation rather than reasoning-over-context) is not shown. The cross-family transfer is demonstrated on four models from three families, but the scorer still requires a fine-tuning stage, so the per-target-model cost of adapting or re-tuning the scorer is not quantified. The compression ratios and the resulting prefill-cost savings at fixed accuracy are asserted qualitatively rather than tabulated in the abstract.

**Source:** [arXiv 2606.01336](https://arxiv.org/abs/2606.01336) · raw: [raw/huggingface/2026-06-02-longattncomp-cross-family-context-compression-for-long-conte.md](../../raw/huggingface/2026-06-02-longattncomp-cross-family-context-compression-for-long-conte.md)
