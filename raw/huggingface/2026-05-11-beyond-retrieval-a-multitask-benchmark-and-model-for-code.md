---
source: farmer/huggingface
farmed: 2026-05-11T00:00:00
arxiv_id: 2605.04615
url: https://huggingface.co/papers/2605.04615
arxiv_url: https://arxiv.org/abs/2605.04615
date: 2026-05-11
---

# Beyond Retrieval: A Multitask Benchmark and Model for Code Search

Code search has usually been evaluated as first-stage retrieval, even though production systems rely on broader pipelines with reranking and developer-style queries. Existing benchmarks also suffer from data contamination, label noise, and degenerate binary relevance. In this paper, we introduce CoREB, a contamination-limited, multitask code retrieval and reranking benchmark, together with a fine-tuned code reranker, that goes beyond retrieval to cover the full code search pipeline. CoREB is built from counterfactually rewritten LiveCodeBench problems in five programming languages and delivered as timed releases with graded relevance judgments. We benchmark eleven embedding models and five rerankers across three tasks: text-to-code, code-to-text, and code-to-code. Our experiments reveal that: (1) code-specialised embeddings dominate code-to-code retrieval (~2x over general encoders), yet no single model wins all three tasks; (2) short keyword queries, the format closest to real developer search, collapse every model to near-zero nDCG@10; (3) off-the-shelf rerankers are task-asymmetric, with a 12-point swing on code-to-code and no baseline net-positive across all tasks; (4) our fine-tuned CoREB-Reranker is the first to achieve consistent gains across all three tasks.
