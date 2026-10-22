---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.19439
url: https://huggingface.co/papers/2610.19439
arxiv_url: https://arxiv.org/abs/2610.19439
date: 2026-10-20
---

# Progress-Aware Distillation for Mitigating Stagnation in Small Language Model Agents

While LLM-based agent systems have demonstrated remarkable proficiency in reasoning and solving complex real-world tasks, they also come with substantial token consumption and inference latency, limiting their practical deployment. To enhance the efficiency of agent systems, recent efforts have focused on transferring agentic capabilities from large-scale models to small language models (SLMs) via supervised fine-tuning-based distillation. Nevertheless, as interaction trajectories grow longer, involving extended reasoning-action chains and extensive environmental feedback, distilled student agents tend to experience progress stagnation: becoming trapped in unproductive loops characterized by persistent failed strategies and difficulty making meaningful progress. Our systematic analysis shows that this phenomenon consistently occurs across diverse SLMs and task domains. To address this issue, we propose Progress-Aware Distillation (ProD), which explicitly detects and penalizes stagnation in student-generated trajectories. ProD encodes the stagnation gap between student and teacher into an adaptive margin for dynamically penalizing possible stagnation. By iteratively applying this procedure, ProD enables student agents to progressively approximate teacher behavior. Extensive experiments involving 8 SLMs, ranging from 0.6B to 8B parameters, on both in-domain and out-of-domain benchmarks, demonstrate that ProD substantially mitigates progress stagnation while enhancing both the success rates and task-completion efficiency of distilled SLM agents.
