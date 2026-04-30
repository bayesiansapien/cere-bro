---
source: farmer/huggingface
farmed: 2026-04-30T00:00:00Z
arxiv_id: 2604.26904
url: https://huggingface.co/papers/2604.26904
arxiv_url: https://arxiv.org/abs/2604.26904
date: 2026-04-30
---

# ClawGym: A Scalable Framework for Building Effective Claw Agents

**Authors:** Huatong Song, Shuang Sun, Daixuan Cheng, Yike Yang, Chuan Hao, Renyuan Li, Feng Chang, Yuan Wei, Ran Tao, Bryan Dai, Jian Yang, Wayne Xin Zhao (Renmin University of China, IQuest Research, Beihang University)

Claw-style environments support multi-step workflows over local files, tools, and persistent workspace states. However, scalable development around these environments remains constrained by the absence of a systematic framework, especially one for synthesizing verifiable training data and integrating it with agent training and diagnostic evaluation. To address this challenge, we present ClawGym, a scalable framework that supports the full lifecycle of Claw-style personal agent development. Concretely, we construct ClawGym-SynData, a diverse dataset of 13.5K filtered tasks synthesized from persona-driven intents and skill-grounded operations, paired with realistic mock workspaces and hybrid verification mechanisms. We then train a family of capable Claw-style models, termed ClawGym-Agents, through supervised fine-tuning on black-box rollout trajectories, and further explore reinforcement learning via a lightweight pipeline that parallelizes rollouts across per-task sandboxes. To support reliable evaluation, we further construct ClawGym-Bench, a benchmark of 200 instances calibrated through automated filtering and human-LLM review. Relevant resources will be soon released at https://github.com/ClawGym.

## Key contributions

- **ClawGym-SynData**: 13.5K tasks using dual-route synthesis (persona-driven top-down + skill-grounded bottom-up), with realistic mock workspaces and hybrid (code-based + rubric-based) verification.
- **ClawGym-Agents**: Trained via SFT on black-box rollout trajectories; RL explored via sandbox-parallel pipeline.
- **ClawGym-Bench**: 200-instance benchmark with rollout-based difficulty calibration and human-LLM review.
- **Results**: Qwen3-8B improves 38.90% on PinchBench and 43.46% on ClawGym-Bench; Qwen3-30B-A3B improves 54.68% on PinchBench and 25.96% on ClawGym-Bench.
