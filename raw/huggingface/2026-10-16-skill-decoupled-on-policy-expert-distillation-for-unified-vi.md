---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.22217
url: https://huggingface.co/papers/2610.22217
arxiv_url: https://arxiv.org/abs/2610.22217
date: 2026-10-16
---

# Skill-Decoupled On-Policy Expert Distillation for Unified Vision-Language Models

Reinforcement learning (RL) can elicit specialized visual capabilities in vision-language models (VLMs), yet jointly optimizing heterogeneous objectives often introduces cross-capability gradient conflicts. Training experts independently mitigates this interference, but direct reward optimization may entangle specialized knowledge with reward-hacking biases. This paper proposes Skill-Decoupled On-Policy Expert Distillation (SCOPED), which trains capability-specific experts and extracts explicit skills through reward-guided reflection. During on-policy distillation, these skills guide expert supervision while remaining unavailable to the unified student, encouraging it to internalize procedural knowledge without explicit skills at inference time. Across eight multimodal benchmarks, SCOPED consistently outperforms the backbone and mixed-capability RL, demonstrating the effectiveness of skill-decoupled on-policy expert distillation for integrating independently acquired capabilities. Further analyses reveal interference during joint capability optimization and suggest that skill augmentation promotes more consistent expert trajectories, greater attention to task-relevant visual evidence, and better preservation of specialized expertise in the unified student. All code and data are available at https://github.com/NEUIR/SCOPED.
