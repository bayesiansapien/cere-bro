---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.644434
arxiv_id: 2610.27450
url: https://huggingface.co/papers/2610.27450
arxiv_url: https://arxiv.org/abs/2610.27450
date: 2026-10-21
---

# Ask to Distill: Learning to Synthesize Data for On-Policy Distillation

On-policy distillation (OPD) can succeed with surprisingly few training questions, motivating a view of questions as carriers of distributional knowledge transfer. How can we assess whether a newly generated question is valuable for distillation, and learn to generate better questions---without access to its correct answer? We introduce Ask-to-Distill (\method), a framework that treats synthetic questions as distribution elicitors and optimizes the teacher supervision they expose along student-generated trajectories. A student-initialized synthesizer is optimized using a distributional surrogate for question value, computed from a frozen student--teacher pair without reference answers, correctness rewards, or per-candidate student updates. The reward combines teacher--student disagreement with teacher probability mass on the student's candidate support, together with length and diversity controls. The generated questions are filtered and deduplicated into a prompt-only bank for standard OPD. Across mathematical reasoning, code generation, and agentic tasks, our method improves average performance and teacher-gap recovery over unoptimized student-generated prompts and KL-filtered real questions, while matching or exceeding real-bank OPD in the evaluated settings. Signal analyses further show that optimized questions can elicit denser supervision and more total signal from shorter student responses, supporting elicited distributional supervision as an objective for synthetic distillation data. Our code, data and models are publicly available at https://github.com/GasolSun36/Ask_to_Distill.
