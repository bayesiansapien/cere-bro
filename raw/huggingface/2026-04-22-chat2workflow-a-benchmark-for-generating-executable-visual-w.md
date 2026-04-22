---
source: farmer/huggingface
farmed: 2026-04-22T00:00:00
arxiv_id: 2604.19667
url: https://huggingface.co/papers/2604.19667
arxiv_url: https://arxiv.org/abs/2604.19667
date: 2026-04-22
---

# Chat2Workflow: A Benchmark for Generating Executable Visual Workflows with Natural Language

At present, executable visual workflows have emerged as a mainstream paradigm in real-world industrial deployments, offering strong reliability and controllability. However, in current practice, such workflows are almost entirely constructed through manual engineering: developers must carefully design workflows, write prompts for each step, and repeatedly revise the logic as requirements evolve—making development costly, time-consuming, and error-prone. To study whether large language models can automate this multi-round interaction process, we introduce Chat2Workflow, a benchmark for generating executable visual workflows directly from natural language, and propose a robust agentic framework to mitigate recurrent execution errors. Chat2Workflow is built from a large collection of real-world business workflows, with each instance designed so that the generated workflow can be transformed and directly deployed to practical workflow platforms such as Dify and Coze. Experimental results show that while state-of-the-art language models can often capture high-level intent, they struggle to generate correct, stable, and executable workflows, especially under complex or changing requirements. Although our agentic framework yields up to 5.34% resolve rate gains, the remaining real-world gap positions Chat2Workflow as a foundation for advancing industrial-grade automation.
