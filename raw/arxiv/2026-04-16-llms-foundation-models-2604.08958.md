---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.08958
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.08958
published: 2026-04-16
authors: Mintae Kim, Koushil Sreenath
---

# WOMBET: World Model-based Experience Transfer for Robust and Sample-efficient Reinforcement Learning

**arXiv:** https://arxiv.org/abs/2604.08958
**Authors:** Mintae Kim, Koushil Sreenath

## Abstract

arXiv:2604.08958v2 Announce Type: replace-cross  Abstract: Reinforcement learning (RL) in robotics is often limited by the cost and risk of data collection, motivating experience transfer from a source task to a target task. Offline-to-online RL leverages prior data but typically assumes a given fixed dataset and does not address how to generate reliable data for transfer. We propose \textit{World Model-based Experience Transfer} (WOMBET), a framework that jointly generates and utilizes prior data. WOMBET learns a world model in the source task and generates offline data via uncertainty-penalized planning, followed by filtering trajectories with high return and low epistemic uncertainty. It then performs online fine-tuning in the target task using adaptive sampling between offline and online data, enabling a stable transition from prior-driven initialization to task-specific adaptation. We show that the uncertainty-penalized objective provides a lower bound on the true return and derive a finite-sample error decomposition capturing distribution mismatch and approximation error. Empirically, WOMBET improves sample efficiency and final performance over strong baselines on continuous control benchmarks, demonstrating the benefit of jointly optimizing data generation and transfer.
