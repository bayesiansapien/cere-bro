---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.34605
url: https://huggingface.co/papers/2609.34605
arxiv_url: https://arxiv.org/abs/2609.34605
date: 2026-09-30
---

# PMOPD: Task Ordering, Cycling, and Parameter-Update Subspace Protection in Multi-Teacher On-Policy Distillation

Multi-teacher on-policy distillation (MOPD) has emerged as a popular post-training paradigm for integrating specialized capabilities in frontier language models. Existing OPD research has primarily focused on optimizing single-task distillation through objective design, distillation scope, and teacher signal construction, whereas MOPD must aggregate multiple capabilities in shared parameters and address the resulting capability seesaw, in which improving one domain suppresses capabilities acquired from another. Inspired by the distinctive update geometry of OPD, we find that parameter updates from different tasks rapidly concentrate in their respective low-dimensional subspaces during MOPD, providing a direct geometric basis for identifying and controlling cross-task interference. We therefore propose PMOPD (Projection-based Multi-Teacher On-Policy Distillation), which constructs subspace memories from the cumulative parameter displacements of different tasks and projects both gradients and optimizer updates to remove components that interfere with protected task directions. We further develop a lightweight conflict probe to characterize task interactions and guide task ordering, together with a cycling strategy that balances subspace estimation and timely task revisitation. Experiments on representative Code, Reason, and Math tasks show that PMOPD improves every evaluated capability over MOPD, raising the average score across the three tasks by 2.54 points on Qwen2.5-7B and 2.09 points on Llama-3.1-8B. These consistent gains establish geometry-aware optimization as an effective and transferable approach to balanced multi-teacher distillation.
