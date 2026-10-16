---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.223325+05:30
arxiv_id: 2610.20572
url: https://huggingface.co/papers/2610.20572
arxiv_url: https://arxiv.org/abs/2610.20572
date: 2026-10-15
---

# Recovering Reliable Supervision via Critique-Guided On-Policy Distillation

On-policy distillation (OPD) trains a student model on its own rollouts with token-level supervision from a teacher, assuming that the teacher can reach a correct answer from any prefix the student writes. We call this property the recoverability of the teacher and show it fails on incorrect rollouts: the teacher follows student errors, although it recognizes them. We propose CriticOPD, using error recognition to restore recoverability. The teacher critiques an incorrect rollout, allowing the student to rewrite its solution following the error. The resulting output, including the critique as privileged information, is scored by the teacher while the student uses the revision without the critique for training. On two Qwen3 students and six mathematical reasoning benchmarks, CriticOPD improves OPD, with the largest gains on competition problems.
