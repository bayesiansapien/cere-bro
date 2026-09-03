---
source: farmer/huggingface
farmed: 2026-09-03T17:01:45.591071
arxiv_id: 2609.00638
url: https://huggingface.co/papers/2609.00638
arxiv_url: https://arxiv.org/abs/2609.00638
date: 2026-09-03
---

# It Takes Two to Match: Co-Evolving Generative Retriever with Reinforcement Learning

Retrieval is the first stage of modern search and advertising systems, selecting a candidate set from a large item universe for downstream ranking and auction. Recent work increasingly leverages LLMs to improve retrieval through query expansion, data synthesis, and retrieval-feedback training. However, the generative component is typically used for query-side augmentation, while final matching is still delegated to a downstream retriever. We introduce CoGR, a retrieval framework that instead trains LLMs to directly construct retrieval representations on both query and item sides. Each generator produces a compact set of keywords, which are matched directly through an inverted index, preserving compatibility with existing keyword-based retrieval infrastructure. CoGR uses a two-stage training pipeline. Supervised fine-tuning first establishes an aligned keyword space, after which co-evolving reinforcement learning alternately optimizes the query- and item-side generators with GRPO against the opposite side's frozen index. Both sides optimize the same query-to-item retrieval F_1 objective: the query side receives retrieval F_1 directly, while the item side receives a counterfactual marginal reward measuring the change in query-side F_1 caused by its generated keywords. Across 10 representative sparse, dense, and generative baselines, CoGR achieves the best performance on both an internal APP Marketplace dataset and the public WANDS benchmark, improving F_1 over the strongest baseline by 10.9% and 36.1%, respectively. Further analysis shows stable co-evolution and increasingly aligned query--item keyword spaces over training.
