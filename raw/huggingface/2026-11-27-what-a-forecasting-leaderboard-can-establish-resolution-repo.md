---
source: farmer/huggingface
farmed: 2026-11-28T10:45:04+05:30
arxiv_id: 2611.31619
url: https://huggingface.co/papers/2611.31619
arxiv_url: https://arxiv.org/abs/2611.31619
date: 2026-11-27
---

# What a Forecasting Leaderboard Can Establish: Resolution Reporting for Zero-Shot Time-Series Models

A foundation model for time series is pretrained once and then asked to forecast series it has never seen, so the evidence for it is its score on held-out datasets. Such datasets are scarce, and a few public leaderboards carry most comparisons, yet none of them states how small a difference its datasets can detect. We call that quantity the resolution of a board and introduce Vernier, a tool that computes it from the files a board already publishes. Vernier also reports which entries a board cannot separate from its leader and whether its order changes when unrelated parties submit. GIFT-Eval resolves 6.8 rank places, and its displayed neighbours sit 0.91 apart. The ten places of its top ten hold fewer than two resolvable steps. fev-bench, Chronos Benchmark II and TIME show the same pattern: their resolution is 3.6 to 19 times the gap between neighbours. With each of its 2,554 series as an independent source, BOOM is the one board that resolves its top ten. Below the resolution the order depends on who else submitted: across four boards, rules that rank against the pool reversed 43 top-ten pairs with neither entry rerun, in one update in seven. Boards also do not record how much history a model receives. On 70 configurations, shortening it raised the error of three of four open models, two of them by 15%. We release Vernier, which runs this report with one command on any leaderboard that publishes per-dataset scores: https://github.com/therealram18/vernier
