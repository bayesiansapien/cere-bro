---
source: farmer/huggingface
farmed: 2026-08-11T07:29:49.637235+00:00
arxiv_id: 2608.06614
url: https://huggingface.co/papers/2608.06614
arxiv_url: https://arxiv.org/abs/2608.06614
date: 2026-08-11
---

# Factorized Hypothesis Search for Evidence-to-Taxonomy Retrieval

Large-taxonomy retrieval often assumes that the input already expresses the target concept. In many settings, however, the input is indirect evidence, such as a table cell whose meaning depends on its row, column, datatype, and context. We call this mismatch the retrieval readiness gap. Our analysis shows that the current index retrieves the target reliably when its semantics are explicit, while raw evidence often leaves it deep in the ranking. We propose Factorized Hypothesis Search (FHS), which maintains multiple partial interpretations over named semantic dimensions. These hypotheses support structured query rendering, multi-hypothesis retrieval, and dimension-level candidate verification. On both financial taxonomy tagging and CodiEsp clinical coding tasks, FHS achieves the best Recall@1, MRR, and final accuracy among the non-oracle methods. Replacing the factorized hypothesis path with a free-text ensemble causes the largest drop in head-ranking performance, while sequential refinement provides no additional gain over FHS's strong parallel first round.
