---
source: farmer/huggingface
farmed: 2026-06-14T07:38:18Z
arxiv_id: 2606.11409
url: https://huggingface.co/papers/2606.11409
arxiv_url: https://arxiv.org/abs/2606.11409
date: 2026-06-14
---

# Risk Under Pressure: Compute-Aware Evaluation of Adversarial Robustness in Language Models

Adversarial robustness evaluations of large language models (LLMs) typically report attack success rate (ASR) under fixed query budgets, implicitly treating all attacks as equally costly. In practice, the computational expense of different attack strategies can vary by orders of magnitude. Consequently, ASR at a fixed budget can obscure the true effort required to jailbreak a model, thereby making it hard to determine whether an attack's cost justifies its payoff to the attacker. We propose a compute-aware evaluation framework based on computational pressure, measured in cumulative floating-point operations (FLOPs), as a proxy for adversarial effort. We introduce risk-compute curves, which map compute budgets to attack risk, and derive two metrics that summarize the average pressure required for a given attack to succeed. Across ten models spanning three families and four different stages in language model training and alignment, evaluated with three attack strategies (gradient-based, iterative refinement, and template-based) on two jailbreak robustness benchmarks, we find: (1) alignment training has non-monotonic effects on compute-space robustness; (2) scaling model size reduces gradient-based attack effectiveness but has limited impact on cheaper template-based attacks; (3) gradient-based attacks optimized on a surrogate model can transfer to a separate target model, providing a way to reduce attacker costs; (4) compute cost varies by up to {approx}5{times} across harm categories within a single model; and (5) safety-aligned RL increases aggregate cost while leaving some categories disproportionately accessible. We release our framework to enable compute-aware risk assessment and evaluation.
