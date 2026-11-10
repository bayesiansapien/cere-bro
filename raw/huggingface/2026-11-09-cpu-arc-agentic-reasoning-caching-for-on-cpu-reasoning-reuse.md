---
source: farmer/huggingface
farmed: 2026-11-10T05:05:44.205406+00:00
arxiv_id: 2611.09891
url: https://huggingface.co/papers/2611.09891
arxiv_url: https://arxiv.org/abs/2611.09891
date: 2026-11-09
---

# CPU-ARC: Agentic Reasoning Caching for on-CPU Reasoning Reuse

Large language models reinvent the wheel all the time. They conflate task-solving with the execution of the solutions, which forces them to solve every problem from scratch. We show that once a task has been reasoned through, the application of its solution to a new problem instance can be done very efficiently and with little involvement from language models. We introduce agentic reasoning caching, a method for constructing robust CPU-executable agentic reasoning caches (ARCs) from LLM reasoning traces. ARCs show on-par performance with frontier LLMs across a range of difficult mathematical and scientific tasks, are fully explainable, continually trainable, robust to input perturbations, and 16-291x cheaper to invoke than the source model.
