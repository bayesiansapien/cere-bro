---
source: farmer/huggingface
farmed: 2026-10-14T17:45:17.067247+05:30
arxiv_id: 2610.13481
url: https://huggingface.co/papers/2610.13481
arxiv_url: https://arxiv.org/abs/2610.13481
date: 2026-10-13
---

# Branching On-Policy Distillation

On-policy distillation (OPD) provides teacher supervision on student-generated trajectories, but a single trajectory realizes only one continuation at each decision, limiting supervision coverage under a finite sampling budget. We propose BranchOPD (Branching On-Policy Distillation), which selects informative decision points using student uncertainty and teacher-student disagreement, resamples student-policy continuations from shared prefixes, and applies token-level teacher supervision to both main trajectories and branches. BranchOPD operates at token-level decisions in mathematics and within-turn decisions in agent tasks. Shared-prefix reuse reduces student-generated token costs by approximately 19% on ALFWorld and 31% on WebShop relative to seven independent trajectories. We also introduce protocol-boundary repair (PBR), which uses targeted supervision under protocol constraints to mitigate repetition and wasted generation. BranchOPD outperforms Vanilla OPD and Multi-Rollout OPD (n=7) across all evaluated benchmarks, with gains over Vanilla OPD of 18.55 percentage points in mean mathematics accuracy over 16 sampled answers (avg@16) and 13.8 points in mean ALFWorld ID/OOD success. Mechanistic analyses and selection ablations show that branching at uncertain decisions expands subsequent behavior coverage and outperforms random selection and turn-initial branching.
