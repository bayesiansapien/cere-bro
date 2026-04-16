---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.10974
category: cs.LG
concept: agents-tool-use
url: https://arxiv.org/abs/2604.10974
published: 2026-04-16
authors: Mintae Kim, Koushil Sreenath
---

# Robust Adversarial Policy Optimization Under Dynamics Uncertainty

**arXiv:** https://arxiv.org/abs/2604.10974
**Authors:** Mintae Kim, Koushil Sreenath

## Abstract

arXiv:2604.10974v2 Announce Type: replace  Abstract: Reinforcement learning (RL) policies often fail under dynamics that differ from training, a gap not fully addressed by domain randomization or existing adversarial RL methods. Distributionally robust RL provides a formal remedy but still relies on surrogate adversaries to approximate intractable primal problems, leaving blind spots that potentially cause instability and over-conservatism. We propose a dual formulation that directly exposes the robustness-performance trade-off. At the trajectory level, a temperature parameter from the dual problem is approximated with an adversarial network, yielding efficient and stable worst-case rollouts within a divergence bound. At the model level, we employ Boltzmann reweighting over dynamics ensembles, focusing on more adverse environments to the current policy rather than uniform sampling. The two components act independently and complement each other: trajectory-level steering ensures robust rollouts, while model-level sampling provides policy-sensitive coverage of adverse dynamics. The resulting framework, robust adversarial policy optimization (RAPO) outperforms robust RL baselines, improving resilience to uncertainty and generalization to out-of-distribution dynamics while maintaining dual tractability.
