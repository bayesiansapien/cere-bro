---
source: farmer/huggingface
farmed: 2026-09-18T16:13:44.923131+00:00
arxiv_id: 2609.20784
url: https://huggingface.co/papers/2609.20784
arxiv_url: https://arxiv.org/abs/2609.20784
date: 2026-09-18
---

# RetireOPD: Self-Retiring On-Policy Distillation for Agentic Reinforcement Learning

Multi-turn agents trained with reinforcement learning (RL) receive a single scalar reward per trajectory, which motivates self on-policy distillation (OPD) to supply dense token-level supervision from a self-teacher with privileged task skills, letting a skill-free student internalize them. This recipe, however, is undermined by two findings in agentic tasks: privileged information alone does not always make a teacher reliable, and the benefit of teacher supervision is stage-dependent. We therefore propose RetireOPD (Self-Retiring On-Policy Distillation), which first optimizes a decoupled, skill-conditioned teacher with environment rewards and then trains a skill-free student jointly with RL and OPD. Rather than following a predefined distillation schedule, RetireOPD adopts Adaptive Retirement: the student drops the teacher on its own once their discrepancy stops shrinking and it reaches a target fraction of the teacher's success rate, after which training proceeds with RL alone. Across Qwen2.5 models from 1.5B to 7B, RetireOPD improves ALFWorld success rate over RL baseline by 14.1% to 18.8% and WebShop accuracy by 11.8% to 19.0%, and surpasses its own skill-conditioned teacher in every setting.
