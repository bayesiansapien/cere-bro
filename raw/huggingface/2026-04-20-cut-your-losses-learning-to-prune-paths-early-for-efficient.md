---
source: farmer/huggingface
farmed: 2026-04-20T00:00:00
arxiv_id: 2604.16029
url: https://huggingface.co/papers/2604.16029
arxiv_url: https://arxiv.org/abs/2604.16029
date: 2026-04-20
---

# Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning

Parallel reasoning enhances Large Reasoning Models (LRMs) but incurs prohibitive costs due to futile paths caused by early errors. To mitigate this, path pruning at the prefix level is essential, yet existing research remains fragmented without a standardized framework. In this work, we propose the first systematic taxonomy of path pruning, categorizing methods by their signal source (internal vs. external) and learnability (learnable vs. non-learnable). This classification reveals the unexplored potential of learnable internal methods, motivating our proposal of STOP (Super TOken for Pruning). Extensive evaluations across LRMs ranging from 1.5B to 20B parameters demonstrate that STOP achieves superior effectiveness and efficiency compared to existing baselines. Furthermore, we rigorously validate the scalability of STOP under varying compute budgets—for instance, boosting GPT-OSS-20B accuracy on AIME25 from 84% to nearly 90% under fixed compute budgets. Finally, we distill our findings into formalized empirical guidelines to facilitate optimal real-world deployment. Code, data and models are available at https://bijiaxihh.github.io/STOP.
