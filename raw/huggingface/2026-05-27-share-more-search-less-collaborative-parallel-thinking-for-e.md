---
source: farmer/huggingface
farmed: 2026-05-27T07:52:03Z
arxiv_id: 2605.27030
url: https://huggingface.co/papers/2605.27030
arxiv_url: https://arxiv.org/abs/2605.27030
date: 2026-05-27
upvotes: 17
---

# Share More, Search Less: Collaborative Parallel Thinking for Efficient Test-Time Scaling

Test-Time Scaling (TTS) enhances the reasoning capabilities of large language models by allocating additional inference compute to explore the solution space. However, existing parallel TTS methods typically keep branches isolated during search: intermediate discoveries remain branch-private and cannot guide other branches in time. This information isolation causes substantial redundant exploration, as branches repeatedly rediscover information already found elsewhere and require more search steps to collect complete decision information needed to reach correct answers. To bridge this gap, we propose Collaborative Parallel Thinking (CPT), a training-free inference framework that enables search-time information sharing across parallel branches. CPT extracts compact intermediate information from ongoing branches, maintains a deduplicated query-level information pool, and broadcasts pool entries through the input context, allowing each branch in subsequent search steps to reuse discoveries made by other branches rather than rediscover the same information. Empirically, experiments on HMMT and AIME benchmarks show that CPT establishes a stronger accuracy--latency Pareto frontier than strong baselines across rollout budgets and model scales, highlighting search-time collaboration as an effective direction for efficient parallel TTS.
