---
source: farmer/huggingface
farmed: 2026-09-22T11:38:12.626404+05:30
arxiv_id: 2609.22220
url: https://huggingface.co/papers/2609.22220
arxiv_url: https://arxiv.org/abs/2609.22220
date: 2026-09-22
---

# Measuring the Checker: Mutation Analysis for GPU-Kernel Benchmark Oracles

Benchmarks for LLM-generated GPU kernels decide correctness with a few random inputs and a loose floating-point tolerance, and their verdicts now feed leaderboards and reinforcement-learning rewards. Recent work agrees these checkers are weak and patches them by hand---extra input distributions, fuzzing recipes, tighter tolerances---with no way to measure whether any patch suffices. We introduce mutation analysis as an adequacy metric for kernel-benchmark oracles: deterministic rules inject 10{,}303 compilable faults into verified CUDA implementations of 188 KernelBench problems, 7{,}384 of them with an independent kill witness; any test protocol is scored by the fraction it detects. The official check misses one in six witnessed faults (16.9%), deterministically, and the misses are skewed by family: 8.7% of arithmetic faults escape, but 78.6% of precision faults do. The metric explains why (a tolerance blind band growing with reduction size; a measured ceiling on input aggressiveness set by legitimate floating-point variance), audits the strongest existing patch (KernelBench-Verified's gain splits into +4.0 points from hidden inputs and +4.5 from tighter tolerance, a split its authors could not compute), and exposes a published fuzzing recipe that rejects correct kernels 107 times. Optimizing suites over the kill matrix reaches 98.0% detection with two inputs per problem (94.8% held-out), and the measurement's fault taxonomy teaches a test generator more than the raw faults themselves. Across 48 whole architectures, the blindness grows with scale, concentrating in deep homogeneous pipelines, and two problems prove unrefereeable: their official references violate the benchmark's own tolerance against fp64. We release everything as https://huggingface.co/datasets/Elfsong/KernelBench-M{KernelBench-M}.
