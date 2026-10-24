---
source: farmer/huggingface
farmed: 2026-10-24T12:49:20.888299+00:00
arxiv_id: 2610.24385
url: https://huggingface.co/papers/2610.24385
arxiv_url: https://arxiv.org/abs/2610.24385
date: 2026-10-23
---

# Bridging Exploration and Persona: Information-Directed Dueling for Test-Time Agent Personalization

Effective test-time personalization requires LLM agents to adapt to query-dependent user preferences from lightweight interaction. We study persona selection with binary comparisons between candidate responses as the online signal. We present ID-TAP, a scalable, IDS-inspired neural dueling-bandit framework for large discrete persona spaces. ID-TAP combines a query-conditioned neural utility model with a lightweight Bradley-Terry explorer, and transfers comparison evidence across related queries through similarity-weighted warm starts. The neural model shares statistical strength across queries while preserving query-specific scores, and efficient BT updates score hypothetical challengers. Across seven user-conditioned generation benchmarks under reference- and model-based preference simulators, ID-TAP achieves the strongest aggregate performance among the evaluated baselines within a fixed ten-round comparison budget. These results support information-directed challenger selection as an effective design for test-time persona adaptation.
