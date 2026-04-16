---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2510.26491
category: cs.LG
concept: llms-foundation-models
url: https://arxiv.org/abs/2510.26491
published: 2026-04-16
authors: Erle Zhu, Dazhi Jiang, Yuan Wang
---

# Data-Efficient RLVR via Off-Policy Influence Guidance

**arXiv:** https://arxiv.org/abs/2510.26491
**Authors:** Erle Zhu, Dazhi Jiang, Yuan Wang

## Abstract

arXiv:2510.26491v2 Announce Type: replace  Abstract: Data selection is a critical aspect of Reinforcement Learning with Verifiable Rewards (RLVR) for enhancing the reasoning capabilities of large language models (LLMs). Current data selection methods are largely heuristic-based, lacking theoretical guarantees and generalizability. This work proposes a theoretically-grounded approach using influence functions to estimate the contribution of each data point to the learning objective. To overcome the prohibitive computational cost of policy rollouts required for online influence estimation, we introduce an off-policy influence estimation method that efficiently approximates data influence using pre-collected offline trajectories. Furthermore, to manage the high-dimensional gradients of LLMs, we employ sparse random projection to reduce dimensionality and improve storage and computation efficiency. Leveraging these techniques, we develop \textbf{C}urriculum \textbf{R}L with \textbf{O}ff-\textbf{P}olicy \text{I}nfluence guidance (\textbf{CROPI}), a multi-stage RL framework that iteratively selects the most influential data for the current policy. Experiments on models up to 7B parameters demonstrate that CROPI significantly accelerates training. On a 1.5B model, it achieves a 2.66x step-level acceleration while using only 10\% of the data per stage compared to full-dataset training. Our results highlight the substantial potential of influence-based data selection for efficient RLVR.
