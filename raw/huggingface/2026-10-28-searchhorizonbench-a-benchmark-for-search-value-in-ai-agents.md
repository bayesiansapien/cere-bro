---
source: farmer/huggingface
farmed: 2026-10-29T10:37:09.995346+05:30
arxiv_id: 2610.34714
url: https://huggingface.co/papers/2610.34714
arxiv_url: https://arxiv.org/abs/2610.34714
date: 2026-10-28
---

# SearchHorizonBench: A Benchmark for Search Value in AI Agents

AI agents must decide when another search is worth its cost. Answer-success probabilities capture question difficulty, while this decision requires estimating the additional benefit of search. We introduce SearchHorizonBench, a benchmark for learning and evaluating search value from execution experience. Paired continuations and repeated executions separate expected search gain from generation noise and connect prediction quality to decision utility. The resource contains 45,632 executions across 3,168 questions. On 1,632 held-out questions, historical calibration reduces Brier error by 16.2%, with the improvement concentrated in success-level information. Search gains have a standard deviation of 21.4 percentage points, and tested historical estimators explain less than 2% of this variance in point estimates. Matched-configuration learning curves probe this distinction across training scales. At the reference token price, free selection observations yield a 2.49-point utility opportunity over the best constant action, driven primarily by gain information. Reusable histories, frozen splits, strong baselines and scoring tools provide a common foundation for developing and evaluating value-aware search agents.
