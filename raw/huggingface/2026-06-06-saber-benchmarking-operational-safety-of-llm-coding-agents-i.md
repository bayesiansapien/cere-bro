---
source: farmer/huggingface
farmed: 2026-06-06T09:05:36Z
arxiv_id: 2606.01317
url: https://huggingface.co/papers/2606.01317
arxiv_url: https://arxiv.org/abs/2606.01317
date: 2026-06-06
---

# SABER: Benchmarking Operational Safety of LLM Coding Agents in Stateful Project Workspaces

Large language models are increasingly deployed as coding agents, shifting safety from individual responses to action sequences. Existing benchmarks, however, primarily assess whether models refuse unsafe prompts, leaving impacts on stateful workspaces largely unexamined. We present SABER, a benchmark for environment-aware operational safety that places models in realistic agent-style projects and evaluates safety from the final environment state after a sequence of actions. Beyond binary safety-violation reports, SABER categorizes violations by cause, enabling analysis of model-specific safety profiles. Our evaluations show that even the best-performing model has more than a 54% harmful safety-violation rate (HSR), suggesting that current alignment remains insufficient for realistic project environments. SABER further reveals distinct safety profiles across models. Our benchmark is publicly available at https://github.com/sssr-lab/saber.
