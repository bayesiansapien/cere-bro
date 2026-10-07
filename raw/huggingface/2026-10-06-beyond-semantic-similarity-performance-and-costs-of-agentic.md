---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.05750
url: https://huggingface.co/papers/2610.05750
arxiv_url: https://arxiv.org/abs/2610.05750
date: 2026-10-06
---

# Beyond Semantic Similarity: Performance and Costs of Agentic Retrieval for Complex Tasks

Modern information systems, including many agentic workflows, use dense retrieval to explore large amounts of unstructured data. However, dense retrieval relies on surface-level semantic similarity, which is insufficient for increasingly complex search applications. Here, we investigate agentic retrieval that combines the reasoning capabilities of Large Language Models (LLMs) with the efficient corpus exploration of retrievers in a ReAct agentic loop to solve complex retrieval tasks. In our experiments, we show that agentic retrieval is more effective than standard retrieval, improving nDCG@10 by 8.7 points using the same embedding model. Moreover, while specialized retrieval methods struggle on out-of-domain tasks, agentic retrieval is highly generalizable: the same pipeline achieves competitive results on both the ViDoRe v3 and BRIGHT leaderboards. However, this improvement comes at a cost. On average, agentic retrieval takes 107.4 seconds, compared to 0.67 seconds for standard retrieval, and consumes 764.1K input and 5.8K output tokens per query. In short, our study demonstrates the effectiveness of agentic retrieval in modern data systems and motivates future work on more cost-efficient retrieval agents for large-scale deployment.
