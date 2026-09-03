---
source: farmer/huggingface
farmed: 2026-09-03T17:01:45.591071
arxiv_id: 2608.30949
url: https://huggingface.co/papers/2608.30949
arxiv_url: https://arxiv.org/abs/2608.30949
date: 2026-09-03
---

# MULTI3IR: A Benchmark for Multi-perspective Multi-domain Multi-modal Information Retrieval

Information retrieval (IR) increasingly targets open-ended queries that admit diverse perspectives. Existing IR benchmarks, however, focus primarily on closed-ended queries, while even open-ended benchmarks largely consist of queries whose supporting documents span a single subject domain and modality. We introduce Multi^3IR, a benchmark that evaluates how well retrievers cover the multifaceted perspectives of open-ended queries across diverse domains and modalities. It comprises 104.9K Stack Exchange queries, each annotated with perspective descriptions that capture the query's implicit viewpoints. We further propose SPIN, a parameter- and label-efficient method that learns noise vectors to steer embeddings toward diverse yet meaningful semantic directions. Experiments show that existing multimodal retrievers suffer from single-perspective bias, while SPIN substantially improves perspective coverage on Multi^3IR and generalizes well to unseen open-ended IR benchmarks. The dataset and experimental code are available at https://github.com/seokwon99/Multi3IR.
