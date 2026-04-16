---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13891
category: cs.AI
concept: agents-tool-use
url: https://arxiv.org/abs/2604.13891
published: 2026-04-16
authors: Saeed Rahmani (Gavin), G\"ozde K\"orpe (Gavin), Zhenlin (Gavin)
---

# Beyond Conservative Automated Driving in Multi-Agent Scenarios via Coupled Model Predictive Control and Deep Reinforcement Learning

**arXiv:** https://arxiv.org/abs/2604.13891
**Authors:** Saeed Rahmani (Gavin), G\"ozde K\"orpe (Gavin), Zhenlin (Gavin)

## Abstract

arXiv:2604.13891v1 Announce Type: cross  Abstract: Automated driving at unsignalized intersections is challenging due to complex multi-vehicle interactions and the need to balance safety and efficiency. Model Predictive Control (MPC) offers structured constraint handling through optimization but relies on hand-crafted rules that often produce overly conservative behavior. Deep Reinforcement Learning (RL) learns adaptive behaviors from experience but often struggles with safety assurance and generalization to unseen environments. In this study, we present an integrated MPC-RL framework to improve navigation performance in multi-agent scenarios. Experiments show that MPC-RL outperforms standalone MPC and end-to-end RL across three traffic-density levels. Collectively, MPC-RL reduces the collision rate by 21% and improves the success rate by 6.5% compared to pure MPC. We further evaluate zero-shot transfer to a highway merging scenario without retraining. Both MPC-based methods transfer substantially better than end-to-end PPO, which highlights the role of the MPC backbone in cross-scenario robustness. The framework also shows faster loss stabilization than end-to-end RL during training, which indicates a reduced learning burden. These results suggest that the integrated approach can improve the balance between safety performance and efficiency in multi-agent intersection scenarios, while the MPC component provides a strong foundation for generalization across driving environments. The implementation code is available open-source.
