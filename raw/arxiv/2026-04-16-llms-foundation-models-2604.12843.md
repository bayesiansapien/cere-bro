---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.12843
category: cs.CL
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.12843
published: 2026-04-16
authors: Eliya Habba, Itay Itzhak, Asaf Yehudai
---

# Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration

**arXiv:** https://arxiv.org/abs/2604.12843
**Authors:** Eliya Habba, Itay Itzhak, Asaf Yehudai

## Abstract

arXiv:2604.12843v2 Announce Type: replace  Abstract: The rapid release of both language models and benchmarks makes it increasingly costly to evaluate every model on every dataset. In practice, models are often evaluated on different samples, making scores difficult to compare across studies. To address this, we propose a framework based on multidimensional Item Response Theory (IRT) that uses anchor items to calibrate new benchmarks to the evaluation suite while holding previously calibrated item parameters fixed. Our approach supports a realistic evaluation setting in which datasets are introduced over time and models are evaluated only on the datasets available at the time of evaluation, while a fixed anchor set for each dataset is used so that results from different evaluation periods can be compared directly. In large-scale experiments on more than $400$ models, our framework predicts full-evaluation performance within 2-3 percentage points using only $100$ anchor questions per dataset, with Spearman $\rho \geq 0.9$ for ranking preservation, showing that it is possible to extend benchmark suites over time while preserving score comparability, at a constant evaluation cost per new dataset. Code available at https://github.com/eliyahabba/growing-pains
