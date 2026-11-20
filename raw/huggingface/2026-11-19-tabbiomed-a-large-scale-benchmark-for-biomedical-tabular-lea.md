---
source: farmer/huggingface
farmed: 2026-11-20T05:04:58.143737+00:00
arxiv_id: 2611.23779
url: https://huggingface.co/papers/2611.23779
arxiv_url: https://arxiv.org/abs/2611.23779
date: 2026-11-19
---

# TabBioMed: A Large-Scale Benchmark for Biomedical Tabular Learning

Recent advances in machine learning have accelerated biomedical prediction, but evaluation on structured biomedical data remains fragmented, especially for datasets with high dimensionality, large sample size, missingness, and class imbalance. We introduce TabBioMed, a large-scale benchmark of 94 curated public biomedical tabular datasets spanning electronic health records, drug discovery, genomics, transcriptomics, proteomics, metabolomics, single-cell omics, and systems biology. TabBioMed unifies these datasets through a standardized, dataset-aware preprocessing and evaluation framework, enabling reproducible comparison across classification, regression, and multi-target tasks. We benchmark 23 models across classical baselines, gradient-boosted trees, neural tabular architectures, and tabular foundation models. Foundation models deliver the strongest family-level predictive performance. However, their gains are regime-dependent: tree-based models and tuned multilayer perceptrons remain highly competitive, often dominating under inference-time or training-cost constraints. Overall, TabBioMed shows that biomedical tabular learning is strongly context-dependent, with optimal model choice depending on data regime, task type, and computational budget. We release TabBioMed with curated datasets and splits, preprocessing code, baselines, and results, providing a reproducible benchmark for practical model selection and future methods development in biomedical machine learning, available at https://github.com/AI-sandbox/TabBioMed.
