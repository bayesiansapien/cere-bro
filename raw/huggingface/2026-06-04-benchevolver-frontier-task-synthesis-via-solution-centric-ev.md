---
source: farmer/huggingface
farmed: 2026-06-04T06:39:44Z
arxiv_id: 2606.01286
url: https://huggingface.co/papers/2606.01286
arxiv_url: https://arxiv.org/abs/2606.01286
date: 2026-06-04
---

# BenchEvolver: Frontier Task Synthesis via Solution-Centric Evolution

The rapid progress of frontier large language models has led to widespread benchmark saturation, limiting the ability of existing datasets to differentiate model capabilities or provide useful training signal. For instance, on LiveCodeBench, frontier models achieve over 99% Pass@1 on easy splits and exceed 90% Pass@1 on average across difficulty levels. Constructing new, challenging datasets typically requires substantial human effort, creating a bottleneck for progress. We introduce BenchEvolver, a solution-centric evolutionary framework that automatically transforms existing coding problems into harder variants. Rather than generating problems from scratch, BenchEvolver evolves reference solutions through structured transformations and derives corresponding statements and tests from the evolved solutions. This design grounds generation in executable semantics, enabling scalable construction of high-quality, diverse, and difficult tasks with verifiable correctness. Applying BenchEvolver to LiveCodeBench and SciCode, we obtain evolved tasks that are substantially harder while maintaining validity, reference correctness, and diversity. We further curate LiveCodeBench-Plus, a 91-problem benchmark combining evolved and difficult original LCB-v6 tasks, where frontier-model Pass@1 ranges from 27.5% to 62.6%, restoring clear discrimination among strong coding models. Importantly, evolved tasks remain challenging even for the model that generates them, enabling self-improvement. We further show that RL on evolved LCB tasks improves held-out coding performance: for gpt-oss-20b, seed+evolved training achieves +8.7 and +8.3 Pass@1 gains on LCB v6 Hard and LCB-Pro Easy, exceeding seed-only gains by 70.7% and 34.8%, respectively. Our results show that BenchEvolver can convert saturated benchmarks into frontier-level evaluation suites and reusable training signal.
