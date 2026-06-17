---
source: farmer/huggingface
farmed: 2026-06-17T10:05:49Z
arxiv_id: 2606.17628
url: https://huggingface.co/papers/2606.17628
arxiv_url: https://arxiv.org/abs/2606.17628
date: 2026-06-17
---

# OPD-Evolver: Cultivating Holistic Agent Evolver via On-Policy Distillation

Memory has become a standard substrate for self-evolving agents, yet retaining experience is not the same as learning how to evolve through it. Existing memory agents can store trajectories, retrieve reflections, or accumulate skills, but often lack the holistic competence to select useful experience, act on it, write reusable knowledge, and maintain a growing repository. We introduce OPD-Evolver, a slow-fast co-evolution framework that cultivates such an agent evolver through on-policy self-distillation. In the fast loop, OPD-Evolver interacts with a four-level memory hierarchy to read, use, write, and maintain experience for rapid test-time evolution. In the slow loop, outcome-calibrated memory attribution and privileged hindsight distill these four abilities into the deployable policy. Across multi-domain benchmarks, OPD-Evolver surpasses memory systems such as ReasoningBank by up to 11.5%, and training-based methods such as Skill0 by ~5.8%. Further analysis shows that OPD-Evolver internalizes high-value experience and memory management, enabling OPD-Evolver-9B to challenge giant counterparts such as Qwen3.5-397B-A17B and Step-3.5-Flash, pointing beyond memory-augmented agents toward genuinely qualified agent evolvers.
