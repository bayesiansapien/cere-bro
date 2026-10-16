---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.229709+05:30
arxiv_id: 2610.17016
url: https://huggingface.co/papers/2610.17016
arxiv_url: https://arxiv.org/abs/2610.17016
date: 2026-10-15
---

# ProbabilityBench: Model Evaluation and Calibration with Exact Ground-Truth Uncertainty

Evaluating model uncertainty on real-world data is challenging because each instance provides only a single observed label, leaving true conditional class probabilities unknown. To address this, we introduce ProbabilityBench, a benchmark that provides exact, instance-level class probabilities across three simulated text-based domains: peer review, covert information transfer, and credit risk. By explicitly defining the full data-generating process for each environment, we analytically compute both exact class probabilities and Bayes error. Furthermore, we provide a theoretical guarantee that rendering these cases into natural-language memos strictly preserves their underlying generative probabilities. This exactness enables direct measurement of reported probability quality via KL divergence. Across 16 evaluated models, most models on the observed cost-quality Pareto frontiers are decision models, including Jev and Perplexity Decider. Finally, ProbabilityBench serves as a meta-evaluation framework, leveraging known ground-truth values to benchmark the accuracy of standard calibration metrics and Bayes-error estimators themselves.
