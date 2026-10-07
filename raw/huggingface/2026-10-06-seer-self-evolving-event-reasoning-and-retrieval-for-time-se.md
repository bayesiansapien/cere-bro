---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.04109
url: https://huggingface.co/papers/2610.04109
arxiv_url: https://arxiv.org/abs/2610.04109
date: 2026-10-06
---

# SEER: Self-Evolving Event Reasoning and Retrieval for Time Series Forecasting

Real-world time series are frequently driven by exogenous events and structural shifts, rendering conventional forecasting based solely on historical numerical observations insufficient. While language models can retrieve external news, standard retrieval-augmented approaches struggle with high noise, missing signals, and an inability to reason causally about event impacts. We propose SEER (Self-Evolving Event Reasoning and Retrieval), a closed-loop framework that dynamically optimizes event conditioning for time series forecasting. SEER translates prediction errors into two decoupled feedback mechanisms: (i) a reflective retrieval memory that refines subsequent search queries and filters spurious noise, and (ii) a persistent causal knowledge base that distills transferable domain dynamics. SEER enforces strict chronological boundaries across both event retrieval and reflection, preventing look-ahead bias and data leakage. Across six volatile time-series benchmarks, SEER consistently outperforms state-of-the-art time series foundation models and language model baselines.
