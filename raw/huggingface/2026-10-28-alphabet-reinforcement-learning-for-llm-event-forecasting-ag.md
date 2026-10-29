---
source: farmer/huggingface
farmed: 2026-10-29T10:37:09.996484+05:30
arxiv_id: 2610.22684
url: https://huggingface.co/papers/2610.22684
arxiv_url: https://arxiv.org/abs/2610.22684
date: 2026-10-28
---

# AlphaBet: Reinforcement Learning for LLM Event Forecasting Agents

Forecasting an unresolved event requires finding relevant evidence and deciding how strongly it supports each outcome. Yet outcome-based training of Large Language Model (LLM) forecasters often begins with preassembled evidence at a single prediction date, leaving evidence acquisition outside the learning loop. We introduce AlphaBet, an agentic reinforcement learning (RL) framework that trains a single LLM policy to search, reason, and report probabilities across multiple pre-resolution dates. Each dated forecast is scored by a proper scoring rule against the eventual outcome, allowing one resolved event to supervise decisions under different information states. We decompose forecasting regret into an evidence-acquisition gap and a probability-reporting gap, and show that Group Relative Policy Optimization (GRPO)'s standard-deviation normalization can distort the reporting target under multi-class proper scores. On GLM-4.5-Air, AlphaBet reduces the Brier score from 0.731 to 0.626 on Forecast-Dojo and from 0.612 to 0.528 on FutureX. Controlled ablations attribute these gains to multi-date training and show that they come from improvements in both information acquisition and probability reporting. Our empirical results validate that GRPO's std normalization degrades proper-scoring-rule performance while leaving top-outcome accuracy largely unchanged.
