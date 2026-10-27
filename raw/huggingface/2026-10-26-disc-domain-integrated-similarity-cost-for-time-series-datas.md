---
source: farmer/huggingface
farmed: 2026-10-27T05:06:31.801092+00:00
arxiv_id: 2610.31288
url: https://huggingface.co/papers/2610.31288
arxiv_url: https://arxiv.org/abs/2610.31288
date: 2026-10-26
---

# DISC: Domain-Integrated Similarity Cost for Time-Series Dataset

The growth of time-series datasets and foundation models has made dataset comparison a central part of time-series workflows. Assessing source-target transfer before model adaptation requires similarity estimates that can summarize transfer-related dataset relationships without exhaustive source-target evaluation over every candidate pair. Many metrics have been proposed for measuring similarity between time-series datasets, but they capture different dataset relationships and vary in how well they align with downstream utility across tasks. We evaluate this gap by measuring the correlation between source-target similarity scores and downstream forecasting errors in out-of-distribution and transfer-learning settings. We propose Domain-Integrated Similarity Cost (DISC), a learnable aggregation framework that uses calibration transfer observations to select, weight, and combine similarity metrics for different downstream tasks. By integrating complementary metric values, DISC better distinguishes source-target dataset differences that matter for downstream behavior. After calibration, DISC scores source-target pairs using only their similarity-metric values and yields higher alignment than single-metric references on the reported split. These results show that time-series dataset similarity is task-dependent, and that learned metric integration provides a stronger proxy for downstream transfer behavior than manually selecting one similarity metric.
