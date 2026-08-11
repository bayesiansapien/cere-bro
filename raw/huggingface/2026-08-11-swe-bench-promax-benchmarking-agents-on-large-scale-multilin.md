---
source: farmer/huggingface
farmed: 2026-08-11T07:29:49.637235+00:00
arxiv_id: 2608.09802
url: https://huggingface.co/papers/2608.09802
arxiv_url: https://arxiv.org/abs/2608.09802
date: 2026-08-11
---

# SWE-Bench ProMax: Benchmarking Agents on Large-Scale Multilingual Code Refactoring

As AI coding agents take on increasingly complex, long-horizon software engineering tasks, existing benchmarks are rapidly saturating and their evaluation quality has come under serious scrutiny: a recent audit found that nearly 60% of unsolved SWE-bench Verified instances contain flawed tests -- either overly narrow tests that reject correct solutions or overly broad tests that check unstated requirements -- and that frontier models can verbatim reproduce gold patches from training data. Code refactoring, which requires coordinated, behavior-preserving changes across many files, offers a substantially harder and more realistic test of agent capability, yet remains underserved by current benchmarks. We introduce SWE-Bench ProMax, an expert-curated, multilingual code refactoring benchmark of 170 instances drawn from real commits across seven programming languages (Python, Java, TypeScript, Go, C, C++, and Rust). Every instance undergoes rigorous, multi-stage curation that directly addresses the quality problems identified in prior benchmarks: issue descriptions are rewritten from scratch to provide precise, unambiguous specifications, and test suites are manually reviewed to remove overly narrow and overly broad tests. Tasks with insufficient complexity or limited cross-file scope are filtered out, yielding a benchmark of challenging, large-scale refactoring tasks that average 11.4 modified files and 261.6 lines of code per instance, substantially exceeding the scale of existing benchmarks. Experiments with frontier models under two agent scaffolds show that the best model achieves only 41.2% resolve rate, confirming that SWE-Bench ProMax presents a meaningful and unsaturated challenge for current AI coding agents. Our benchmark is available at https://huggingface.co/datasets/swe-bench-promax/SWE-Bench-ProMax.
