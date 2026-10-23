---
source: farmer/huggingface
farmed: 2026-10-23T08:19:34.197472+00:00
arxiv_id: 2610.26397
url: https://huggingface.co/papers/2610.26397
arxiv_url: https://arxiv.org/abs/2610.26397
date: 2026-10-22
---

# Bridged Self-Distillation for On-Policy Learning

On-policy distillation can transfer the reasoning capabilities of a strong teacher to a smaller student. However, distillation from a stronger teacher model faces two mismatches: its solutions may be difficult for a smaller student to imitate, and its token-level probabilities may be incompatible with, or even unavailable to, the student. Existing methods handle these settings through different forms of supervision. To this end, we propose Bridged Self-Distillation (BSD), a unified framework for distilling from any teacher that provides reasoning traces. The model to be distilled from, termed the external teacher, first provides a reasoning trace as privileged context, which can be generated in an offline fashion. The student generates rollouts without this context, while a copy of the student conditioned on it, serving as the self-teacher, scores the same rollouts in the student's own token space. BSD uses the resulting token-level guidance to adjust updates on unsuccessful rollouts, with a verifier providing the outcome signal. As the external teacher is queried only to produce text, the same training procedure applies to all teacher scenarios: shared-tokenizer, cross-tokenizer, and closed API teachers. Across these scenarios, BSD improves over the base model and outperforms baselines tailored to each scenario, offering a novel and unified pathway for distillation. Code is available: https://github.com/TUMLegalTech/Bridged-Self-Distillation
