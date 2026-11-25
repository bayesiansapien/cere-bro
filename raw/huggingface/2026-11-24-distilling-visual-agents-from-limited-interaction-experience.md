---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.920701+00:00
arxiv_id: 2611.28618
url: https://huggingface.co/papers/2611.28618
arxiv_url: https://arxiv.org/abs/2611.28618
date: 2026-11-24
---

# Distilling Visual Agents from Limited Interaction Experience

How much interaction experience is needed to distill a capable visual agent? We study learning from few tasks and recorded interaction histories. Our framework selects representative trajectories using skill-context coverage and ordered visual-decision similarity. On-policy distillation (OPD) learns through fresh interaction on selected tasks or fresh student responses at fixed histories. Across Navigation, Sokoban, and spatial mapping, even one online training task supports transfer to other tasks. Four fixed trajectories raise a 4B student's success from 49.17% to 82.08% on standard Navigation and from 60.16% to 85.55% on Sokoban, recovering over 90% of the measured gap to a 27B teacher on these panels. On an independent Navigation panel, replay improves success from 45.83% to 76.67%, retaining 91.36% of the same-task online gain without new interaction during optimization. Training repetitions, matched supervised fine-tuning (SFT), and a 9B extension further support the value of compact experience.
