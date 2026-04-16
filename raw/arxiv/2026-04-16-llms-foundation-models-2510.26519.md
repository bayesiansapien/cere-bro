---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2510.26519
category: cs.LG
concept: llms-foundation-models
url: https://arxiv.org/abs/2510.26519
published: 2026-04-16
authors: Hsiu-Yuan Huang, Chenming Tang, Weijie Liu
---

# Think Outside the Policy: In-Context Steered Policy Optimization

**arXiv:** https://arxiv.org/abs/2510.26519
**Authors:** Hsiu-Yuan Huang, Chenming Tang, Weijie Liu

## Abstract

arXiv:2510.26519v3 Announce Type: replace  Abstract: Existing Reinforcement Learning from Verifiable Rewards (RLVR) methods, such as Group Relative Policy Optimization (GRPO), have achieved remarkable progress in improving the reasoning capabilities of Large Reasoning Models (LRMs). However, they exhibit limited exploration due to reliance on on-policy rollouts which are confined to the current policy's distribution, resulting in narrow trajectory diversity. Recent approaches attempt to expand policy coverage by incorporating trajectories generated from stronger expert models, yet this reliance increases computational cost and such advanced models are often inaccessible. To address these issues, we propose In-Context Steered Policy Optimization (ICPO), a unified framework that leverages the inherent in-context learning capability of LRMs to provide expert guidance using existing datasets. ICPO introduces mixed-policy GRPO with implicit expert forcing, which expands exploration beyond the current policy distribution without requiring advanced LRM trajectories. To further stabilize optimization, ICPO integrates expert region reject sampling to filter unreliable off-policy trajectories and annealed expert-bonus reward shaping to balance early expert guidance with later autonomous improvement. Results demonstrate that ICPO consistently enhances RLVR performance and training stability on mathematical reasoning benchmarks, revealing a scalable and effective RLVR paradigm for LRMs. Our code is available at https://github.com/Celine-hxy/ICPO.
