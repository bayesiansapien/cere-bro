---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.24960
url: https://huggingface.co/papers/2610.24960
arxiv_url: https://arxiv.org/abs/2610.24960
date: 2026-10-20
---

# CoworkEnv: Synthesizing Training Environments for Long-Horizon Cowork Agents

AI coworkers must coordinate tools, communicate across turns, and act on changing workspace state while respecting workflow constraints. Constructing training experience for these capabilities requires coherent requests, service records, tool interfaces, and grading checks. We present CoworkEnv, a capability-guided framework for synthesizing executable training environments for AI coworkers. Workflow requirements guide task construction, and programmatic validation with feedback repair checks generated specifications and grading behavior. Teacher executions yield curated demonstrations for supervised fine-tuning (SFT), while student interactions provide rollouts and rewards for reinforcement learning (RL). Using these resources, we train compact PocketWorker models. For Qwen3-VL-8B-Instruct, SFT raises the mean score from 46.6 to 64.1 on Claw-Eval, including a 31.9-point gain on Multi-turn tasks. An SFT-only extension to ClawMark demonstrates applicability across coworker benchmarks. We further compare RL training dynamics across configurations that vary reward processing and credit assignment. Improving training rewards provide preliminary evidence that the constructed environments support policy optimization.
