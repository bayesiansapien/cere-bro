---
source: farmer/huggingface
farmed: 2026-11-18T05:07:04.109844+00:00
arxiv_id: 2611.20882
url: https://huggingface.co/papers/2611.20882
arxiv_url: https://arxiv.org/abs/2611.20882
date: 2026-11-17
---

# Accelerate Bench: Evaluating Agents for Application-Level Program Optimization

Application optimization requires coding agents to discover useful changes and coordinate them across a complete program while preserving the required computation. We introduce Accelerate Bench, a benchmark of 32 CPU optimization tasks adapted from scientific applications and supercomputing competitions. Each task provides a working program and specifies the workload, correctness requirements, timing boundaries, and permitted edits, leaving agents to choose where and how to optimize. Public testing supports iterative development, and a separate verifier scores the final submission. On benchmark version 1.1, we evaluate 16 coding agents, each pairing a model with a harness. Their Score@1 ranges from 25.5% to 67.4%. Most of their programs are correct, and the size of the speedup separates them: the two leading agents are at least 2x faster on 22 or more of the 32 tasks, while the other fourteen reach 2x on 8 to 17 and leave 125 of their 412 correct outcomes below 1.25x. Controlled replays show why coordination across an application matters: identical source code runs between 0.29x and 2.12x depending only on build and runtime settings, and one code change is worth 1.01x or 6.4x depending on another. Accelerate Bench pairs executable workloads with agents' programs and trajectories to evaluate both their gains and the process behind them.
