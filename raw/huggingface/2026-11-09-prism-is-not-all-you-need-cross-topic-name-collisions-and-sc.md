---
source: farmer/huggingface
farmed: 2026-11-10T05:05:44.205973+00:00
arxiv_id: 2611.01362
url: https://huggingface.co/papers/2611.01362
arxiv_url: https://arxiv.org/abs/2611.01362
date: 2026-11-09
---

# "PRISM" Is Not All You Need: Cross-Topic Name Collisions and Scientific Paper Retrieval

Scientific names increasingly connect papers from different research topics, leaving readers to recover a paper's identity from context. We study this convergence in 564,861 AI-related arXiv records. Cross-topic name collision grows 4.33-fold from a pooled 2020-2022 reference to 2026, compared with 1.12-fold within topics. A second sentence encoder reproduces the pattern, and name-group resampling quantifies its uncertainty. Fixed word-frequency bands locate the main increase in an intermediate-frequency vocabulary shared by many research areas. We then measure the ambiguity that remains after supplying research clues. With the same three-term query construction, shared-name targets retain matched identification deficits of 25.7 percentage points under title-based BM25 and 6.9 points under title-plus-abstract E5. Within fixed same-name candidates, listwise language-model ranking reaches 89.2% using the query and candidate titles. Topic-specific comparisons show that context resolves more cross-topic ambiguity. The evaluation separates candidate competition, document fields, and contextual ranking through lexical, dense, and language-model baselines. Source-linked cases and a portable evaluation collection make the phenomenon inspectable and reusable for scientific retrieval and research assistants.
