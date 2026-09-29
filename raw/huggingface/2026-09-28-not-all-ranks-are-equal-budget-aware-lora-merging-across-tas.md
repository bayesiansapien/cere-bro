---
source: farmer/huggingface
farmed: 2026-09-29T05:05:53.598588+00:00
arxiv_id: 2609.22237
url: https://huggingface.co/papers/2609.22237
arxiv_url: https://arxiv.org/abs/2609.22237
date: 2026-09-28
---

# Not All Ranks Are Equal: Budget-Aware LoRA Merging Across Tasks

Merging low-rank adapters (LoRAs) promises to eliminate the overhead of swapping task-specific weights at inference time. However, existing merging methods assume every layer needs the same rank budget. Further, some methods assume that rank budget needs to be split equally among the tasks too. We show this uniform-budget assumption is a major source of the performance gap between merged and per-task LoRAs. However, rank selection is an NP hard problem. To this end, we introduce Net Utility, a data free metric that first decomposes every task LoRA by its Singular Value Decomposition (SVD) and scores each of those singular directions by its task utility and its interference with other tasks directions. Next, we globally pool these scores to select singular directions with the highest values with a constraint on the total number of directions selected. The proposed Net Utility metric is applied on top of five different merging methods across three different merging spaces. The merging is done over two sets of tasks, vision and language tasks. Net utility based rank allocation outperforms its counterparts without that allocation. On average, over vision tasks it achieves +2.1% improvement in performance, and +2.2% improvement over the language tasks.
