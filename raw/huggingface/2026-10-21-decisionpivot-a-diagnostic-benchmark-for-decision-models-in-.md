---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.642589
arxiv_id: 2610.28522
url: https://huggingface.co/papers/2610.28522
arxiv_url: https://arxiv.org/abs/2610.28522
date: 2026-10-21
---

# DecisionPivot: A Diagnostic Benchmark for Decision Models in LLM Systems

Decision models support routing, guardrails, and output verification in LLM systems. However, item accuracy alone cannot establish whether models make correct decisions across controlled variations or assign reliable confidence to their predictions. We introduce DecisionPivot, a diagnostic benchmark comprising 48 tasks and 40,033 items across seven decision roles. Its core track contains 7,800 items from 13 generated task families, organized into contrast groups with computed answers verified by independently implemented solvers. The complementary reference track contains 32,233 items from 35 public test sets, preserving their original evaluation metrics. We evaluate 40 decision models and 14 general models using documented, model-specific protocols, assessing item and contrast-group accuracy, probability ordering, calibration, and empirical selective coverage. Our results reveal substantial differences obscured by aggregate scores: two 27B models separated by only 2.6 points on the reference track achieve contrast-group accuracies of 70.1% and 44.2%. Across 2,400 binary contrast pairs, Perplexity Decider correctly ranks the positive member above the negative member in 92.3% of pairs but answers both members correctly in only 74.1%, exposing a gap between probability ordering and decision correctness. Models with similar item accuracy also differ in the reliability of their high-confidence predictions. On a separate 1,296-item subset, GLM-5.3 achieves 93.5\% contrast-group accuracy at a higher reasoning setting, compared with 81.5% at its lowest effort. By linking errors to pivotal details and difficulty levels, DecisionPivot provides fine-grained diagnostics of decision failures that aggregate evaluation alone cannot reveal.
