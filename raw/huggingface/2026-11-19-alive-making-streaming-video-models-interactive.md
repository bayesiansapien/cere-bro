---
source: farmer/huggingface
farmed: 2026-11-20T05:04:58.139435+00:00
arxiv_id: 2611.21366
url: https://huggingface.co/papers/2611.21366
arxiv_url: https://arxiv.org/abs/2611.21366
date: 2026-11-19
---

# ALIVE: Making Streaming Video Models Interactive

Streaming video LLMs can continuously observe the world, yet often handle user requests in isolation. We introduce ALIVE, an interactive streaming video model supporting proactive monitoring, streaming task coordination, and feedback-seeking interaction. We construct ALIVE-SFT-288K and ALIVE-RL-3K for two-stage training. Contrastive supervised fine-tuning teaches when and how to respond, while reinforcement learning with Behavior-Aligned Credit Assignment (BACA) combines trajectory-level and local advantages to refine decisions, responses, and silence across multi-turn interactions. We also introduce FSI-Bench to evaluate feedback seeking and subsequent task completion. ALIVE achieves the highest overall scores among the compared models on four public benchmarks and FSI-Bench, demonstrating strong streaming understanding and interactive capabilities.
