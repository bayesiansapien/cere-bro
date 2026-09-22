---
source: farmer/huggingface
farmed: 2026-09-22T11:38:12.626404+05:30
arxiv_id: 2609.23088
url: https://huggingface.co/papers/2609.23088
arxiv_url: https://arxiv.org/abs/2609.23088
date: 2026-09-22
---

# OmniEdu: Open Foundation Models for Learning and Teaching

Educational foundation models must solve problems, understand curriculum structure, diagnose learner difficulties, and provide appropriate instructional support. Existing educational language models often focus on either problem solving or tutoring, with training mixtures organized by source or task rather than capability. We present OmniEdu, an open family of foundation models for K-12 learning and teaching. Its instruction-tuning corpus combines over 100 educational resources and general instruction sources, organized around four capabilities: subject competence, curriculum grounding, diagnostic reasoning, and pedagogical action and scaffolding. Our pipeline integrates deterministic cleaning, semantic auditing and rewriting, task-specific quality scoring, token-budgeted diversity selection, and pedagogical instruction assignment. It yields 69,999 examples and 15.96M supervised response tokens, including 60,951 education-specific examples. We fine-tune 4B, 9B, and 27B models and evaluate curriculum grounding, K-12 problem solving, and pedagogical tutoring, alongside general capability. Education-oriented tuning consistently improves all three educational benchmark groups across model scales. OmniEdu-27B achieves 63.12% EM and 76.69% F1 on K12-Bench, 85.89% on MathFish, 86.95% on EDUMATH, and 78.74% in MathTutorBench's Scaffold setting. It also achieves the highest Teaching average on LongTutor among the evaluated models, at 3.02. These results demonstrate the value of curated, capability-balanced supervision for adapting general language models to educational tasks spanning problem solving, curriculum understanding, and instructional support.
