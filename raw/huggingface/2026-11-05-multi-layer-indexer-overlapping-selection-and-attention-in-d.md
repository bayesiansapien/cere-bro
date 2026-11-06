---
source: farmer/huggingface
farmed: 2026-11-06T05:50:41.305937+00:00
arxiv_id: 2611.03768
url: https://huggingface.co/papers/2611.03768
arxiv_url: https://arxiv.org/abs/2611.03768
date: 2026-11-05
---

# Multi-layer Indexer: Overlapping Selection and Attention in DeepSeek Sparse Attention

Sparse attention cuts the cost of long-context inference by making the attention matrix sparse: each query attends only a subset of the sequence, chosen by a fixed pattern or, in recent production LLMs, learned per query. In DeepSeek Sparse Attention (DSA), the attention of DeepSeek-V3.2 and the GLM-5 family, every layer is preceded by a lightning indexer that scores the whole cache and keeps the k=2048 highest-scoring tokens for the layer to attend. At long context this indexer scan, not the sparse attention it feeds, is where the decode time goes. But adjacent layers select nearly the same tokens, so a layer can attend the selection of the previous indexer layer instead of its own. This removes the dependency: each indexer then runs concurrently with the attention of its layer. The resulting Multi-layer Indexer (MLI) needs no retraining and no new weights. Its default realization changes no kernel, running inside SGLang's production decode graph; an optional fused decode kernel accelerates it further on DeepSeek-V3.2. MLI composes with IndexCache (the cross-layer reuse GLM-5.2 ships as IndexShare): IndexCache drops the indexer from some layers, and MLI hides the scan on the rest. We serve DeepSeek-V3.2 and GLM-5 under IndexCache's protocol at retentions 1/2 to 1/32 (the fraction of layers that keep an indexer) and contexts 10K to 195K. At equal retention the composition decodes faster than IndexCache: up to 14.5% faster on DeepSeek-V3.2 and 9.8% on GLM-5 at 1/2, and 7.9% and 5.1% at 1/4, largest where IndexCache keeps the most indexers and growing with context. At retention 1/r it is faster still than IndexCache at 1/(2r) while keeping twice the fresh selections: at 128K it reaches 1.32x the unmodified model's decode throughput at 1/4, above IndexCache's 1.28x at 1/8. Its LongBench, RULER and LongBench v2 accuracy stays within a few percentage points of IndexCache's.
