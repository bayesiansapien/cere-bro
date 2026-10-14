---
source: farmer/huggingface
farmed: 2026-10-14T17:45:17.067247+05:30
arxiv_id: 2610.12933
url: https://huggingface.co/papers/2610.12933
arxiv_url: https://arxiv.org/abs/2610.12933
date: 2026-10-13
---

# Learning More by Training Less: Uncertainty-Guided Progressive Contraction for Efficient Reasoning Post-Training

Large language models have achieved remarkable advances in complex reasoning. However, scaling reasoning post-training with ever-larger corpora can substantially increase training cost without proportional performance gains. In this study, we therefore ask: how far can reasoning supervision be compressed without sacrificing capability? To this end, we propose an uncertainty-guided progressive contraction framework that concentrates supervision and optimization on the reasoning trajectories most valuable for learning. Specifically, rather than treating a teacher-generated chain-of-thought (CoT) as a single realized path, we construct uncertainty-profiled reasoning supervision by building Monte Carlo reasoning trees around intermediate reasoning states to expose process-level uncertainty. This uncertainty first contracts the original corpus into a compact teacher-informed pool. A second, learner-aware contraction then performs online routing during SFT, concentrating optimization according to the student's evolving learning state. Together, the two stages progressively contract both supervision and optimization, substantially reducing the student training budget. Experiments across diverse reasoning benchmarks and LLM families show that our method uses as little as 0.22% of the optimization budget of full-data SFT, over 450x less training exposure, while maintaining or improving reasoning performance. Notably, our framework generalizes well across heterogeneous student families, black-box teachers, and weak-to-strong transfer. This indicates that it is not only a way to accelerate training but can also enhance reasoning capability.
