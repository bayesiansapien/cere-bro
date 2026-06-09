---
source: farmer/huggingface
farmed: 2026-06-09T16:28:21
arxiv_id: 2606.08432
url: https://huggingface.co/papers/2606.08432
arxiv_url: https://arxiv.org/abs/2606.08432
date: 2026-06-09
---

# Trajectory-Refined Distillation

On-policy distillation (OPD) has become a central post-training tool for large language models (LLMs), providing dense per-token teacher supervision along the student's own rollouts. In this work, we identify a common structural cause underlying OPD, which we call prefix failure. Under prefix failure, dense per-token supervision induces a bimodal teacher mixture and fragmented gradients that token-level loss truncation or reweighting fail to address. This observation motivates us to move beyond token-level loss interventions toward trajectory-level output corrections. We thus propose Trajectory-Refined Distillation (TRD), a trajectory-level correction method that revises the student's rollout under the teacher guidance while within on-policy support. By correcting problematic prefixes before distillation, TRD mitigates prefix failure at its source. Moreover, TRD improves the exploration by exposing the student to alternative valid derivations under teacher guidance, even when the original rolls are already correct. TRD can also be applied to on-policy self-distillation (OPSD), a parameter-sharing variant that uses the student model conditioned on privileged informations as the teacher. Across a wide range of benchmarks and base models at multiple scales, TRD consistently outperforms prior baselines, improving single-attempt accuracy and broadening reasoning coverage. Code is available at https://github.com/louieworth/trd
