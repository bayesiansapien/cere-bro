---
source: farmer/huggingface
farmed: 2026-09-08T04:39:30Z
arxiv_id: 2609.02998
url: https://huggingface.co/papers/2609.02998
arxiv_url: https://arxiv.org/abs/2609.02998
date: 2026-09-08
---

# Verify Before You Distill: Prompt-Level Teacher Gating for On-Policy Distillation

On-policy distillation (OPD) accelerates post-training by providing dense token-level supervision from a frozen teacher on the student's own rollouts. Vanilla OPD applies this supervision uniformly across prompts, without checking whether the teacher is reliable for each prompt. Because reverse KL is mode-seeking, a confidently wrong teacher can induce a strong yet misleading update. Distributional proxies, such as entropy or teacher-student likelihood agreement, measure uncertainty or agreement but do not directly verify outcome correctness. We introduce Teacher-Gated On-Policy Distillation (TGOPD), built on the principle that teacher reliability should be verified at the prompt level before dense supervision is admitted. TGOPD estimates reliability from a small set of verifier-scored teacher probes and routes each prompt exclusively to dense OPD when the reliability check passes or to verifier-grounded GRPO otherwise. Across 4B and 35B students in mathematics, code, and instruction following, TGOPD outperforms Vanilla OPD in all six single-domain settings and achieves higher seven-benchmark averages at both scales under multi-domain training. By using otherwise-idle teacher capacity for reliability estimation, TGOPD also reduces teacher-side compute waste in asynchronous OPD, increasing teacher-node GPU utilization from 9.8% to 78.9% in the measured 4B single-domain run.
