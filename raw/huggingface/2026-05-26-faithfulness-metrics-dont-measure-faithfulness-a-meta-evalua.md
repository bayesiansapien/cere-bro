---
source: farmer/huggingface
farmed: 2026-05-26T06:42:03Z
arxiv_id: 2605.25052
url: https://huggingface.co/papers/2605.25052
arxiv_url: https://arxiv.org/abs/2605.25052
date: 2026-05-26
---

# Faithfulness Metrics Don't Measure Faithfulness: A Meta-Evaluation with Ground Truth

Chains of thought (CoTs) have become central in interpreting and auditing behaviors of large language models. Yet growing evidence suggests that these traces often fail to faithfully represent the computations behind a model's predictions. Several faithfulness metrics have been proposed, but whether they indeed measure faithfulness remains unknown. Answering this requires ground-truth labels, which are hard to obtain since internal computations are not directly observable. Consequently, most works proposing metrics report only absolute scores or comparisons to prior metrics, and the few existing benchmarks rely on proxies like plausibility or importance, properties orthogonal to faithfulness that can mislead about whether a CoT can be trusted. We address this challenge by constructing tasks whose outputs reveal which intermediate computations must have produced them, and developing an automated labeling pipeline that yields ground-truth faithfulness labels at both the step and CoT level. Building on this methodology, we present BonaFide, a benchmark of 3,066 labeled CoTs across 13 tasks and 10 models, and use it to conduct the first systematic evaluation of prominent faithfulness metrics. Our experiments show that most metrics perform near chance, exhibit strong prediction biases and degrade on longer CoTs. The best metric reaches only 0.70 AUROC at the CoT level while another reaches 0.59 at the step level, with neither transferring across settings, while entailing prohibitively high computational cost. Our results expose fundamental gaps in current faithfulness evaluation and call for the development of more reliable and efficient metrics.
