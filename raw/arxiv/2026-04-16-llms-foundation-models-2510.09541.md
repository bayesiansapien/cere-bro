---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2510.09541
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2510.09541
published: 2026-04-16
authors: Chenyu Wang, Paria Rashidinejad, DiJia Su
---

# SPG: Sandwiched Policy Gradient for Masked Diffusion Language Models

**arXiv:** https://arxiv.org/abs/2510.09541
**Authors:** Chenyu Wang, Paria Rashidinejad, DiJia Su

## Abstract

arXiv:2510.09541v3 Announce Type: replace-cross  Abstract: Diffusion large language models (dLLMs) are emerging as an efficient alternative to autoregressive models due to their ability to decode multiple tokens in parallel. However, aligning dLLMs with human preferences or task-specific rewards via reinforcement learning (RL) is challenging because their intractable log-likelihood precludes the direct application of standard policy gradient methods. While prior work uses surrogates like the evidence lower bound (ELBO), these one-sided approximations can introduce significant policy gradient bias. To address this, we propose the Sandwiched Policy Gradient (SPG) that leverages both an upper and a lower bound of the true log-likelihood. Experiments show that SPG significantly outperforms baselines based on ELBO or one-step estimation. Specifically, SPG improves the accuracy over state-of-the-art RL methods for dLLMs by 3.6% in GSM8K, 2.6% in MATH500, 18.4% in Countdown and 27.0% in Sudoku.
