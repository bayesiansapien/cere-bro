---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.929190+00:00
arxiv_id: 2611.31053
url: https://huggingface.co/papers/2611.31053
arxiv_url: https://arxiv.org/abs/2611.31053
date: 2026-11-24
---

# ReWeave: Emergent Physical Task Topologies for Embodied Harness Optimization and Cross-Task Meta-Distillation

Long-horizon embodied tasks involve physical dependencies that may only become clear through interaction. As task understanding deepens, past trials can reveal new information for adaptation and transfer. However, coarse progress feedback cannot identify which physical preconditions held, leaving search unguided, while task-specific optimization easily overfits to individual scenes, making cross-task transfer brittle. We introduce ReWeave, a framework that jointly optimizes an embodied agent harness and an emergent physical task topology from interaction without updating policy weights. Keeping execution policies and perception frozen, ReWeave co-optimizes coupled context, workflows, and control loops. As new evidence revises the topology, ReWeave reprojects past trials onto the updated task understanding, exposing retained progress, regressions, and bottlenecks that guide parent selection and search width. Across tasks, matching verified local mechanisms to unmet preconditions consolidates 72 specialist units into 44 reusable groups (0.34times full concatenation) within a compact shared harness capable of continual learning. ReWeave improves held-out success from 89.00% to 98.75% on LIBERO-PRO and from 25.50% to 58.25% on RoboDojo, while uncovering retained progress in 89% of 159 failed RoboDojo development trials and translating stronger offline reasoning into higher online performance. On eight unseen LIBERO-PRO tasks, the shared harness reaches 51.3% success versus 41.3% for direct distillation, rising to 75.0% after continual learning.
