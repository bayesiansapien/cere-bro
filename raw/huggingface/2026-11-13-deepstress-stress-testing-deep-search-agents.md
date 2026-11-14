---
source: farmer/huggingface
farmed: 2026-11-14T05:10:36.531183+00:00
arxiv_id: 2607.13920
url: https://huggingface.co/papers/2607.13920
arxiv_url: https://arxiv.org/abs/2607.13920
date: 2026-11-13
---

# DeepStress: Stress-Testing Deep Search Agents

While search agents demonstrate impressive capabilities in multi-step question answering, their robustness to poor-quality evidence remains under-explored. Such evidence is rare in benchmark corpora, and resulting failures are hard to reproduce. We propose DeepStress, a dynamic stress-testing framework that subjects agents to degraded evidence at controlled rates. It replaces the retrieval module with a synthetic environment where documents are generated dynamically for each query, under independent control of their trustworthiness, relevance, and factuality. To characterize behavior under stress, we go beyond binary accuracy with a five-way classification of final-answer outcomes and two new reliability-aware metrics, RAS and CoPRAS, which credit cautious behavior and account for computational cost. Evaluating 12 systems on questions from HotpotQA and BrowseComp-Plus, we find that several open-weight agents answer confidently when sources contain obvious credibility red flags, and that many HotpotQA questions are answered from parametric knowledge even when all returned documents are factually wrong.
