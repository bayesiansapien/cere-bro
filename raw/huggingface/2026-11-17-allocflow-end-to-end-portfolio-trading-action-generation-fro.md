---
source: farmer/huggingface
farmed: 2026-11-18T05:07:04.108269+00:00
arxiv_id: 2611.19937
url: https://huggingface.co/papers/2611.19937
arxiv_url: https://arxiv.org/abs/2611.19937
date: 2026-11-17
---

# AllocFlow: End-to-End Portfolio Trading Action Generation from Raw Market Data

Real-world portfolio management requires converting noisy market observations into coordinated, simultaneous allocations across multiple assets under shared capital constraints. Advances in forecasting models and alpha discovery help identify opportunities. However, traditional pipelines often decouple signal forecasting from portfolio construction, potentially misaligning learning with allocation and execution objectives. We present AllocFlow, an end-to-end flow-matching framework that directly generates joint portfolio allocations from raw multi-asset market histories. To capture dependencies among portfolio positions, AllocFlow employs a cross-asset flow Transformer conditioned on temporal market representations to generate continuous, signed position weights across all instruments jointly. To address the sample inefficiency and instability of learning continuous allocation policies from scratch, we establish a two-stage training scheme: strategy-supervised imitation shapes a structured distribution of candidate portfolios, followed by group-relative reinforcement learning (RL) that refines joint decisions using portfolio-level financial rewards and a frozen policy reference. On hourly cryptocurrency perpetual futures, RL refinement raises the annualized net return of the imitation policy from 27.79% to 51.38% and its Calmar ratio from 0.955 to 4.043, surpassing the teacher strategy on every metric, and AllocFlow reaches a Calmar ratio of 4.90 on six further months of unseen 2026 data without retraining.
