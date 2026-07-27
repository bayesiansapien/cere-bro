---
source: farmer/huggingface
farmed: 2026-07-27T13:15:36.767293
arxiv_id: 2607.22042
url: https://huggingface.co/papers/2607.22042
arxiv_url: https://arxiv.org/abs/2607.22042
date: 2026-07-27
---

# LAMAR: An Open Language-Aware Multilingual Alignment Reranker

In multilingual retrieval augmented generation, a retriever can retrieve relevant documents written in multiple languages, which are subsequently reranked before answer generation. However, it remains unclear whether existing multilingual rerankers consider document language when ordering semantically relevant candidates. Our analysis shows that these rerankers do not consistently prioritize documents written in the same language as the query when semantically equivalent documents are available across languages, even though document language can affect answer generation. We release LAMAR, a language aware multilingual cross encoder trained to account for both semantic relevance and language coherence. LAMAR first uses English anchored relevance distillation to establish consistent relevance scoring across multilingual inputs and then applies preference alignment for language coherence to encourage documents written in the same language as the query to receive higher rankings while retaining semantic relevance. In a controlled experiment designed to assess language coherence, LAMAR achieves the best performance overall and across all languages examined individually. LAMAR also remains competitive on established multilingual reranking benchmarks. In practical retrieval settings, LAMAR achieves the best results across all reported metrics when reranking candidates retrieved in the first stage. These results demonstrate that LAMAR accounts for language coherence while achieving strong performance on general multilingual reranking benchmarks.
