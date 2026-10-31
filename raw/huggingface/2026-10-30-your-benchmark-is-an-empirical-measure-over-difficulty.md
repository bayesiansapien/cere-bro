---
source: farmer/huggingface
farmed: 2026-10-31T08:06:35.156116+00:00
arxiv_id: 2610.29927
url: https://huggingface.co/papers/2610.29927
arxiv_url: https://arxiv.org/abs/2610.29927
date: 2026-10-30
---

# Your Benchmark Is an Empirical Measure Over Difficulty

A benchmark is not merely a collection of test questions; it naturally induces an empirical measure over difficulty. In this work, we develop this measure-based view of benchmark evaluation. This perspective allows us to identify and formalize two central failure modes: measure mismatch, where the benchmark difficulty distribution differs from the intended difficulty distribution, and coverage gaps, where uncovered regions along the difficulty axis prevent benchmarks from detecting meaningful localized training progress. We propose two diagnostic metrics that capture these two failure modes and provide rigorous theoretical guarantees. Empirically, we analyze 25 popular benchmarks spanning 7 domains using carefully estimated item difficulties. Our results show that many benchmarks implicitly overweight certain difficulty regions, so their leaderboard conclusions should be interpreted with caution; others leave substantial portions of the difficulty axis uncovered, limiting their ability to monitor the model improvement process. Finally, we turn diagnosis into action by introducing BenchFill, a simple difficulty-targeted item rewriting algorithm that effectively reduces local coverage gaps.
