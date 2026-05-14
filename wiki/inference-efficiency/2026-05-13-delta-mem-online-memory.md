# δ-mem: Efficient Online Memory for Large Language Models

**Date:** 2026-05-13
**Source:** [arXiv 2605.12357](https://arxiv.org/abs/2605.12357) · HuggingFace Daily Papers
**Tier:** 1. Long-context inference, compact online state, attention augmentation
**Raw:** [`raw/huggingface/2026-05-13-mem-efficient-online-memory-for-large-language-models.md`](../../raw/huggingface/2026-05-13-mem-efficient-online-memory-for-large-language-models.md)

## TL;DR

δ-mem augments a frozen full-attention backbone with a tiny associative-memory state that gets updated by the delta rule. The state is 8x8 (yes, 64 scalars total in the headline configuration) and produces low-rank corrections to the backbone's attention computation at generation time. No fine-tuning, no backbone replacement, no context-window extension. Gains 1.10x over the frozen backbone average and 1.15x over the strongest non-δ-mem memory baseline. On memory-heavy benchmarks the gain rises to 1.31x on MemoryAgentBench and 1.20x on LoCoMo.

## Why it matters

The wiki has been tracking KV-cache eviction and selective attention as the right way to handle long context. δ-mem is the orthogonal move, do not extend the cache, add a small fixed-size online state that lives alongside. The headline configuration is 8x8. This is the cleanest "compact online memory as low-rank correction to attention" result in the wiki so far, and it composes directly with the eviction-side techniques rather than competing with them.

## Mechanism

The online state is a small matrix S (e.g., 8x8) that gets updated by delta-rule learning as the model consumes context: S receives associative updates from key-value pairs, much like the inner state of a linear-attention model. At each generation step, S is read out and produces a low-rank correction added to the standard attention computation of the frozen backbone. The state is compact (constant memory regardless of context length), the backbone is unchanged, and the correction is additive rather than replacing the cache.

The interpretive frame: the standard KV cache is high-rank evidence over the full context. The δ-mem state is a low-rank running summary. The two are not redundant, they cover different aspects of the same information. The full cache preserves position-specific tokens, the running state captures associative patterns that the attention head's query-key dynamics cannot easily recover at long range.

## Relation to prior wiki

- **Make Each Token Count (2026-05-12)** — learned KV eviction that beats the full cache. δ-mem composes cleanly: evict aggressively at the cache, retain the associative signal in the small online state. Two complementary mechanisms for the same underlying problem (attention dilution at long context). The Make-Each-Token-Count paper's research-angle prediction asked whether selective eviction composes with low-bit cache quantization. δ-mem is a different composition: selective eviction plus compact online state.
- **MDN (2026-05-11)** — momentum DeltaNet, hybrid linear attention. δ-mem can be read as importing the delta-rule mechanism from linear attention into a full-attention model as an auxiliary online state, without committing to the full hybrid architecture. A retrofit path for labs that don't want to re-pretrain.
- **MIA Signature (2026-05-09)** and **MISA (2026-05-11)** — both work at the indexer or signature axis. δ-mem works at the running-state axis. The KV-cache problem is being attacked at three orthogonal axes in three weeks.

## Research angle

Three open questions. (1) Is the 8x8 state large enough at frontier scale? The paper validates at unspecified backbone sizes; whether the state needs to scale with model size or context length is open. (2) Does δ-mem compose with MISA's sparsified indexer head? Both reduce attention dilution at different points. (3) Can δ-mem be made *learned*, with the delta-rule update replaced by a trained recurrent update? That gives a hybrid architecture as a retrofit step rather than a from-scratch design.

## Why Tier 1

Compact-online-state-as-attention-correction is a new design point in the long-context efficiency stack. It does not require re-pretraining or fine-tuning, runs over frozen backbones, and reaches double-digit-percent gains on memory-heavy benchmarks. If the technique transfers to production LLMs, it lowers the cost floor for long-context inference further.
