---
source: farmer/huggingface
farmed: 2026-09-09T05:28:24.738031+00:00
arxiv_id: 2609.08404
url: https://huggingface.co/papers/2609.08404
arxiv_url: https://arxiv.org/abs/2609.08404
date: 2026-09-09
---

# Environments as Scaffold: Enriching Feedback to Bootstrap Self-Evolving Agents in Long-Horizon Tasks

Large Language Models demonstrate remarkable proficiency in static reasoning, yet training them as autonomous agents through Reinforcement Learning (RL) for long-horizon tasks is often hindered by severe reward sparsity. While conventional agent-side warming up via supervised fine-tuning (SFT) can alleviate this, it is frequently limited by data scarcity and constrained exploration. To address this, we propose a paradigm shift to environment-side adaptation by constructing Feedback-Enriched Environments (FEEs). Through a pilot study, we establish a feedback design strategy that reformulates environments by transitioning from action guidance to observation enrichment during the later stages of both intra-episode exploration and inter-episode evolution. Large-scale experiments on SciWorld and BFCL benchmarks using various Qwen3 model scales and RL algorithms such as GRPO, GSPO, and DAPO demonstrate that FEEs consistently yield performance improvements over standard settings. Furthermore, our analysis reveals that training with FEEs (1) stabilizes training dynamics by reducing entropy volatility, (2) facilitates proactive state-space exploration in difficult tasks, (3) ensures the internalization of environmental guidance into policy weights rather than acting as a mere inference-time prior, and (4) identifies intra-group feedback consistency as a critical boundary for stable optimization.
