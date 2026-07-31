---
source: farmer/huggingface
farmed: 2026-07-31T19:58:50.731985
arxiv_id: 2607.26497
url: https://huggingface.co/papers/2607.26497
arxiv_url: https://arxiv.org/abs/2607.26497
date: 2026-07-31
---

# BM25 Wins at Scale: A Scaling Study of Retrieval-Augmented Generation Paradigms

Retrieval-augmented generation (RAG) spans lexical and dense retrieval, graph-based indexing, and agentic search, but these paradigms are usually evaluated on different benchmarks at one corpus size, leaving their accuracy-cost scaling unclear. To bridge this gap, we present a controlled study that varies corpus size along 28 strictly nested tiers spanning roughly 450-fold, while holding questions and a fixed bedrock of relevant and adversarial documents unchanged. Under one reader model and one judging protocol, we measure official accuracy, construction and query tokens, and latency. The results reveal a scale-dependent crossover rather than an unconditional winner. File-System Agent leads at the smallest shared tiers, but its sequential exploration costs 39 times more query tokens at the bedrock and becomes less effective as the search space grows. Around 10 million corpus tokens, BM25 overtakes it and leads at every larger shared tier, with a margin approaching 20 points at full scale. BM25 also anchors the low-cost end of the Pareto frontier without LLM-based construction. Dense retrieval remains efficient but less accurate, whereas graph-based RAG encounters construction walls before deployment scale and its scalable variants remain below BM25 at shared tiers. Overall, corpus growth increasingly favors global candidate ranking: lexical retrieval is the strongest scalable default, while agentic reasoning works best after ranked discovery rather than in place of it.
