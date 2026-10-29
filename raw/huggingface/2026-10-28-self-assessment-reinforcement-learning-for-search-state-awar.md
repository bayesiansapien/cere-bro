---
source: farmer/huggingface
farmed: 2026-10-29T10:37:09.996351+05:30
arxiv_id: 2610.30435
url: https://huggingface.co/papers/2610.30435
arxiv_url: https://arxiv.org/abs/2610.30435
date: 2026-10-28
---

# Self-Assessment Reinforcement Learning for Search-State Awareness in Retrieval-Augmented Large Language Models

Recent advances in search agents have enabled large language models to tackle complex tasks by retrieving and synthesizing external information. However, existing search agents often lack search-state awareness, i.e., the ability to recognize what information has been obtained and what remains missing, leading to hallucinated reasoning and prematurely terminated search. To address this limitation, we propose Self-Assessment Reinforcement Learning (SARL), a reinforcement learning framework in which models learn to recognize their own search state during training and improve their search behavior accordingly, without requiring additional assessment at test time. SARL achieves this through a dual reward design that captures the corrective effect of each assessment while penalizing excessive reliance on it, jointly encouraging effective and efficient search trajectories. Under this setup, SARL achieves a 24.3% relative improvement over the strongest baseline, with average gains of 35.9% on multi-hop reasoning and 27.9% on deep research benchmarks against the strongest per-benchmark baselines. SARL further surpasses methods built on auxiliary supervision or multi-agent coordination, despite operating as a standalone RL framework with no inference-time scaffolding. Beyond final performance, SARL maintains training stability under extended search horizons, a regime where existing methods consistently degrade, enabling sustained gains as task complexity grows.
