---
source: farmer/huggingface
farmed: 2026-11-11T05:06:31.323634+00:00
arxiv_id: 2611.11995
url: https://huggingface.co/papers/2611.11995
arxiv_url: https://arxiv.org/abs/2611.11995
date: 2026-11-10
---

# Infrathon: Benchmarking Language Agents for Real-World, Long-Horizon AI Infra Optimization

In this work, we study whether frontier agent can continually improve real-world AI infrastructure over long horizons. We introduce Infrathon, a benchmark of diverse, long-horizon AI infrastructure optimization tasks across different levels. We evaluate six models across 150 runs with 24-hour budgets, totaling over 10,000 GPU-hours. Our results show that model rankings vary with the evaluation horizon, while 135 of the 150 runs achieve further improvements during the second half of their budgets. These findings indicate that shorter evaluations can overlook both optimization gains and changes in relative model performance. We also find agents can discover solutions that outperform human-designed baselines: Claude Opus 5.5 increases the mean KV-cache compression ratio from 6.82% with the human-designed Quant-VideoGen codec to 19.86%. Analysis of agent trajectories identifies task violations, unreliable testing, and premature completion as barriers to sustained improvement. Together, Our Infrathon framework provide resources for constructing long-horizon tasks, evaluating frontier agents, and discovering good infrastructure solutions.
