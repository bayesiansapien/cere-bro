---
source: farmer/huggingface
farmed: 2026-11-03T14:58:56.502622+05:30
arxiv_id: 2610.40901
url: https://huggingface.co/papers/2610.40901
arxiv_url: https://arxiv.org/abs/2610.40901
date: 2026-11-02
---

# TSFLab: A Self-Improving Agent-Agnostic Workbench for Time Series Forecasting Research

As publications and products on time series forecasting (TSF) proliferate, researchers face a growing burden of analyzing existing work. First, not all publications release code. For instance, only about 20% of arXiv TSF papers have a code link in the surveyed period. Second, released code also requires manual maintenance. Thus, TSF researchers must constantly adapt or implement existing works. However, independent implementations can differ in experimental settings and are difficult to maintain. We therefore propose to use AI agents for benchmarking TSF research and even supporting autoresearch, e.g., developing new TSF models. Yet directly applying existing coding agents, such as Claude Code and Codex, is suboptimal: prohibitive costs, limited scalability to large research projects (e.g., benchmarking), and lack of self-maintenance. To address these challenges, we propose TSFLab, a self-improving agent-agnostic "workbench" that equips compatible coding agents with shared resources and tools for low-cost TSF research and continuous maintenance of research resources. Our experiments cover reproduction, benchmarking, and new method development. In reproduction and benchmarking, TSFLab improves task completion by 20-163% and cuts fresh tokens per completed task by 11-66% across baselines. A pilot study of agent-driven method development also shows improved forecasting accuracy via TSFLab, with 32.8-73.6% fewer fresh tokens and 9.2-68.8% less development time than the other settings.
