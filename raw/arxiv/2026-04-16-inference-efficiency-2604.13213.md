---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13213
category: cs.LG
concept: inference-efficiency
url: https://arxiv.org/abs/2604.13213
published: 2026-04-16
authors: Yuanqi Du, Jiajun He, Dinghuai Zhang
---

# Rare Event Analysis via Stochastic Optimal Control

**arXiv:** https://arxiv.org/abs/2604.13213
**Authors:** Yuanqi Du, Jiajun He, Dinghuai Zhang

## Abstract

arXiv:2604.13213v1 Announce Type: cross  Abstract: Rare events such as conformational changes in biomolecules, phase transitions, and chemical reactions are central to the behavior of many physical systems, yet they are extremely difficult to study computationally because unbiased simulations seldom produce them. Transition Path Theory (TPT) provides a rigorous statistical framework for analyzing such events: it characterizes the ensemble of reactive trajectories between two designated metastable states (reactant and product), and its central object--the committor function, which gives the probability that the system will next reach the product rather than the reactant--encodes all essential kinetic and thermodynamic information. We introduce a framework that casts committor estimation as a stochastic optimal control (SOC) problem. In this formulation the committor defines a feedback control--proportional to the gradient of its logarithm--that actively steers trajectories toward the reactive region, thereby enabling efficient sampling of reactive paths. To solve the resulting hitting-time control problem we develop two complementary objectives: a direct backpropagation loss and a principled off-policy Value Matching loss, for which we establish first-order optimality guarantees. We further address metastability, which can trap controlled trajectories in intermediate basins, by introducing an alternative sampling process that preserves the reactive current while lowering effective energy barriers. On benchmark systems, the framework yields markedly more accurate committor estimates, reaction rates, and equilibrium constants than existing methods.
