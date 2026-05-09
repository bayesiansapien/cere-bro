---
source: farmer/huggingface
farmed: 2026-05-09T03:37:34Z
arxiv_id: 2605.04956
url: https://huggingface.co/papers/2605.04956
arxiv_url: https://arxiv.org/abs/2605.04956
date: 2026-05-09
---

# KernelBench-X: A Comprehensive Benchmark for Evaluating LLM-Generated GPU Kernels

LLM-based Triton kernel generation has attracted significant interest, yet a fundamental empirical question remains unanswered: where does this capability break down, and why? We present KernelBench-X, a benchmark designed to answer this question through category-aware evaluation of correctness and hardware efficiency across 176 tasks in 15 categories. Task structure determines correctness more than method design: category explains nearly three times more variance in semantic correctness than method (9.4% vs. 3.3% explained deviance), and 72% of Fusion tasks fail across all five methods while Math tasks are solved consistently. Iterative refinement improves correctness but not performance. Quantization remains completely unsolved (0/30 successes) despite non-trivial compilation rates.
