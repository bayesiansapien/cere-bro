---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.30017
url: https://huggingface.co/papers/2611.30017
arxiv_url: https://arxiv.org/abs/2611.30017
date: 2026-11-25
---

# OWE-Bench: A long-horizon benchmark for measuring real-world engineering

We present OWE-Bench (OpenWorldEngineer-Bench), a benchmark of 26 long-horizon engineering tasks written by domain experts in software engineering, physical engineering, machine learning, and scientific computing. Tasks range from optimizing kernels and designing an aircraft, to identifying the faults responsible for an earthquake. Each task requires significant domain knowledge and engineering work, with models averaging hundreds of millions of tokens per task. Solutions are scored on practical measures such as speed, cost and accuracy, both on provided cases the agent could test against and on hidden cases that an engineer would expect from the task description. The best-performing frontier model so far, Claude Fable 5.2, scores 54.6% and averages 211 million tokens per task. We highlight two findings. First, when models are given more time, they use more test-time compute and achieve higher scores. Models also scale differently with test-time compute: GPT-6 Astra achieves higher scores at shorter time limits and at equal token use, while Claude Fable 5.2 uses more tokens at longer limits to achieve the highest overall score. Second, each model scores lower on hidden cases than on the provided cases, by an average of 18 points, which we call the deployment gap. Models also fail to predict the deployment gap, overestimating their performance on hidden test cases by an average of 21 points. We hope that OWE-Bench grounds progress toward agents whose engineering solutions perform as well in deployment as they do in testing.
