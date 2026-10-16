---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.224756+05:30
arxiv_id: 2610.19128
url: https://huggingface.co/papers/2610.19128
arxiv_url: https://arxiv.org/abs/2610.19128
date: 2026-10-15
---

# CLASHarness: Benchmarking Multi-Agent Conflict in Computer Use via a Controllable and Verifiable Generation Pipeline

Vision-language models (VLMs) are increasingly deployed in multi-agent systems to automate complex computer-use workflows, yet existing benchmarks mostly assume consistent, cooperative environments. In contrast, real-world collaboration rarely runs on consistent information: peer or sub-agents frequently report outdated states, issue contradictory instructions, or compete over shared permissions and files, forcing agents to check others' outputs and verify ground truth in the environment. Evaluating such conflict resolution remains challenging: manual authoring cannot scale across complex systems, while unconstrained LLM generation produces narrative drift, answer leakage, and unsatisfiable rubrics. We introduce CLASHarness (Conflict-Loaded Agent Scenario Harness), a controllable framework for generating verifiable multi-agent conflicts in computer use, with a benchmark of 600 multi-round tasks. By combining hierarchical scenario planning with an eight-step verified micro-pipeline, CLASHarness pre-commits decisive visual facts before rendering and compiles hybrid code and semantic graders directly from executed reference trajectories, guaranteeing every task is solvable by construction. Evaluating 15 frontier models on CLASHarness reveals three core bottlenecks. First, when sub-agent outputs conflict with the environment, weaker models blindly follow misleading information, whereas stronger models inspect visual evidence to verify ground truth. Second, resolving conflicts is much harder than finding them: while agents can spot inconsistencies, actively fixing system state drops task success significantly. Third, coordination protocols remain a universal bottleneck: even frontier models fail over 58% of closing actions, often forgetting to release shared locks or hand off tasks. CLASHarness provides a scalable, verifiable foundation for building reliable multi-agent systems.
