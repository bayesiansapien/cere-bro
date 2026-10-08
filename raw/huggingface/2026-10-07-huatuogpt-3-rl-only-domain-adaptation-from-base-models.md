---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.05966
url: https://huggingface.co/papers/2610.05966
arxiv_url: https://arxiv.org/abs/2610.05966
date: 2026-10-07
---

# HuatuoGPT-3: RL-Only Domain Adaptation from Base Models

Domain adaptation aims to turn a general-purpose large language model (LLM) into an expert for a target domain. While the dominant SFT+RL pipeline offers a convenient cold start, it may reduce exploration diversity and introduces additional complexity through multi-stage optimization. These limitations motivate RL-only adaptation. However, pure on-policy RL suffers from a cold-start problem, while mixed-policy RL still falls short: informative tokens in teacher outputs are learned too slowly in early training, and stale teacher outputs can hinder later improvement. We identify these two failure modes as Gradient Starvation and Teacher-Distribution Anchoring. To address them, we propose One-stage Policy Optimization (OnePO), which treats teacher outputs as transient guidance for policy improvement. OnePO combines Adaptive Objective Evolution to strengthen learning on informative low-probability teacher tokens and Teacher Retirement to discard teacher outputs once the current policy can surpass them. On medical adaptation, OnePO achieves 67.2 on HealthBench (Total) with only 20K training samples, outperforming SFT+RL and pure RL by 2.7 and 7.4 points, respectively. We further scale OnePO to produce HuatuoGPT-3, an open-source medical LLM series whose 27B variant reaches 70.1 on HealthBench (Total) and 71.4 on HealthBench Professional, surpassing frontier models such as GPT-6 Astra. Models and code are available at https://github.com/FreedomIntelligence/HuatuoGPT-3.
