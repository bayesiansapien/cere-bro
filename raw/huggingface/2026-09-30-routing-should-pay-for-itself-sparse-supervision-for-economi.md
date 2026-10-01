---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.37402
url: https://huggingface.co/papers/2609.37402
arxiv_url: https://arxiv.org/abs/2609.37402
date: 2026-09-30
---

# Routing Should Pay for Itself: Sparse Supervision for Economical LLM Routing

Large language model (LLM) routing reduces serving cost by assigning each query to an appropriate model while preserving response quality. Learning such a router, however, often requires executing multiple candidate models on historical queries to collect query--model quality feedback, creating a nontrivial supervision cost before deployment. Existing work largely focuses on serving-time efficiency, overlooking whether the resulting savings are sufficient to recover this upfront expenditure. We further observe that routing quality often saturates well before all query--model feedback is collected, suggesting that dense supervision can be economically over-provisioned. We propose SaveRouter, a sparse-supervision routing framework that selectively acquires informative model feedback and shares capability information across related queries, while retaining query-level refinement for fine-grained routing. We evaluate routing by jointly accounting for supervision expenditure and subsequent serving-time savings. Across four routing benchmarks, the main setting uses only about 33--41% of available training feedback while maintaining competitive or better routing quality, and reduces the break-even deployment volume by approximately 1.9--9.5 times compared with the fastest conventional router. Further analysis shows that acquiring more supervision is not always economically preferable: the supervision level that minimizes serving cost can differ from the one that achieves the earliest payback. Our code is publicly available at https://github.com/LAMDA-Model-Reuse/SaveRouter.
