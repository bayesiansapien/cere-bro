---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.930783+00:00
arxiv_id: 2609.32472
url: https://huggingface.co/papers/2609.32472
arxiv_url: https://arxiv.org/abs/2609.32472
date: 2026-09-29
---

# AdaTutoRank: Learning to Rerank Document Sets via Adaptive Tutoring Optimization for RAG and Deep Research

Document rerankers determine what evidence reaches the downstream model in RAG and deep research, yet mainstream rerankers select by relevance matching, and individually relevant documents rarely constitute the complete, complementary, non-redundant set a complex information need demands. Prior work rewards a set by its aggregate rubric score, shifting the objective from ranking documents to composing sets. Yet that score is one scalar shared by every document in the set, so the supervision is sparse: a redundant document is rewarded with the rest whenever the set scores well, and a decisive one penalized with the rest whenever it does not; credit assignment leaves contributors indistinguishable from free riders. On-policy distillation could densify this supervision, but existing methods give every rollout the same fixed guidance, too prescriptive for strong rollouts and too abstract for weak ones. We therefore propose AdaTutoRank, a setwise reranker trained with Adaptive Tutoring Optimization (ATO) under a three-level hierarchy of nine rubric dimensions, which supplies silver labels for the cold start, rewards for reinforcement learning, and hints for distillation. ATO draws three hint forms of increasing specificity from the policy's own frozen snapshot: the rubrics alone, a self-selector's sibling-set chosen under rubrics, and a self-reflector's reflection contrasting the rollout with that sibling-set; each rollout receives the form matched to its quality. Re-scoring that rollout under the hint-conditioned frozen teacher and the hint-free snapshot distills the hint's effect into a token-level advantage that complements the group-relative outcome advantage. Across ten benchmarks spanning RAG, deep research, and setwise evaluation, AdaTutoRank attains the best overall performance while issuing fewer retrieval calls.
