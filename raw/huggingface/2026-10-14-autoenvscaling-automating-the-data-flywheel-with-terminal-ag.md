---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.508182+00:00
arxiv_id: 2610.14163
url: https://huggingface.co/papers/2610.14163
arxiv_url: https://arxiv.org/abs/2610.14163
date: 2026-10-14
---

# AutoEnvScaling: Automating the Data Flywheel with Terminal Agents

Terminal agents solve tasks in software engineering and scientific research by executing commands in a terminal. Training them via reinforcement learning (RL) requires diverse and verifiable environments, but these environments are still mostly designed by human researchers, so their supply grows only as fast as researchers can work. We introduce AutoEnvScaling, which treats environment design as a terminal task and uses agents to automate the data flywheel. A proposer agent builds new RL environments from the rollouts of the solver being trained, and the solver's new rollouts guide the next round. By turning environment generation into a terminal task, AutoEnvScaling increases the valid-environment rate by up to 25 times compared to prompt-only generation, at up to 75% lower cost per valid environment. We show that training Qwen3.5-35B-A3B on AutoEnvScaling environments from GPT-5.6-sol improves its Terminal-Bench 2.1 score by 4.3 points over the matched Tmax baseline. The broader goal of AutoEnvScaling is to enable recursive self-improvement (RSI): by making both environment generation and solving terminal tasks, it lets one model co-evolve in both roles. We show that Qwen3.6-35B-A3B, acting in both roles, gains 12.2 points on Terminal-Bench 2.1 and raises its Terminal-Bench 4.0 score from 1.6 to 3.2. The pipeline also generalizes across agentic domains, generating environments for software engineering, computer use, professional work, and GPU kernel programming. Overall, these results show a path toward agents building their own training environments, reducing human reliance and taking a core step toward RSI.
