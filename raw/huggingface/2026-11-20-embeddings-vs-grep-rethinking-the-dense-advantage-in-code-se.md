---
source: farmer/huggingface
farmed: 2026-11-21T10:04:29.386981+00:00
arxiv_id: 2611.20455
url: https://huggingface.co/papers/2611.20455
arxiv_url: https://arxiv.org/abs/2611.20455
date: 2026-11-20
---

# Embeddings vs. Grep: Rethinking the Dense Advantage in Code Search

Code-search benchmarks show dense encoders well ahead of BM25, yet coding agents do well with grep. What does this dense advantage measure? Existing benchmarks cannot tell: they use curated queries, old code and a handicapped BM25. To find out, we build Repo-Premium, a realistic repository-level code-search benchmark. It ranks files in real repositories, with curated and raw queries in Python, JavaScript, TypeScript, Go, Rust and Java, pull requests from 2022 to 2026, and a preregistered test pool over 91 repositories. Our experiments trace the advantage to two sources: evaluation choices that favor dense retrieval, such as splitting files into chunks for BM25 and counting edited tests as relevant, and queries that lack the code's rare identifiers. Expanding the query with LLM-written identifiers (generate-then-grep) helps BM25 far more than dense retrieval, letting it match dense retrieval in every Python pool, even on pull requests opened after the LLM was released. No method we tried predicts which retriever will win on a given query. From these results we derive three guidelines: measure dense gains against a fair lexical baseline, fuse dense retrieval with BM25, and add the code's words to queries that lack them.
