---
source: farmer/huggingface
farmed: 2026-08-25T14:22:16.352902
arxiv_id: 2608.19408
url: https://huggingface.co/papers/2608.19408
arxiv_url: https://arxiv.org/abs/2608.19408
date: 2026-08-25
upvotes: 5
authors: ["Chen Yang", "Haiyuan Wan", "Rengrong Xiong", "Yize Chen", "Danny H. K. Tsang"]
---

# Beyond Imitation: Filtering On-Policy Distillation by Reasoning Progress

**Upvotes:** 5
**Authors:** Chen Yang, Haiyuan Wan, Rengrong Xiong, Yize Chen, Danny H. K. Tsang

On-policy distillation (OPD) has emerged as an effective framework for post-training language models by pairing student-generated trajectories with dense token-level supervision from a teacher. However, OPD implicitly assumes that teacher-derived rewards are an appropriate proxy for reasoning progress, and therefore treats all teacher feedback equally during policy optimization. While in practice, this assumption does not always hold. We observe that teacher-derived rewards often conflict with genuine reasoning progress, as reasoning steps with clear reasoning advancement may still receive lower distillation rewards, simply due to deviation from teacher's outputs. To address this mismatch, we propose Reasoning-Progress-Aware Reward Filtering for On-Policy Distillation (R2-OPD), which constructs two within-trajectory rankings of reasoning spans, one from teacher-derived rewards and the other from independently estimated progress reward. Distillation rewards are selectively suppressed whenever the two rankings disagree, reducing supervision that conflicts with reasoning progress while preserving effective teacher guidance. Our approach shows consistent improvement over standard OPD especially regarding reasoning performances.
