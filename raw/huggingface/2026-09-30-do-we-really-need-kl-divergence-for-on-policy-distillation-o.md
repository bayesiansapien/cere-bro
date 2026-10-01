---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.33791
url: https://huggingface.co/papers/2609.33791
arxiv_url: https://arxiv.org/abs/2609.33791
date: 2026-09-30
---

# Do We Really Need KL Divergence for On-Policy Distillation of Large Language Models?

Since the advent of knowledge distillation, KL divergence has been the standard loss in distillation. Recently, on-policy distillation (OPD) has emerged as an efficient post-training paradigm for LLMs. As a distillation method, OPD naturally inherits KL divergence as its standard loss. However, in this work, we find that KL divergence may not be necessary for OPD. We show that simply preserving the update direction is sufficient for effective OPD. As long as the update direction is toward the teacher, OPD works. More precisely, it is not the direction of every token, but the direction of a small subset of tokens where the teacher and student disagree strongly. We first show that simply assigning a reward of (+1) to tokens where the teacher probability is higher than the student probability and (-1) where it is lower, which merely encourages updates toward the teacher, reproduces almost the same training mode as OPD with reverse KL. We further show that only the direction of a small subset of tokens with large teacher-student disagreement is critical, and training works as long as their update direction is toward the teacher, even if other tokens are pulled away from the teacher. And as an application of these findings, we introduce Consensus Multi-Teacher On-Policy Distillation (C-MOPD) to improve Multi-Teacher On-Policy Distillation (MOPD). Unlike MOPD, which routes each sample to a single teacher and may cause capability conflicts across domains, C-MOPD lets every sample be supervised by all teachers. Experiments show that C-MOPD consistently outperforms MOPD on both math and code benchmarks. Our code is available at https://github.com/LeapLabTHU/KL-Free-OPD.
