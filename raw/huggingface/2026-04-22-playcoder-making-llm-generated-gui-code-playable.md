---
source: farmer/huggingface
farmed: 2026-04-22T00:00:00
arxiv_id: 2604.19742
url: https://huggingface.co/papers/2604.19742
arxiv_url: https://arxiv.org/abs/2604.19742
date: 2026-04-22
---

# PlayCoder: Making LLM-Generated GUI Code Playable

Large language models (LLMs) have transformed code generation, but their ability to generate code for applications with graphical user interfaces (GUIs), particularly games, remains underexplored. Prior code-generation benchmarks assess correctness using test cases, but this is insufficient for GUI applications. These applications are interactive and event-driven, and their correctness depends on stateful behavior over sequences of user actions. Consequently, evaluation should account for interaction flows and UI state transitions rather than relying solely on pass or fail test outcomes. To explore the performance of LLMs on GUI applications, we construct PlayEval, a repository-aware evaluation dataset from 43 multilingual (Python, TypeScript, and JavaScript) GUI applications. Different from existing GUI benchmarks which are difficult to transplant to Desktop platform, PlayEval consists of 6 major categories of GUI applications and directly supports evaluation on code generation tasks. To enable more reliable assessment beyond simple execution and unit tests, we propose Play@k, which measures whether at least one of k generated candidates yields an application that can be played end-to-end without logical errors. We further develop an LLM-based agent, PlayTester, that automates interactive evaluation by driving the GUI through task-oriented playthroughs and checking for logic violations. Through systematic evaluation, we demonstrate that 10 state-of-the-art code LLMs struggle to generate logically correct GUI applications, achieving near-zero Play@3 scores despite high compilation rates. To address these, we introduce PlayCoder, a multi-agent, repository-aware framework that writes, evaluates and refines GUI application code via closed-loop control.
