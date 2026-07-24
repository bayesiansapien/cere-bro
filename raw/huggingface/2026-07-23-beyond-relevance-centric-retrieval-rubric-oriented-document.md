---
source: farmer/huggingface
farmed: 2026-07-24T23:47:01.610703+05:30
arxiv_id: 2607.19747
url: https://huggingface.co/papers/2607.19747
arxiv_url: https://arxiv.org/abs/2607.19747
date: 2026-07-23
---

# Beyond Relevance-Centric Retrieval: Rubric-Oriented Document Set Selection and Ranking

As large language models and AI agents become the primary consumers of search results, document set quality determines the upper bound of downstream generation. Yet existing evaluation systems remain confined to scoring documents independently and aggregating via nDCG, ignoring inter-document interactions (redundancy, conflict, complementarity) and unable to answer what makes one document set better than another. To address these issues, we propose a complete evaluate-diagnose-optimize framework. We design SetwiseEvalKit, a three-level, nine-dimension document set evaluation benchmark covering both short-form and long-form scenarios, comprising approximately 28K high-quality evaluation rubrics. We systematically evaluate 12 rerankers: even the best method achieves no more than 45% coverage, cross-document coordination dimensions are universally weak, and no single method maintains top performance across both settings. Building on this, we propose Rubric4Setwise, a training-free method that converts rubric-based evaluation criteria into document set selection signals, achieving the best downstream generation performance with fewer documents and search rounds. It is the only method that maintains state-of-the-art results across both scenarios, validating the effectiveness of closing the loop from evaluation to optimization.
