---
source: farmer/huggingface
farmed: 2026-08-28T14:50:07.734667+05:30
arxiv_id: 2608.26872
url: https://huggingface.co/papers/2608.26872
arxiv_url: https://arxiv.org/abs/2608.26872
date: 2026-08-28
---

# Self-OPD: On-Policy Distillation for Flow Matching Models without Teacher

On-policy distillation (OPD), which leverages a pre-trained, specialized teacher model to provide dense supervisory signals, has achieved significant success in Large Language Models (LLMs) and has recently been adapted to flow matching models. However, this paradigm suffers from two major issues: First, training a separate, task-specific teacher for every new objective incurs high computational costs. Second, the discrepancy between teacher and student distributions often leads to compounding errors along the generation trajectory. In this paper, we introduce Self-OPD, a teacher-free OPD framework for flow matching models that turns the student's own self-exploration into step-wise supervision. At each timestep, Self-OPD branches the deterministic next-state prediction into K stochastic SDE candidates, rolls them out with the ODE sampler, and compares their rewards against a deterministic self-reference baseline to obtain normalized advantages. The velocity field is optimized with an all-branch pull-push objective, where high-advantage branches attract the student and low-advantage branches repel it under direction-aware attenuation and SDE-variance normalization. For multi-objective alignment, Self-OPD fuses normalized scores at the reward level, avoiding direct gradient conflict. Experiments on single and mixed reward benchmarks show that Self-OPD outperforms prior RL and OPD methods without task-specific teachers.
