---
source: farmer/huggingface
farmed: 2026-11-21T10:04:29.390717+00:00
arxiv_id: 2611.25200
url: https://huggingface.co/papers/2611.25200
arxiv_url: https://arxiv.org/abs/2611.25200
date: 2026-11-20
---

# Squoosh Bench: Evaluating UX-1 on 318 Historical Website A/B Tests

Experimentation teams must decide which proposed website changes to test with live traffic. We evaluated whether forecasts from simulated shoppers could inform that choice. We screened 412 historical website A/B tests and evaluated four systems on the 318 that ran longer than 21 days. Each system predicted an original win, a variant win, or an inconclusive result. Page roles were masked and recorded outcomes were withheld during inference. Squoosh UX-1, a model fine-tuned on human browsing data, simulated 1,000 shoppers per arm and correctly classified 267 of 318 outcomes (84.0%, 95% Wilson interval 79.5-87.6%, treating experiments as independent). Qwen3 Next 80B, the strongest general-purpose configuration on outcome accuracy, correctly classified 196 of 318 (61.6%). UX-1 favored the variant in 126 experiments. In the live tests, 118 of those variants won (93.7%), four lost, and four had inconclusive results. The remaining 192 experiments included 19 additional variant wins.
