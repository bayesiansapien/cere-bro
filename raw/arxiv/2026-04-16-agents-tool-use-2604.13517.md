---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13517
category: cs.AI
concept: agents-tool-use
url: https://arxiv.org/abs/2604.13517
published: 2026-04-16
authors: Jing Sun
---

# Representation over Routing: Overcoming Surrogate Hacking in Multi-Timescale PPO

**arXiv:** https://arxiv.org/abs/2604.13517
**Authors:** Jing Sun

## Abstract

arXiv:2604.13517v1 Announce Type: cross  Abstract: Temporal credit assignment in reinforcement learning has long been a central challenge. Inspired by the multi-timescale encoding of the dopamine system in neurobiology, recent research has sought to introduce multiple discount factors into Actor-Critic architectures, such as Proximal Policy Optimization (PPO), to balance short-term responses with long-term planning. However, this paper reveals that blindly fusing multi-timescale signals in complex delayed-reward tasks can lead to severe algorithmic pathologies. We systematically demonstrate that exposing a temporal attention routing mechanism to policy gradients results in surrogate objective hacking, while adopting gradient-free uncertainty weighting triggers irreversible myopic degeneration, a phenomenon we term the Paradox of Temporal Uncertainty. To address these issues, we propose a Target Decoupling architecture: on the Critic side, we retain multi-timescale predictions to enforce auxiliary representation learning, while on the Actor side, we strictly isolate short-term signals and update the policy based solely on long-term advantages. Rigorous empirical evaluations across multiple independent random seeds in the LunarLander-v2 environment demonstrate that our proposed architecture achieves statistically significant performance improvements. Without relying on hyperparameter hacking, it consistently surpasses the ''Environment Solved'' threshold with minimal variance, completely eliminates policy collapse, and escapes the hovering local optima that trap single-timescale baselines.
