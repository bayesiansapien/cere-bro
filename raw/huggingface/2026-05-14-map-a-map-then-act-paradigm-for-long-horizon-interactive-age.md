---
source: farmer/huggingface
farmed: 2026-05-14T00:00:00
arxiv_id: 2605.13037
url: https://huggingface.co/papers/2605.13037
arxiv_url: https://arxiv.org/abs/2605.13037
date: 2026-05-14
---

# MAP: A Map-then-Act Paradigm for Long-Horizon Interactive Agent Reasoning

Current interactive LLM agents rely on goal-conditioned stepwise planning, where environmental understanding is acquired reactively during execution rather than established beforehand. This temporal inversion leads to Delayed Environmental Perception: agents must infer environmental constraints through trial-and-error, resulting in an Epistemic Bottleneck that traps them in inefficient failure cycles. Inspired by human affordance perception and cognitive map theory, we propose the Map-then-Act Paradigm (MAP), a plug-and-play framework that shifts environment understanding before execution. MAP consists of three stages: (1) Global Exploration, acquiring environment-general priors; (2) Task-Specific Mapping, constructing a structured cognitive map; and (3) Knowledge-Augmented Execution, solving tasks grounded on the map. Experiments show consistent gains across benchmarks and LLMs. On ARC-AGI-3, MAP enables frontier models to surpass near-zero baseline performance in 22 of 25 game environments. We further introduce MAP-2K, a dataset of map-then-act trajectories, and show that training on it outperforms expert execution traces, suggesting that understanding environments is more fundamental than imitation.
