---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.216789+05:30
arxiv_id: 2610.13395
url: https://huggingface.co/papers/2610.13395
arxiv_url: https://arxiv.org/abs/2610.13395
date: 2026-10-12
---

# ProgramGym: Scaling Training Environments for Long-Horizon Program Reproduction Agents

Coding agents are increasingly used to build programs from scratch as software engineers do rather than to resolve issues within a repository or to generate a repository from a given requirements document. However, scalable verifiable training environments that force agents to discover what is required and to decide how the system should be designed remain scarce. Moreover, existing agent workflows also cannot sustain long-horizon development in which the agent explores the reference program before implementation. To address these challenges, we introduce ProgramGym, a framework consisting of Program-Env and Program-Agent for scalable training environments of long-horizon program reproduction agents. Specifically, Program-Env constructs verifiable training environments from repositories through a feedback-driven loop that repairs runtime sandbox builds and the quality of black-box tests. Using this novel pipeline, we obtain 1,648 training environments spanning C, C++, Go, and Rust. Program-Agent combines a role-isolated workflow of analysis, implementation, and review with revision management for compilation checks and failure recovery. Experiments on ProgramBench show that both Program-Env and Program-Agent improve performance on program reproduction. Fine-tuning on trajectories with these constructed environments raises the performance of Qwen3.8-27B from 34.87% to 42.84%. Program-Agent further raises the base and SFT models to 55.71% and 56.25%, both exceeding some flagship models. We will release the ProgramGym to support further research on coding agents that build programs from scratch.
