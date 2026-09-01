---
source: farmer/huggingface
farmed: 2026-09-01T08:46:18.970698+00:00
arxiv_id: 2608.30241
url: https://huggingface.co/papers/2608.30241
arxiv_url: https://arxiv.org/abs/2608.30241
date: 2026-09-01
---

# PaperBanana-Interact: Scientific Diagram Refinement with Multi-Turn Human Feedback

Recent efforts have aimed to automate scientific diagram generation from paper content (Lin et al., 2026; Zhu et al., 2026a). However, fully satisfying an author's visual and communicative preferences in a single turn is challenging: in our formative user study (N = 14), all participants requested further revisions after viewing an initial draft, and 86% of them rated the refined diagrams as more satisfactory. Despite the clear demand, the multi-turn workflow remains largely underexplored. To bridge this gap, we present MTPaperBananaBench, a benchmark for multi-turn diagram generation containing 292 images annotated with 3,518 user requirements. To reduce expensive human studies and enable scalable benchmarking, we construct a user simulator that, at each turn, identifies unsatisfied requirements and converts k of them into natural language feedback. Evaluating both requirement satisfaction and overall diagram quality reveals two key failure modes shared across baseline multiturn systems: (1) quality drift, where diagram quality progressively declines over turns, and (2) forgetting, where previously implemented features are lost in subsequent turns. To address these issues, we introduce PaperBanana-Interact, a multi-agent system that refines diagrams via an internal critique-and-refine loop. PaperBanana-Interact consistently improves rather than degrades diagram quality across turns, outperforming baselines by 11.9-18.6 points in quality score and reducing forgetting by 3.7-6.2 points.
