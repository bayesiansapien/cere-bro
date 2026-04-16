---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2601.10245
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2601.10245
published: 2026-04-16
authors: Vansh Kapoor, Aman Gupta, Hao Chen
---

# TRIM: Hybrid Inference via Targeted Stepwise Routing in Multi-Step Reasoning Tasks

**arXiv:** https://arxiv.org/abs/2601.10245
**Authors:** Vansh Kapoor, Aman Gupta, Hao Chen

## Abstract

arXiv:2601.10245v2 Announce Type: replace  Abstract: Multi-step reasoning tasks like mathematical problem solving are vulnerable to cascading failures, where a single incorrect step leads to complete solution breakdown. Current LLM routing methods assign entire queries to one model, treating all reasoning steps as equal. We propose TRIM (Targeted routing in multi-step reasoning tasks), which routes only critical steps$\unicode{x2013}$those likely to derail the solution$\unicode{x2013}$to larger models while letting smaller models handle routine continuations. Our key insight is that targeted step-level interventions can fundamentally transform inference efficiency by confining expensive calls to precisely those steps where stronger models prevent cascading errors. TRIM operates at the step-level: it uses process reward models to identify erroneous steps and makes routing decisions based on step-level uncertainty and budget constraints. We develop several routing strategies within TRIM, ranging from a simple threshold-based policy to more expressive policies that reason about long-horizon accuracy-cost trade-offs and uncertainty in step-level correctness estimates. On MATH-500, even the simplest thresholding strategy surpasses prior routing methods with 5x higher cost efficiency, while more advanced policies match the strong, expensive model's performance using 80% fewer expensive model tokens. On harder benchmarks such as AIME, TRIM achieves up to 6x higher cost efficiency. All methods generalize effectively across math reasoning tasks, demonstrating that step-level difficulty represents fundamental characteristics of reasoning.
