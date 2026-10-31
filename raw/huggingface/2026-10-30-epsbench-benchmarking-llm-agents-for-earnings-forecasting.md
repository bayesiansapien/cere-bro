---
source: farmer/huggingface
farmed: 2026-10-31T08:06:35.161934+00:00
arxiv_id: 2610.38293
url: https://huggingface.co/papers/2610.38293
arxiv_url: https://arxiv.org/abs/2610.38293
date: 2026-10-30
---

# EPSBench: Benchmarking LLM Agents for Earnings Forecasting

Quarterly earnings forecasting requires an agent to connect financial evidence to the income-statement line items that produce a company's reported earnings. We introduce EPSBench, a benchmark for studying this ability across 149 firm-quarters from 86 US companies. Agents read a fixed collection of filings, earnings-call transcripts, and news, then estimate company-specific income-statement drivers with cited evidence. A shared accounting calculator converts these estimates into GAAP diluted earnings per share (EPS), providing a common basis for comparing forecast assumptions. We evaluate six models under a common harness, assessing point forecast error relative to date-matched analyst consensus and checking whether their prediction intervals achieve the stated coverage. Three models show no detectable paired difference in point forecast error from consensus, and three have higher error. Across all six models, nominal 80% intervals contain reported EPS in only 37--70% of runs that return an interval, and most misses fall above the upper bound because the forecasts run low. The driver records trace most of the error gap between models to operating-income estimates.
