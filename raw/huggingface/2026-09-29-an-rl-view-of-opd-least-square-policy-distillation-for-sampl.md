---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.931843+00:00
arxiv_id: 2609.35505
url: https://huggingface.co/papers/2609.35505
arxiv_url: https://arxiv.org/abs/2609.35505
date: 2026-09-29
---

# An RL View of OPD: Least Square Policy Distillation for Sample-Efficient LLM Reasoning

We study on-policy distillation (OPD) through the lens of reinforcement learning, establishing a connection between the reverse-KL objective in OPD and KL-regularized policy optimization. Building on this connection, we introduce Least-Square Policy Distillation (LSPD), an RL-inspired framework that brings optimistic exploration and off-policy data reuse from value-based RL into policy distillation. LSPD preserves policy diversity through exploration while improving rollout efficiency by repeatedly learning from previously collected trajectories. Our theoretical analysis connects LSPD to optimistic value-based learning and shows that its idealized formulation achieves a sharp mathcal O(log K) regret bound under online exploration. Empirically, LSPD consistently outperforms existing distillation baselines across six mathematical reasoning benchmarks and diverse teacher-student settings, with average gains of +1.59 points in Avg@16. Remarkably, through Pass@k evaluations up to k=64, we found that LSPD better preserves policy diversity by achieving stronger performance as k grows. Its fully off-policy variant achieves comparable performance to vanilla OPD using only the first 25% of rollout batches. Together, these results provide an RL perspective on OPD that offers both a principled interpretation and a practical route toward more effective and rollout-efficient language model distillation.
