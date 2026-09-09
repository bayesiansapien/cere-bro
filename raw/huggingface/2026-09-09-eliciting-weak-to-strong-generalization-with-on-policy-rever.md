---
source: farmer/huggingface
farmed: 2026-09-09T05:28:24.738031+00:00
arxiv_id: 2609.08798
url: https://huggingface.co/papers/2609.08798
arxiv_url: https://arxiv.org/abs/2609.08798
date: 2026-09-09
---

# Eliciting Weak-to-Strong Generalization with On-Policy Reverse Distillation

Weak-to-strong generalization asks whether stronger models can learn from weaker supervisors and surpass them. This question is particularly important for successive model generations and multi-domain consolidation, where repeating frontier-scale post-training from scratch can be prohibitively expensive. Yet conventional distillation treats the weak teacher as an optimization target, potentially imposing its capacity ceiling on the student. We introduce On-Policy Reverse Distillation (OPRD), which evaluates the teacher's policy shift relative to its reference policy on student rollouts and amplifies the component of the student's verifier-driven policy gradient along that direction. By rescaling only verifier-supported updates, OPRD preserves the stationary points of policy optimization while accelerating learning beyond the teacher. In both successive model transfer and multi-teacher distillation, OPRD achieves higher performance with fewer student updates than existing RL and distillation approaches. Response-style analysis shows that OPRD students remain closer to models trained with verifier-based RL alone than to their weak teachers, suggesting that teacher guidance accelerates rather than redirects the student's own optimization. Results in conventional strong-to-weak distillation further demonstrate that OPRD effectively combines verifier-driven policy optimization with teacher guidance regardless of capacity ordering.
