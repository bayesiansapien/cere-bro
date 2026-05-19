---
source: farmer/huggingface
farmed: 2026-05-19T09:55:00.432604+00:00
arxiv_id: 2605.16909
url: https://huggingface.co/papers/2605.16909
arxiv_url: https://arxiv.org/abs/2605.16909
date: 2026-05-19
---

# TOBench: A Task-Oriented Omni-Modal Benchmark for Real-World Tool-Using Agents

Tool-using agents are increasingly expected to operate across realistic professional workflows, where they must interpret multimodal inputs, coordinate external tools, inspect intermediate artifacts, and revise their actions before producing a final result. Existing benchmarks, however, often evaluate tool use, computer use, and multimodal reasoning in isolation, leaving a gap between benchmark settings and end-to-end omni-modal tool use in the real world. To address this gap, we introduce MM-ToolBench, a benchmark and evaluation harness for task-oriented omni-modal tool use. MM-ToolBench contains 100 executable tasks from two macro task families, Customer Service and Intelligent Creation, covering 20 subcategory slices and supported by 27 MCP servers with 324 tools. The central design of MM-ToolBench is closed-loop multimodal verification: agents must execute tools, inspect rendered or transformed artifacts, and self-correct when outputs fail task-specific requirements. To make such evaluation scalable and verifiable, MM-ToolBench couples MCP-based execution with task-specific grounded evaluators and a semi-automated construction pipeline for scenario discovery, task instantiation, evaluator synthesis, and human audit. Experiments on 15 contemporary agentic models show that MM-ToolBench remains highly challenging: Claude Opus 4.6, commonly regarded as one of the strongest coding-agent models, achieves only 32.0% task success, far below the 94.0% human benchmark. We envision MM-ToolBench as a practical foundation for evaluating and advancing next-generation omni-modal tool-using agents through closed-loop multimodal verification.
