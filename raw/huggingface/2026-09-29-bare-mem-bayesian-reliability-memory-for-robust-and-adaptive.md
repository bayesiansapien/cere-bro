---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.932285+00:00
arxiv_id: 2609.35551
url: https://huggingface.co/papers/2609.35551
arxiv_url: https://arxiv.org/abs/2609.35551
date: 2026-09-29
---

# BaRe-Mem: Bayesian Reliability Memory for Robust and Adaptive Agent Consultation

In multi-agent systems, reliable consultation is challenging because advisor capabilities vary across tasks, and misleading information can make consultation worse than autonomous reasoning. We introduce BaRe-Mem, an online Bayesian reliability memory for multi-agent consultation. It estimates advisor reliability based on the central model's internal belief representations and updates these estimates from historical interactions. These estimates modulate the influence of advisor responses and guide the choice between consultation and autonomous reasoning. Across nine benchmarks and six central models, BaRe-Mem is more robust to misleading advisor information than debate and majority voting. On the more challenging tasks, it remains above autonomous reasoning across all tested misleading levels. Moreover, we extend the BaRe-Mem mechanism to worker allocation in agent teams. On the MuSiQue benchmark, BaRe-Mem improves task completion over routing by historical success counts and identifies capable workers earlier.
