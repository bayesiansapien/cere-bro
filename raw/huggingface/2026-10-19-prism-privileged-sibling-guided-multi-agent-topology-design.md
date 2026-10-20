---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.20628
url: https://huggingface.co/papers/2610.20628
arxiv_url: https://arxiv.org/abs/2610.20628
date: 2026-10-19
---

# PRISM: PRIvileged Sibling-guided Multi-Agent Topology Design

Multi-agent systems (MAS) based on large language models (LLMs) have become a powerful way to address complex problems, and their effectiveness depends critically on the collaboration topology that decides which agents participate and how they communicate. Recent work learns to generate this topology from the task query, fitting the generator to corpora of execution-verified graphs. The post-training method for such generators remains a limitation: a corpus lists the graphs that solved a query but never ranks them, leaving continued supervised fine-tuning (SFT) with no per-query preference to exploit. Without such a preference, the generator drifts toward the topologies the corpus contains most often rather than those that suit each query, so a gain on one task can come at a cost on another. We propose PRISM, which recovers per-query signal from the same corpus by learning with privileged information: a teacher reads, through a zero-initialized low-rank branch, a sibling graph that also solved the query and is unavailable at deployment, and the student matches its per-decision targets on trajectories the student samples itself. Across six diverse benchmarks PRISM improves over every topology-design baseline evaluated, and matched-teacher controls support the contribution of privileged query information. Code is available in this link.
