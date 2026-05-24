---
source: farmer/huggingface
farmed: 2026-05-24T05:07:38.368292+00:00
arxiv_id: 2605.15669
url: https://huggingface.co/papers/2605.15669
arxiv_url: https://arxiv.org/abs/2605.15669
date: 2026-05-24
---

# Rule2DRC: Benchmarking LLM Agents for DRC Script Synthesis with Execution-Guided Test Generation

Manufacturable chip layouts must satisfy thousands of geometry-based design rules, and design rule checking (DRC) enforces them by running executable DRC scripts on layouts. Translating natural language rules into correct DRC scripts is labor-intensive and requires specialized expertise, motivating LLM agents for DRC script synthesis and debugging. However, existing benchmarks have small evaluation sets and often evaluate scripts by code similarity rather than execution correctness, and prior machine learning-based methods either ignore execution feedback or require labeled test layouts as agent's input. To this end, we introduce Rule2DRC, a large-scale benchmark for DRC script coding agents with 1,000 rule-to-script tasks and 13,921 evaluation chip layouts for execution-based scoring. Rule2DRC provides an evaluation pipeline that measures functional correctness via DRC execution outcomes without requiring evaluation layouts as input to the agent. We also propose SplitTester, a tester agent for program selection that uses execution feedback to generate discriminative test cases and separate previously indistinguishable candidate scripts, substantially improving Best-of-N selection performance in this domain. We release the code at https://github.com/snu-mllab/Rule2DRC.
