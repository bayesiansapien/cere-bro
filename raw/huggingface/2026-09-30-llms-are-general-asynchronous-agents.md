---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.35427
url: https://huggingface.co/papers/2609.35427
arxiv_url: https://arxiv.org/abs/2609.35427
date: 2026-09-30
---

# LLMs are General Asynchronous Agents

Modern LLMs are increasingly capable as autonomous agents, but they follow sequential interaction cycles: read, think, reply or call tools, repeat. Many real-world use cases are not sequential: voice assistants, embodied agents, and monitoring systems receive new inputs while they think or perform another task. Modern LLMs address this with specialized architectures for voice interaction and video streams, VLAs for robot control, asynchronous tool calling for API usage, and others. In this work, we generalize from different asynchronous tasks to general asynchronous agents that can adapt to different types of concurrency. To achieve this, we develop an asynchronous LLM framework that lets users (or the agents themselves) define inference coroutines with overlapping memory states. We showcase that Qwen 3.x models are capable of asynchronous operation for streaming video understanding, videogames, and monitoring, without task-specific training.
