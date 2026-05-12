---
source: farmer/huggingface
farmed: 2026-05-12T00:00:00Z
arxiv_id: 2605.09608
url: https://huggingface.co/papers/2605.09608
arxiv_url: https://arxiv.org/abs/2605.09608
date: 2026-05-12
---

# Geometry Conflict: Explaining and Controlling Forgetting in LLM Continual Post-Training

Continual post-training aims to extend large language models (LLMs) with new knowledge, skills, and behaviors, yet it remains unclear when sequential updates enable capability transfer and when they cause catastrophic forgetting. Existing methods mitigate forgetting through sequential fine-tuning, replay, regularization, or model merging, but offer limited criteria for determining when incorporating new updates is beneficial or harmful. In this work, we study LLM continual post-training through three questions: What drives forgetting? When do sequentially acquired capabilities transfer or interfere? How can compatibility be used to control update integration? We address these questions through task geometry: we represent each post-training task by its parameter update and study the covariance geometry induced by the update. Our central finding is that: forgetting can be considered as a state-relative update-integration failure, it arises when the covariance geometries induced by tasks misalign with the geometry of the evolving model state. Sequential updates transfer when they remain compatible with the model state shaped by previous updates, and interfere when state-relative geometry conflict becomes high. Motivated by this finding, we propose Geometry-Conflict Wasserstein Merging (GCWM), a data-free update-integration method that constructs a shared Wasserstein metric via Gaussian Wasserstein barycenters and uses geometry conflict to gate geometry-aware correction. Across Qwen3 0.6B-14B on domain-continual and capability-continual settings, GCWM consistently outperforms data-free baselines, improving retention and final performance without replay data. These results identify geometry conflict as both an explanatory signal for forgetting and a practical control signal for LLM continual post-training.
