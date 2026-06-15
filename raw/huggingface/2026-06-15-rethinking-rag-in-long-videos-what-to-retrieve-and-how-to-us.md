---
source: farmer/huggingface
farmed: 2026-06-15T06:21:28Z
arxiv_id: 2606.13141
url: https://huggingface.co/papers/2606.13141
arxiv_url: https://arxiv.org/abs/2606.13141
date: 2026-06-15
---

# Rethinking RAG in Long Videos: What to Retrieve and How to Use It?

Retrieval-augmented generation is moving beyond text into long, egocentric video, where systems must select query-relevant chunks across multiple modalities and temporal granularities. Yet progress in VideoRAG is limited by two gaps: existing benchmarks allow queries to be answered without the video, obscuring retrieval errors, and prior methods apply a single modality-granularity configuration per query, ignoring chunk-level variability. We address both by introducing V-RAGBench, a benchmark of langlequery, evidence chunk, answerrangle triplets that enables faithful, decoupled evaluation of retrieval and generation, and CARVE, a simple method that runs parallel retrievers across configurations and employs chunk-adaptive reranking to identify the winning configuration for each chunk. Each chunk then enters the generator under its winning configuration selected during retrieval, yielding an interleaved evidence form where the chunk-level decision propagates across both stages. CARVE outperforms eight recent VideoRAG baselines, with the chunks supplied to the generator interleaving multiple configurations rather than sharing a single one, a behavior unattainable by query-level methods.
