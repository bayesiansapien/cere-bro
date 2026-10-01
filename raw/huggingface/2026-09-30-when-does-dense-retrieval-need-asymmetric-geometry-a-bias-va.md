---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.32488
url: https://huggingface.co/papers/2609.32488
arxiv_url: https://arxiv.org/abs/2609.32488
date: 2026-09-30
---

# When Does Dense Retrieval Need Asymmetric Geometry? A Bias-Variance Theory of Shared and Dual Projections

Dense retrieval powers retrieval-augmented generation, semantic search, and question answering, yet the theoretical basis for choosing between shared and dual query-document projections remains unclear. We introduce a bias-variance theory for low-rank bilinear scoring. Shared projections induce positive-semidefinite operators, whereas dual projections realize arbitrary low-rank operators. We derive their exact approximation gap and prove a local Gaussian boundary: dual has lower risk exactly when squared directional signal exceeds the estimation cost of its additional degrees of freedom. This boundary motivates the Cross-fitted Asymmetry Risk Selector (CARS), which estimates reproducible directional signal from training pairs; its Gaussian counterpart admits exact selection-power and regret formulas. Guided by the theory, we run retrieval experiments across multiple datasets and embedding models. The mean Dual-minus-Shared NDCG@10 advantage more than doubles as query rotation increases from 0 degrees to 90 degrees. In the rank-sample-size grids, Shared wins 13 of 16 cells at n=32, whereas Dual wins all 32 cells at n=1024 and n=2048. Consistent with this shift, all 168 comparable operator-risk curves move toward Dual as training data grow. Compared to the two fixed-geometry baselines, CARS reduces held-out regret by 49-96% and achieves 90.1% mean geometry-selection accuracy.
