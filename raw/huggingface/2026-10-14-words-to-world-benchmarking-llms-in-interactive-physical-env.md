---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.513908+00:00
arxiv_id: 2610.15228
url: https://huggingface.co/papers/2610.15228
arxiv_url: https://arxiv.org/abs/2610.15228
date: 2026-10-14
---

# Words to World: Benchmarking LLMs in Interactive Physical Environments

Words are increasingly becoming an interface for action: large language models (LLMs) can now invoke tools, operate devices, and make decisions that affect the physical world. However, current benchmarks largely evaluate LLMs through static text responses, offline tool calls, or simulated tasks, leaving open the question of how well they can act in real physical environments. We present a benchmark for measuring LLMs in closed-loop physical interaction, where models control a harness system connected to real-world components including robotic arms, cameras, and sensors. In each task, the model must issue instructions, receive physical feedback from the environment, interpret the resulting state, and adapt its next action accordingly. This setting evaluates capabilities beyond language understanding, including grounded perception, action planning, tool selection, spatial reasoning, feedback-driven correction, and robustness to execution uncertainty. Through experiments with representative LLMs, we characterize their ability to translate linguistic reasoning into physical actions and identify common failure modes such as hallucinated state changes, poor recovery from unexpected outcomes, and unstable long-horizon plans. Our benchmark aims to provide a systematic foundation for evaluating LLMs as interactive agents that connect words, tools, and the physical world.
