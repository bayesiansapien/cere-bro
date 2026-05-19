---
source: farmer/huggingface
farmed: 2026-05-19T09:55:00.432604+00:00
arxiv_id: 2605.17698
url: https://huggingface.co/papers/2605.17698
arxiv_url: https://arxiv.org/abs/2605.17698
date: 2026-05-19
---

# Agent Bazaar: Enabling Economic Alignment in Multi-Agent Marketplaces

The deployment of Large Language Models (LLMs) as autonomous economic agents introduces systemic risks that extend beyond individual capability failures. As agents transition to directly interacting with marketplaces, their collective behavior can amplify volatility and mask deception at scale. We introduce the Agent Bazaar, a multi-agent simulation framework for evaluating Economic Alignment, the capacity of agentic systems to preserve market stability and integrity. We identify two failure modes: (1) Algorithmic Instability in a B2C market ("The Crash"), where firms amplify price volatility until the market collapses, and (2) Sybil Deception in a C2C market ("The Lemon Market"), where a single deceptive agent controlling multiple coordinated seller identities floods the market with fraudulent listings, eroding trust and consumer welfare. We evaluate frontier and open-weight models across both scenarios and find that models largely fail to self-regulate, with failure severity varying by model rather than by size. We propose economically aligned harnesses, Stabilizing Firms and Skeptical Guardians, that improve outcomes but remain fragile under harder market conditions. To close this gap, we train agents with REINFORCE++ using an adaptive curriculum, producing a 9B model that outperforms all evaluated frontier and open-weight models. We propose the Economic Alignment Score (EAS), a 4-component scalar metric aggregating stability, integrity, welfare, and profitability, enabling direct cross-model comparison. Our results show that economic alignment is orthogonal to general capability and can be directly trained with targeted RL.
