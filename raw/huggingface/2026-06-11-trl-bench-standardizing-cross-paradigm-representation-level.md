---
source: farmer/huggingface
farmed: 2026-06-11T08:27:36Z
arxiv_id: 2606.09323
url: https://huggingface.co/papers/2606.09323
arxiv_url: https://arxiv.org/abs/2606.09323
date: 2026-06-11
---

# TRL-Bench: Standardizing Cross-Paradigm Representation-Level Evaluation of Tabular Encoders

Tabular encoders are usually evaluated inside task-specific end-to-end pipelines, so models from different training paradigms are difficult to compare directly even when they operate on similar tabular signals. We introduce TRL-Bench, a multi-granular tabular representation learning (TRL) benchmark that standardizes cross-paradigm representation-level evaluation: each encoder exports row-, column-, or table embeddings through its supported wrapper, and shared lightweight heads probe them across three suites: TRL-CTbench (column/table), TRL-Rbench (row), and TRL-DLTE (compositional Data-Lake Table Enrichment spanning all three granularities). To support this standardized setting, we release curated benchmark assets and task reformulations, including 50 OpenML tables with 123 verified targets, 16 row-pair linkage rewrites, and a 47,772-table DLTE lake derived from 1,379 parent tables. Across 20 models and 16 tasks, TRL-Bench shows that once downstream conditions are standardized, encoder quality is capability-specific rather than captured by a single leaderboard. In TRL-CTbench, generic text encoders often lead on tasks with strong surface-text signal, while tabular specialists win where their pretraining objective aligns with the task. In TRL-Rbench, within-table prediction and cross-table linkage favor different training regimes, with atomic linkage performance correlating strongly with the row-matching stage of DLTE pipelines. In TRL-DLTE, the strongest pipelines combine capability-matched specialists rather than reuse a single encoder, and top end-to-end quality depends on non-additive compositional fit rather than per-stage marginal rank alone. TRL-Bench provides a common protocol for measuring reusable signal in exported tabular representations under shared downstream conditions. Code and data: https://github.com/LOGO-CUHKSZ/TRL-Bench
