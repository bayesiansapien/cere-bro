---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.309127+05:30
arxiv_id: 2609.33659
url: https://huggingface.co/papers/2609.33659
arxiv_url: https://arxiv.org/abs/2609.33659
date: 2026-10-08
---

# Learning Multimodal Embeddings with Evidence-Aligned Readout

Multimodal large language models can expose task-relevant evidence through generation, but producing useful evidence does not by itself determine how it enters a retrieval embedding. We study whether the semantic organization of that evidence can also specify where representations are read. To address this question, we introduce EviAlign, which couples Semantic Evidence Generation with Boundary Readout in a shared multimodal large language model. It organizes evidence into five semantic units, reads the contextualized state at each unit boundary, and aggregates these states into a single normalized embedding. Generation and contrastive retrieval objectives jointly train this shared structure. With the same trailing readout, semantic evidence and free-form CoT yield nearly identical retrieval performance, suggesting that evidence organization alone does not explain the full gain. A controlled 2times3 study compares consistent and permuted evidence organization across three readout strategies, using training targets with matched evidence spans. With five readout states and the same mean pooling, the advantage of consistent semantic organization grows from 0.65 points at length-based training positions to 2.39 at evidence boundaries, yielding a 1.74-point co-design interaction. Across 12 MMEB retrieval tasks, EviAlign achieves 76.9 average Recall@1 with 500K training pairs while retaining single-vector indexing and scoring.
