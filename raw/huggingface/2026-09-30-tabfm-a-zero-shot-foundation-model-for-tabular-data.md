---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.37959
url: https://huggingface.co/papers/2609.37959
arxiv_url: https://arxiv.org/abs/2609.37959
date: 2026-09-30
---

# TabFM: A Zero-Shot Foundation Model for Tabular Data

Tabular machine learning typically relies on per-dataset workflows, fitting tree ensembles or running AutoML searches from scratch for every task. We present TabFM, a 400M-parameter tabular foundation model that formulates supervised tabular prediction as in-context learning. TabFM produces calibrated zero-shot predictions in a single forward pass without task-specific tuning. Trained entirely on synthetic tables generated from structural causal models, TabFM learns general tabular representations that transfer zero-shot to real-world tasks. Across all 51 benchmark datasets in TabArena (38 classification and 13 regression), zero-shot TabFM ranks first among default tabular foundation models and outperforms tuned AutoML pipelines. Two extensions over the same frozen weights improve performance further on both tracks: multi-view feature expansion with ensembling and post-hoc calibration (TabFM+), and LLM-guided, dataset-specific data processing and feature engineering (TabFM-Auto).
