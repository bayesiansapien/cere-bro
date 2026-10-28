---
source: farmer/huggingface
farmed: 2026-10-28T10:37:11+05:30
arxiv_id: 2610.34386
url: https://huggingface.co/papers/2610.34386
arxiv_url: https://arxiv.org/abs/2610.34386
date: 2026-10-27
---

# ParetoRSI-Gym: Can AI Agents Improve Language Models Across Multiple Domains?

Recursive self-improvement (RSI) requires an agentic system to design, train, and evaluate its own successor. Data-driven post-training is a central part of that loop, yet existing evaluations measure it on a single benchmark, where an agent selects from a static pool or distills a stronger model to push one score up in one run. Real post-training is multi-domain, and a gain in one domain has to be weighed against a regression in another. We propose ParetoRSI-Gym, in which an agent searches for data, curates it, trains, reads back per-domain results, and repeats, with everything but the data held fixed: the initial LLM, the five domains (math, code, finance, medicine, science), the toolset, and the SFT pipeline. Generalization benchmarks in each domain separate capability gains from overfitting to the scores the agent optimizes against. Across three agent systems, three base models, five rounds and multiple seeds, the strongest system, Claude Code with Opus-5, raises the generalization scores of its proxy-best checkpoint by 9.2% relative to the starting model (+2.3 absolute points), averaged with equal weight over three base models and five domains, with a single-domain relative gain of up to 63% (medicine on Ministral-3-3B). Further analysis shows that the harness matters as much as the model it drives, and that each agent keeps a unique data selection strategy. We see our work as a step towards evaluation of RSI systems in real-world machine learning engineering.
