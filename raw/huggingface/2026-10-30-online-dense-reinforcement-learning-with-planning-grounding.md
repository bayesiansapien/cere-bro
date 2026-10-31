---
source: farmer/huggingface
farmed: 2026-10-31T08:06:35.160564+00:00
arxiv_id: 2610.39264
url: https://huggingface.co/papers/2610.39264
arxiv_url: https://arxiv.org/abs/2610.39264
date: 2026-10-30
---

# Online Dense Reinforcement Learning with Planning-Grounding Agent for UI Navigation on Live IOS Apps

While frontier vision-language models demonstrate strong capabilities in user interface (UI) navigation, their high inference costs prohibit everyday use. Conversely, smaller models trained via supervised fine-tuning (SFT) or offline reinforcement learning often memorize static trajectories, leading to brittle execution and an inability to recover from errors. To address these limitations, we propose a novel online reinforcement learning framework that trains UI navigation agents directly on live iOS applications. Our framework decouples the agent into two specialized components: a Planning agent and a UI Grounding model. We rely on an LLM-as-a-Judge to provide comprehensive reward signals, combining dense, step-level feedback to evaluate intermediate progress with a terminal reward for overall task completion. To effectively leverage this dual reward structure, we optimize the agent using Proximal Policy Optimization (PPO) with step-level advantage estimation. Furthermore, we introduce GiGPPO, a novel neighbor-conditioned value estimation method that improves critic stability by leveraging reward signals from visually similar states across concurrent trajectories. To support this online training paradigm at scale, we introduce an efficient infrastructure that orchestrates hundreds of concurrent virtual iOS devices. Evaluations on rigorous benchmarks, including UINavBench, iOSWorld, and AndroidWorld, demonstrate that our online RL trained agents substantially outperform both SFT and terminal-only RL baselines while accelerating training convergence. Notably, our 8B RL agents achieve nearly a sevenfold improvement over the SFT baseline in out-of-distribution generalization to Android environments, while outperforming Gemini-3.5-Flash and tying with Gemini-3.1-Pro on real iOS applications.
