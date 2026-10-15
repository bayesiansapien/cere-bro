---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.506907+00:00
arxiv_id: 2610.18092
url: https://huggingface.co/papers/2610.18092
arxiv_url: https://arxiv.org/abs/2610.18092
date: 2026-10-14
---

# LifeSearch: Benchmarking Deep Research Agents for Real-World Life and Productivity

Deep research (DR) agents address open-ended information needs through multi-step reasoning, long-horizon web search, and evidence synthesis. However, existing benchmarks primarily focus on academic research or synthetic tasks, leaving DR agents' capabilities in real-world life and professional productivity settings insufficiently evaluated. To bridge this gap, we introduce LifeSearch, a challenging benchmark comprising 203 Chinese and English tasks derived from real-user query seeds across 7 concrete life and productivity domains. With more than 4,500 hours of human annotation, we construct over 4,000 expert-written, fine-grained rubrics, covering both report-content criteria for coverage and accuracy and concrete criteria specifying values, units, dates, and URLs. We conduct extensive experiments on 12 advanced DR agents under a unified evaluation harness, systematically analyzing their performance patterns and failure modes. We find that even the best-performing frontier agent, GPT-5.6 Sol, achieves a score of only 63.4%, leaving substantial room for improvement on realistic life and professional DR tasks. We select the grading configuration by comparing candidate LLM judges against human rubric labels, and a human ranking study shows strong alignment between aggregate benchmark scores and human judgments (Spearman's ρ= 0.89, Kendall's τ= 0.81). LifeSearch provides a rigorous evaluation framework and foundation for advancing DR agents toward real-world life and productivity.
