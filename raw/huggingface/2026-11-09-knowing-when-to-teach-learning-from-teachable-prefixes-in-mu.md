---
source: farmer/huggingface
farmed: 2026-11-10T05:05:44.206928+00:00
arxiv_id: 2611.08179
url: https://huggingface.co/papers/2611.08179
arxiv_url: https://arxiv.org/abs/2611.08179
date: 2026-11-09
---

# Knowing When to Teach: Learning from Teachable Prefixes in Multilingual Reasoning Distillation

On-Policy Self-Distillation (OPSD) improves reasoning by training a student on its own reasoning, using the same model conditioned on reference solutions as a teacher. Applying OPSD to multilingual reasoning requires the teacher to provide useful feedback across languages, even when the student makes mistakes in intermediate steps. We observe a phenomenon we call Teacher Drift: as these mistakes accumulate, the teacher may follow the student's incorrect steps instead of correcting them. Our analysis shows that this shift tends to occur earlier in lower-resource languages. To account for these differences across languages, we propose Teachable On-Policy Self-Distillation (TOPSD), which determines where and whether teacher supervision should be applied to each reasoning trajectory. TOPSD uses teacher-student likelihood to estimate where drift begins and select a prefix for supervision. It then verifies whether the teacher can recover the correct answer from that prefix, applying distillation only to prefixes that pass verification. Experiments on multilingual mathematical reasoning across ten languages and three model scales show that TOPSD consistently outperforms conventional OPSD, particularly in low- and medium-resource languages.
