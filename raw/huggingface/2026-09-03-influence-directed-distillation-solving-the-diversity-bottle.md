---
source: farmer/huggingface
farmed: 2026-09-03T17:01:45.591071
arxiv_id: 2608.29846
url: https://huggingface.co/papers/2608.29846
arxiv_url: https://arxiv.org/abs/2608.29846
date: 2026-09-03
---

# Influence-Directed Distillation: Solving the Diversity Bottleneck in Sampled-Token On-Policy Distillation

Sampled-token on-policy distillation (OPD) efficiently transfers capabilities from teacher to student using student-generated tokens, requiring teacher probabilities only for sampled tokens. Yet it frequently suffers from diversity distillation failure: the student's pass@1 improves while its pass@k plateaus, failing to inherit the teacher's diversity. To explain this, we introduce First-Order Local Entropy Influence, a signed first-order proxy that decouples each update's entropy effect into the teacher--student log-probability gap and the student's local probability structure, and empirically links entropy contraction to negative-influence positions. Motivated by this, we propose Influence-Directed Adaptive On-Policy Distillation (IDA-OPD): rather than relying on costly full-vocabulary Forward-KL objectives, it preserves entropy-expanding updates while replacing entropy-contracting ones with divergence-adaptive advantage shrinkage, using only the teacher's sampled-token log-probability. Experiments on reasoning-oriented distillation show IDA-OPD consistently improves pass@k, inheriting the teacher's diversity through distillation, matches the strongest teacher-informed methods at strictly lower cost, and broadly maintains vanilla OPD's pass@1, all without full-vocabulary teacher information.
