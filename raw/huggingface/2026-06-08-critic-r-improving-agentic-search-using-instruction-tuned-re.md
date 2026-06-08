---
source: farmer/huggingface
farmed: 2026-06-08T09:23:13Z
arxiv_id: 2606.00590
url: https://huggingface.co/papers/2606.00590
arxiv_url: https://arxiv.org/abs/2606.00590
date: 2026-06-08
---

# Critic-R: Improving Agentic Search using Instruction-tuned Retrievers with Natural Language Introspective Feedback

Agentic search systems iteratively interact with retrieval models to answer complex queries. Despite substantial progress, optimizing retrievers for agentic search remains challenging, often requiring heavy co-training or gold-standard annotations that limit real-world applicability. We propose Critic-R, a framework that explicitly closes the feedback loop between the reasoning agent and the retrieval model during both inference and training. Critic-R introduces a critic model that evaluates the agent's introspective reasoning trace after consuming retrieved evidence to determine whether the retrieved context sufficiently supports the next reasoning step. Critic-R has two complementary mechanisms: Critic-R-Zero, an inference-time query refinement loop that iteratively rewrites queries and retrieval instructions, and Critic-Embed, an optimization approach for retrieval models that leverages successful and failed refinement trajectories as automatic supervision without requiring manual relevance annotation. We evaluate Critic-R on HotpotQA, 2WikiMultihopQA, MuSiQue, and Bamboogle. Results show that Critic-R significantly improves both retrieval quality and downstream answer accuracy.
