---
source: farmer/huggingface
farmed: 2026-04-22T00:00:00
arxiv_id: 2604.19341
url: https://huggingface.co/papers/2604.19341
arxiv_url: https://arxiv.org/abs/2604.19341
date: 2026-04-22
---

# Evaluation-driven Scaling for Scientific Discovery

Language models are increasingly used in scientific discovery to generate hypotheses, propose candidate solutions, implement systems, and iteratively refine them. At the core of these trial-and-error loops lies evaluation: the process of obtaining feedback on candidate solutions via verifiers, simulators, or task-specific scoring functions. We introduce Simple Test-time Evaluation-driven Scaling (SimpleTES), a general framework that strategically combines parallel exploration, feedback-driven refinement, and local selection, revealing substantial gains unlocked by scaling evaluation-driven discovery loops along the right dimensions. Across 21 scientific problems spanning six domains, SimpleTES discovers state-of-the-art solutions using gpt-oss models, consistently outperforming both frontier-model baselines and sophisticated optimization pipelines. Particularly, we sped up the widely used LASSO algorithm by over 2x, designed quantum circuit routing policies that reduce gate overhead by 24.5%, and discovered new Erdos minimum overlap constructions that surpass the best-known results. Beyond novel discoveries, SimpleTES produces trajectory-level histories that naturally supervise feedback-driven learning.
