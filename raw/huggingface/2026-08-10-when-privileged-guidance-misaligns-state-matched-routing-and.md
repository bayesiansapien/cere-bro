---
source: farmer/huggingface
farmed: 2026-08-10T09:04:01.722687
arxiv_id: 2608.05219
url: https://huggingface.co/papers/2608.05219
arxiv_url: https://arxiv.org/abs/2608.05219
date: 2026-08-10
---

# When Privileged Guidance Misaligns: State-Matched Routing and Contextualized Self-Distillation for Multi-Turn Agents

Privileged on-policy distillation provides dense supervision for multi-turn agents by allowing a synchronized teacher to re-score the student's response at every turn with access to training-only references, such as successful trajectories. In interactive environments, however, the student's preceding actions continually change the execution state. As the student takes different actions or completes subgoals in a different order, its rollout may reach states not covered by the reference, making the reference an unreliable source of guidance for the state actually reached. Applying privileged distillation indiscriminately therefore creates state--reference mismatch. This mismatch motivates a central objective: providing privileged reference guidance that remains compatible with the student's current execution state. We introduce State-Matched Routing and Contextualized Self-Distillation (SMRC-SD), which explicitly determines when and how a privileged trajectory should guide an on-policy student. At each turn, SMRC-SD verifies whether the student's current execution state matches a supported state along the reference trajectory. Distillation is applied only at matched states, filtering out turns for which the reference lacks locally compatible guidance. For each matched state, SMRC-SD further constructs state-conditioned teacher context from the successful trajectory, grounding supervision in the state actually reached. Across ALFWorld and WebShop, SMRC-SD consistently outperforms unconditional successful full-path distillation. With Qwen3-1.7B, it improves task success from 0.746 to 0.865 on ALFWorld and from 0.574 to 0.693 on WebShop. Controlled routing and context ablations support both selecting locally supported turns and constructing state-compatible teacher context as contributors to these gains. Code is available at https://github.com/liujunzhuo/SMRC-SD.
