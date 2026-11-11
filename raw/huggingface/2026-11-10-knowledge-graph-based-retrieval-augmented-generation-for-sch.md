---
source: farmer/huggingface
farmed: 2026-11-11T05:06:31.328860+00:00
arxiv_id: 2501.08686
url: https://huggingface.co/papers/2501.08686
arxiv_url: https://arxiv.org/abs/2501.08686
date: 2026-11-10
---

# Knowledge Graph-based Retrieval-Augmented Generation for Schema Matching

Traditional similarity-based schema matching methods fail to resolve semantic ambiguities and conflicts in complex, domain-specific mappings due to a lack of commonsense and domain-specific knowledge. In parallel, large language models (LLMs) without sufficient background knowledge tend to hallucinate, further complicating schema matching. To overcome these limitations, we introduce KG-RAG4SM, a Knowledge Graph-based Retrieval-Augmented Generation for Schema Matching. This method integrates novel retrieval mechanisms, including LLM-based, vector-based, graph traversal-based, and hybrid techniques with advanced reranking schemes to extract the most relevant subgraphs from large external KGs. Our approach achieves superior results without requiring re-training, as evidenced by improvements of 39.79% in precision and 30.56% in F1 score over LLM-based state-of-the-art (SOTA) methods (e.g., Jellyfish-8B) on the MIMIC dataset, and enhancements of 69.20% in precision and 21.99% in F1 score over pre-trained language model (PLM)-based SOTA methods (e.g., SMAT) on the Synthea dataset. Additionally, KG-RAG4SM scales effectively across KGs from commonsense KGs to domain-specific ones, while its instruction-tuning knowledge exclusion component ensures truthful performance in end-to-end schema matching tasks despite the suboptimal relevance of KG context. Our empirical analysis and case studies from real-world scenarios show that the hallucination problem in LLMs for schema matching is well mitigated by our solution.
