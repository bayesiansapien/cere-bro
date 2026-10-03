---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.820634+00:00
arxiv_id: 2609.38886
url: https://huggingface.co/papers/2609.38886
arxiv_url: https://arxiv.org/abs/2609.38886
date: 2026-10-02
---

# Benchmarking and Enhancing Skill-Level Memory for Partially Observable Robotic Manipulation

Recent advances in robot learning have enabled manipulation policies to perform increasingly diverse tasks and generalize across environments. However, reliable execution often depends on hidden task states that cannot be determined from current observations alone, making interaction history essential. We introduce HIDE, a benchmark for evaluating manipulation memory under partial observability. HIDE comprises 15 tasks covering repetition counting, historical-state recall, and execution-progress tracking, with randomized initial configurations and decision points where similar observations require different actions depending on prior events. We further propose SEEK, a framework combining three complementary memory mechanisms to retain historical evidence and track execution state. Evaluations reveal substantial limitations in existing policies on HIDE, while memory augmentation improves task success in both simulation and real-world experiments. Individual mechanisms benefit some tasks but can degrade others; their combination achieves the highest average success rate on HIDE among the evaluated configurations. These findings highlight the importance of maintaining internal representations of hidden task states and matching memory design to task-specific information requirements.
