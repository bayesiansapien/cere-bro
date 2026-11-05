---
source: farmer/huggingface
farmed: 2026-11-05T20:36:55.368230+05:30
arxiv_id: 2611.01621
url: https://huggingface.co/papers/2611.01621
arxiv_url: https://arxiv.org/abs/2611.01621
date: 2026-11-04
---

# FinForesight: A Diagnostic Backtesting Benchmark for Deep Research Systems in Financial Forecasting

Anticipating financial outcomes requires synthesizing evolving evidence and reasoning under uncertainty, making deep research systems promising tools for forecasting. Yet evaluating forecasting ability is challenging because historical backtests may reward memorized outcomes or information retrieved after the forecast date. Live forecasting avoids direct access to realized outcomes, but feedback arrives only after events resolve. To obtain timely feedback and assess historical scores, we introduce FinForesight, a diagnostic backtesting benchmark for financial deep research systems. Across the Chinese, U.S., and Hong Kong markets, the benchmark evaluates four forecasting tasks: valuation, return ranking, event direction, and future financial fundamentals. Two capability diagnostic tasks assess counterfactual reasoning and financial calculation, scored separately from forecasting performance. Our harness-compatible framework restricts retrieved evidence to information available at the forecast date. We compare pretraining-era, resolved post-cutoff, and live evaluations to test whether controlled backtests approximate future performance. Pretraining-era scores exceed post-cutoff scores in most temporal comparisons, and stronger retrieval controls narrow the gap between post-cutoff backtests and live results. Forecasting attribution and robustness analyses reveal how scores respond to retrieval policy and how predictions respond to prompt rewrites and numerical perturbations. The code and benchmark data are publicly available.
