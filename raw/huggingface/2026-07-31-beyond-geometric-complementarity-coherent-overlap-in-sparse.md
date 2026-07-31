---
source: farmer/huggingface
farmed: 2026-07-31T19:58:50.731985
arxiv_id: 2607.28308
url: https://huggingface.co/papers/2607.28308
arxiv_url: https://arxiv.org/abs/2607.28308
date: 2026-07-31
---

# Beyond Geometric Complementarity: Coherent Overlap in Sparse Mixture-of-Experts Routing

Sparse mixture-of-experts (MoE) language models route each token to multiple experts, suggesting a geometric account of their benefit: co-selected experts should contribute distinct representation directions. Existing evidence often conflates route coherence, candidate quality, and candidate-by-context interaction. We distinguish these quantities using an Expert Subspace Separation Index (ESSI), matched-route residuals, and a prefix-controlled 2times2 factorial; frozen-route interventions and a controlled Top-k study assess functional value. Three paired contrasts organize the findings. First, across six MoE architectures, expert subspaces overlap substantially, yet actual routes explain token representations better than matched alternatives. Second, across the 39 factorial cells in OLMoE, Mixtral, and DeepSeek, the selected candidate explains more of the residual representation than the strongest unselected rival in every cell, yet the actual prefix narrows this advantage throughout: all interactions are negative, and every 95% confidence interval lies below zero. Third, this geometric narrowing does not imply functional redundancy: adding later experts improves next-token prediction in 24 of 39 frozen-route comparisons, while the other 15 estimates are inconclusive; a controlled training study also favors Top-2 over Top-1 in all three seeds. We call this joint pattern coherent overlap: routing selects token-relevant experts from a shared geometric neighborhood, while useful multi-expert computation persists without disjoint linear coverage. Separating these quantities clarifies why geometric similarity alone cannot determine redundancy or pruning value.
