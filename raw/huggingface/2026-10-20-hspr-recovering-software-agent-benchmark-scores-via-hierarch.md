---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.24611
url: https://huggingface.co/papers/2610.24611
arxiv_url: https://arxiv.org/abs/2610.24611
date: 2026-10-20
---

# HSPR: Recovering Software-Agent Benchmark Scores via Hierarchical Posterior Inference

Evaluating software agents on a full benchmark is expensive. A small task subset can preserve agent rankings while yielding inaccurate scores. Historical responses provide useful structure, but tasks with identical source responses can have different outcomes for a new target agent. We introduce Hierarchical Score Posterior Recovery (HSPR), which combines source-fitted response factors with uncertain group success rates. Observed target outcomes update the posteriors over the target latent state and group rates; posterior-guided acquisition selects subsequent tasks. Its score-based criterion equals the expected one-step reduction in full-score posterior variance. Observed successes and posterior-predictive counts for unqueried tasks yield a full-score posterior. The final estimate uses its median with source-selected calibration. At a 10% task budget on four task banks from the SWE-bench family, HSPR achieves the lowest mean absolute error (MAE) on three banks and the lowest maximum absolute error (MaxErr) on all four among the methods compared. Removing group uncertainty or replacing adaptive queries increases macro MAE in the respective controls. Macro MAE decreases across 5-20% budgets.
