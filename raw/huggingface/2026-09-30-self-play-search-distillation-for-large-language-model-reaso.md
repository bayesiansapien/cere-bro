---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.30936
url: https://huggingface.co/papers/2609.30936
arxiv_url: https://arxiv.org/abs/2609.30936
date: 2026-09-30
---

# Self-Play Search Distillation for Large Language Model Reasoning

Improving reasoning abilities in Large Language Models (LLMs) requires high-quality data that exposes difficult decisions, competing alternatives, and their consequences. Data scarcity is driven by the low quality of synthetic data and the cost of human labeling. We introduce Self-Play Search Distillation (SPSD), a framework for generating superhuman synthetic data via self-play of MuZero-like networks trained on board games. SPSD uses executable environments to turn search into structured reasoning problems. At each state, the expert identifies a preferred decision, plausible alternatives, plausible opponent replies, and value estimates. By converting the self-play search records into superhuman chains-of-thought, we train LLMs with environment-grounded supervision. Although trained only on self-play search records, SPSD transfers to unseen mathematics. On Qwen3-4B-Base, it raises the mean over six mathematics benchmarks from 24.1 to 36.6 while increasing the held-out-game win rate from 15% to 45%. SPSD offers an annotation-efficient way to create high-quality synthetic data for improving LLM performance in reasoning tasks.
