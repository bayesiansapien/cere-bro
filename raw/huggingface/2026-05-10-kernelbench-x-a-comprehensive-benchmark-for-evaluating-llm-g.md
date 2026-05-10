---
source: farmer/huggingface
farmed: 2026-05-10T03:37:12Z
arxiv_id: 2605.04956
url: https://huggingface.co/papers/2605.04956
arxiv_url: https://arxiv.org/abs/2605.04956
date: 2026-05-10
---

# KernelBench-X: A Comprehensive Benchmark for Evaluating LLM-Generated GPU Kernels

LLM-based Triton kernel generation has attracted significant interest, yet a fundamental empirical question remains unanswered: where does this capability break down, and why? We present KernelBench-X, a benchmark designed to answer this question through category-aware evaluation of correctness and hardware efficiency across 176 tasks in 15 categories. Key findings: task structure determines correctness more than method design (category explains 3x more variance than method); iterative refinement improves correctness but not performance (average speedup declines from 1.58x to 1.44x across iterations); 46.6% of correct kernels are slower than the PyTorch eager baseline; quantization remains completely unsolved (0/30 successes).
