---
source: farmer/huggingface
farmed: 2026-07-30T12:41:02.128718+05:30
arxiv_id: 2607.27155
url: https://huggingface.co/papers/2607.27155
arxiv_url: https://arxiv.org/abs/2607.27155
date: 2026-07-30
---

# OmegaUse-OfficeVal: Benchmarking LLM Agents on Long-Horizon Office-Suite Tasks with Economic Grounding

Large language model (LLM) agents are increasingly expected to assist users in completing tasks. However, existing benchmarks provide limited support for evaluating whether agents can carry out office-suite workflows at a reasonable cost. We introduce OmegaUse-OfficeVal, a benchmark for evaluating LLM agents on long-horizon office-suite tasks with task-level economic grounding. The benchmark comprises 100 tasks derived from office-suite requests proposed by practitioners and adapted through a privacy-preserving process. On average, these tasks require 2.32 hours of human labor to complete. An important feature of the benchmark is that each task is paired with two economic signals: human labor time and task price proxy. These signals enable direct comparisons between human costs and LLM inference costs, as well as value-weighted evaluation. To support stable evaluation, we develop code-based verifiers from fine-grained rubrics. We evaluate several frontier LLMs together with a human baseline. Although all evaluated LLMs are substantially cheaper and faster than human workers, they have not yet approached human-level deliverable quality. The code and dataset are fully open-sourced, and more information is available on our project website: https://omegause-officeval.github.io.
