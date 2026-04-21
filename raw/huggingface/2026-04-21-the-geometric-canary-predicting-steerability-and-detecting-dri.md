---
source: farmer/huggingface
farmed: 2026-04-21T00:00:00Z
arxiv_id: "2604.17698"
url: https://huggingface.co/papers/2604.17698
arxiv_url: https://arxiv.org/abs/2604.17698
date: 2026-04-21
---

# The Geometric Canary: Predicting Steerability and Detecting Drift via Representational Stability

Reliable deployment of language models requires two capabilities that appear distinct but share a common geometric foundation: predicting whether a model will accept targeted behavioral control, and detecting when its internal structure degrades. We show that geometric stability, the consistency of a representation's pairwise distance structure, addresses both. Supervised Shesha variants that measure task-aligned geometric stability predict linear steerability with near-perfect accuracy (rho = 0.89-0.97) across 35-69 embedding models and three NLP tasks, capturing unique variance beyond class separability (partial rho = 0.62-0.76). A critical dissociation emerges: unsupervised stability fails entirely for steering on real-world tasks (rho ~0.10), revealing that task alignment is essential for controllability prediction. However, unsupervised stability excels at drift detection, measuring nearly 2x greater geometric change than CKA during post-training alignment (up to 5.23x in Llama) while providing earlier warning in 73% of models and maintaining a 6x lower false alarm rate than Procrustes. Together, supervised and unsupervised stability form complementary diagnostics for the LLM deployment lifecycle: one for pre-deployment controllability assessment, the other for post-deployment monitoring.

**Authors:** (Authors not listed in preview — see arxiv for full list)
