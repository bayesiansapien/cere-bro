---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13728
category: cs.CL
concept: inference-efficiency
url: https://arxiv.org/abs/2604.13728
published: 2026-04-16
authors: Harishkumar Kishorkumar Prajapati
---

# Hybrid Retrieval for COVID-19 Literature: Comparing Rank Fusion and Projection Fusion with Diversity Reranking

**arXiv:** https://arxiv.org/abs/2604.13728
**Authors:** Harishkumar Kishorkumar Prajapati

## Abstract

arXiv:2604.13728v1 Announce Type: cross  Abstract: We present a hybrid retrieval system for COVID-19 scientific literature, evaluated on the TREC-COVID benchmark (171,332 papers, 50 expert queries). The system implements six retrieval configurations spanning sparse (SPLADE), dense (BGE), rank-level fusion (RRF), and a projection-based vector fusion (B5) approach. RRF fusion achieves the best relevance (nDCG@10 = 0.828), outperforming dense-only by 6.1% and sparse-only by 14.9%. Our projection fusion variant reaches nDCG@10 = 0.678 on expert queries while being 33% faster (847 ms vs. 1271 ms) and producing 2.2x higher ILD@10 than RRF. Evaluation across 400 queries -- including expert, machine-generated, and three paraphrase styles -- shows that B5 delivers the largest relative gain on keyword-heavy reformulations (+8.8%), although RRF remains best in absolute nDCG@10. On expert queries, MMR reranking increases intra-list diversity by 23.8-24.5% at a 20.4-25.4% nDCG@10 cost. Both fusion pipelines evaluated for latency remain below the sub-2 s target across all query sets. The system is deployed as a Streamlit web application backed by Pinecone serverless indices.
