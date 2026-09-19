---
source: farmer/huggingface
farmed: 2026-09-19T13:33:45
arxiv_id: 2609.19656
url: https://huggingface.co/papers/2609.19656
arxiv_url: https://arxiv.org/abs/2609.19656
upvotes: 7
date: 2026-09-19
---

# Self-Evolving Search Index

Information retrieval is increasingly important as LLM agents tackle complex tasks involving diverse information needs. Because retrieval relies on an index that represents each document through index keys, retrieval quality depends heavily on how effectively these keys expose the knowledge contained in each document. However, effective index representations vary across retrieval environments, making it difficult for any fixed optimization strategy to perform consistently. Yet evolving an index to its retrieval environment remains largely human-driven, requiring humans to diagnose retrieval failures, refine the optimization strategy, and reprocess the index accordingly. We propose SELF-INDEX, a framework that enables an index to self-evolve without human intervention. Its Optimizer autonomously diagnoses retrieval shortfalls, selectively revises the responsible index keys, and validates each revision before updating the index. Beyond reacting to observed retrieval demands, SELF-INDEX proactively explores additional demands through a Query Simulator, allowing the index to evolve beyond the queries already available for optimization. Across diverse corpora and retrievers, SELF-INDEX consistently improves retrieval performance while outperforming existing index optimization methods. We further show that these benefits extend to downstream applications, improving the effectiveness and efficiency of search agents and helping agent memory systems retrieve useful past interactions.
