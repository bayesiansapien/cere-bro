---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.349475+05:30
arxiv_id: 2609.33711
url: https://huggingface.co/papers/2609.33711
arxiv_url: https://arxiv.org/abs/2609.33711
date: 2026-10-01
---

# DuoOPD: Learning from Joint Teacher-Student Outcomes for Multi-Task On-Policy Distillation

On-policy distillation (OPD) trains a student on its own responses with token-level feedback from a stronger teacher, yet the teacher can fail on questions the student already answers correctly, and how often each model succeeds varies across tasks. OPD ignores these outcomes and, on average, pushes down even the student's correct responses; gating feedback by student correctness fixes the direction but uses the teacher in the same way whether or not it succeeded. We introduce DuoOPD, in which the student's outcome sets the direction of feedback and the joint teacher-student outcome decides how the teacher supports it: when only the teacher succeeds, its verified answer becomes context for scoring the student's failed response, and when only the student succeeds, a weight shared within the task reinforces the whole response. A single rule covers all four outcome combinations without task-specific settings. Across Qwen3 and Llama, DuoOPD outperforms all five baselines in mean macro accuracy, improving over OPD by 2.58 and 5.98 percentage points, and it also leads on two further task mixtures spanning scientific calculation, instruction following, and code generation. Ablations show that outcome-based direction alone stays near the gated baseline, while the joint-outcome designs supply most of the gain.
