# MISA: Mixture of Indexer Sparse Attention for Long-Context LLM Inference

**arXiv:** [2605.07363](https://arxiv.org/abs/2605.07363) · **HF Daily Papers:** [page](https://huggingface.co/papers/2605.07363) · **Date:** 2026-05-11
**Tier:** 1 — Sparse attention / KV cache / routing on the head axis
**Raw:** [farmer file](../../raw/huggingface/2026-05-11-misa-mixture-of-indexer-sparse-attention-for-long-context.md)

## TL;DR

DeepSeek Sparse Attention (DSA) made fine-grained inference-time sparse attention work by adding a learned token-wise indexer that scores every prefix token and picks the top-k for the main attention. The indexer uses 64 query heads on DeepSeek-V3.2 to stay expressive, which makes it the dominant compute cost on long contexts. MISA treats those 64 indexer heads as a mixture-of-experts pool. A cheap block-level router picks h indexer heads per query (h=8 in their setup), and only those heads run the heavy token-level scoring. Drop-in, no extra training, recovers more than 92 percent of the tokens DSA would have picked. TileLang kernel runs roughly 3.82x faster than the original DSA indexer kernel on a single H200.

## What is new

The sparse-attention literature in this wiki has been routing on the **token axis** so far. KV Packet (04-17) reuses cached token states. TurboQuant (04-22) compresses the per-token values. Stream-T1 (05-07) routes token eviction by reward feedback. LIVEditor / ISA (05-07) routes per-query attention by sharpness. All four operate on the question of which tokens to keep, evict, or compress.

MISA opens a fundamentally different axis. The indexer's 64 query heads are the bottleneck, not the cached tokens themselves. By turning the indexer-head pool into a learned mixture of experts and routing per query to a small active subset, the per-query indexer cost drops from O(H^I * L) to O(h * L + H^I * M) where M = ceil(L / B) is the pooled key budget and B is the block size. With h=8 and B sized to keep H^I * M cheap, the long-L term collapses by 8x.

The hierarchical variant MISA-dagger adds a re-rank pass with the original DSA indexer over an enlarged candidate set, recovering the final top-k almost exactly without paying the dense per-head cost.

## Why the mechanism works

Three reasons.

First, indexer heads are redundant by design. DSA needed many heads to keep the indexer expressive enough to disagree with single-head failures on diverse prefix patterns. That redundancy is exactly what makes head-axis sparsification feasible. The router needs only enough signal to pick a useful subset, not to perfectly approximate the dense pool.

Second, the router uses block-level statistics, not token-level scoring. The control signal is cheap to compute and the routing decision is taken before the heavy token-level pass runs. This is the same architectural shape as token-axis hierarchical schemes (HISA, Quest) but applied one axis up.

Third, recovering 92 percent of the tokens picked by the dense indexer on LongBench is good enough. Fine-grained sparse attention is robust to small drift in the selected set, because the main attention then runs over the selected top-k and corrects for indexer error. MISA pays a small selection-quality cost and collects an 8x kernel speedup.

## Relation to prior wiki coverage

This is the second paper this month showing that the cost bottleneck in inference-time sparse attention is no longer the main attention pass, it is the selection pass. Stream-T1 (05-07) noticed it for the streaming-video case and routed eviction. MISA names it explicitly for text: the indexer is the new dominant cost on long contexts.

The composition with PrfaaS / Prefill-as-a-Service (04-22) is direct. PrfaaS moves prefill to a separate compute-dense datacenter and ships the resulting KV cache over Ethernet. If the indexer cost can be reduced 8x via head-axis routing, the bandwidth and compute floor for PrfaaS-style disaggregation drops along with it. The two are stackable: MISA reduces the per-token indexer compute, PrfaaS moves where the compute lives.

The composition with LIVEditor / ISA (05-07) is the cleanest example of the wiki's routing-as-efficiency thread now spanning both axes. ISA routes the query axis by sharpness. MISA routes the head axis by block-level statistics. Together they suggest that any expensive selection-side computation in sparse attention can be sparsified along a second axis if the redundancy structure is well understood.

## Research angle

Two open questions follow.

**Are indexer heads themselves trainable as a routing-aware MoE?** MISA uses h=8 heads picked by a router, but the underlying heads were trained as a dense pool. Co-training the router and the head pool (analogous to MoE expert/router co-training) is the obvious follow-up. If the head pool is co-trained, h might drop further than 8.

**Does head-axis routing compose with token-axis hierarchies?** HISA already does token-axis hierarchical selection. MISA-dagger demonstrates that head-axis routing composes with HISA-style re-ranking. A three-level scheme (block-level head router → coarse token selection → fine token re-rank) is the natural composition, and the paper does not measure how much further it would push.

## Links

- [arXiv 2605.07363](https://arxiv.org/abs/2605.07363)
- [HuggingFace](https://huggingface.co/papers/2605.07363)
- [KV cache concept page](kv-cache.md)
- [LLM Routing concept page](../ai-routing/llm-routing.md)
