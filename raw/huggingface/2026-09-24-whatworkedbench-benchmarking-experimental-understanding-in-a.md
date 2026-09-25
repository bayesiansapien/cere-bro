---
source: farmer/huggingface
farmed: 2026-09-25T17:06:04.306887+00:00
arxiv_id: 2609.27490
url: https://huggingface.co/papers/2609.27490
arxiv_url: https://arxiv.org/abs/2609.27490
date: 2026-09-24
upvotes: 8
authors: ["Jingjie Ning", "Xueqi Li", "Yibo Kong", "Dongting Li"]
---

# WhatWorkedBench: Benchmarking Experimental Understanding in AI Agents

**Authors:** Jingjie Ning, Xueqi Li, Yibo Kong, Dongting Li

**Upvotes:** 8

**Links:** [HuggingFace](https://huggingface.co/papers/2609.27490) · [arXiv](https://arxiv.org/abs/2609.27490)

AI research agents need reliable knowledge of how their experiments change outcomes. We introduce WhatWorkedBench to measure experimental understanding, the accuracy of predictions about component changes after budgeted experimentation. Agents inspect code, select measurements, and submit a response surface, a table predicting scores for every configuration of component settings. Exhaustive CPU execution supplies reference effects for changing each component while holding the others fixed. These effects capture combinations of changes across 36 tasks from 30 data sources and 8 workflow types, with 1248 configuration records. Core evaluation combines 4,206 numerical-control records across all eight families and 108 agent episodes across the original six. At eight new measurements, pair-effect ridge selects an optimum on 15 of 22 sources and limits every effect error to 10% of score range on three. Fitting a Gaussian process (GP) to the same agent observations raises effect recovery, accuracy relative to true effect magnitude, from 0.632 to 0.698 in the original Flash cohort and from 0.621 to 0.720 in an additional cohort. On six completed beat-detection and graph submissions, the same-observation GP raises family-macro recovery from 0.303 to 0.455. On six workflows with six binary options at 20 new measurements, encoding code equivalences, configurations with identical behavior, raises GP recovery from 0.248 to 0.462. WhatWorkedBench supports research on experimental agents, adaptive experimental design, numerical inference, and use of program structure.
