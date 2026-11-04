---
source: farmer/huggingface
farmed: 2026-11-04T11:17:37.426675+00:00
arxiv_id: 2610.38637
url: https://huggingface.co/papers/2610.38637
arxiv_url: https://arxiv.org/abs/2610.38637
date: 2026-11-03
---

# On-Policy Self-Distillation with Teacher Evolution

On-Policy Self-Distillation (OPSD), which aligns a student model's token-level distribution with that of its self-teacher prompted by privileged context, has emerged as a promising direction to mitigate reward sparsity in sequence-level post-training paradigms. However, OPSD often fails to achieve continuous performance gains during training. In this paper, we find that the model's limited self-teaching capability underlies this phenomenon by generating unreliable guidance on certain samples. To address this problem, we propose Teacher-Evolution Self-Distillation (TESD), which enables the self-teacher to generate rollouts and receive environmental feedback based on task correctness and context independence. First, using these rewards as training objectives, we perform teacher-oriented optimization to continuously enhance the model's self-teaching capability during distillation. Second, by estimating teacher guidance reliability from these rewards, we apply adaptive student-oriented optimization to down-weight samples with unreliable guidance. Extensive experiments across multiple datasets and model scales show that TESD consistently outperforms representative token-level and sequence-level methods, highlighting the necessity of improving supervision quality in OPSD.
