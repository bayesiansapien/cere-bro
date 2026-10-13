---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.221909+05:30
arxiv_id: 2610.13627
url: https://huggingface.co/papers/2610.13627
arxiv_url: https://arxiv.org/abs/2610.13627
date: 2026-10-12
---

# AMLworld-Compact: Importance-Weighted Downsampling for Cost-Effective LLM Evaluation and Error Diagnosis

Evaluating large language models (LLMs) on AMLworld's smallest test splits is costly because each of over a million targets requires a separate graph prompt. Sampling reduces this cost, but small balanced subsets change unweighted precision and F1. We introduce AMLworld-Compact, an evaluation set that retains every illicit test transaction and samples benign transactions from supervised-score strata. Its HT-Coreset protocol reduces evaluation targets by 271x and 611x on HI-Small and LI-Small. Horvitz-Thompson weights give unbiased full-test confusion-count estimates for fixed predictions; recall is exact, while precision and F1 are ratio estimates. In a held-out study using Graph Feature Preprocessor (GFP) features, one boosted-tree family defines strata for evaluating the other over 500 draws per configuration. At the released sizes, F1 RMSE is 0.00-2.58 percentage points versus 4.44-7.41 for uniform sampling with HT weights; conservative intervals remain broad. Under the evaluated graph prompts, seven open-weight LLMs have weighted precision near the predict-all-illicit baseline. In an outcome-stratified audit of 1,000 HI-Small few-shot outputs from one run per model, lexical checks pass for 84.5% of correct and 56.2% of incorrect binary verdicts, so these markers do not establish correctness. We release the evaluation sets, construction code, and audit tools at https://huggingface.co/datasets/typhoon-ai/AMLworldCompactEval and https://github.com/nat-nischw/AMLworld-Compact.
