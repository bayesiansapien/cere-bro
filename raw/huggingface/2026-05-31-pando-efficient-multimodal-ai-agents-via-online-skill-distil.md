---
source: farmer/huggingface
farmed: 2026-05-31T09:25:04Z
arxiv_id: 2605.24785
url: https://huggingface.co/papers/2605.24785
arxiv_url: https://arxiv.org/abs/2605.24785
date: 2026-05-31
---

# PANDO: Efficient Multimodal AI Agents via Online Skill Distillation

Recent advances in multimodal web agents often rely on increased inference-time computation, including rollout search, verifier passes, offline skill discovery, and specialist model stacks. This raises a central question: can a web agent become more efficient as it accumulates experience, rather than more expensive? We first analyze trajectories from VisualWebArena and identify three recurring sources of inefficiency: repeat-action loops, hidden discovery costs, and low prompt-cache reuse. We then introduce PANDO, a single-rollout online skill-distillation framework that maintains a structured Skill Library and combines progress reflection, confidence-based skill demotion, hierarchical routing, visual compression, and cache-aware prompting. On the full set of 910 VisualWebArena tasks, PANDO achieves a 58.3% success rate, outperforming SGV (54.0%) and our WALT reproduction (45.2%), while using 58% fewer tokens than SGV and 61% fewer tokens than WALT, without any pre-evaluation discovery budget. A 300-task ablation further shows that rules and routines provide most of the success gains, while routing, compression, and cache-aware prompting convert the larger skill library into lower marginal token cost. Finally, we introduce three trajectory-level efficiency metrics -- Action Repetition Rate, Step Overhead Ratio, and Prompt Cache Utilization -- to make efficiency visible beyond terminal success.
