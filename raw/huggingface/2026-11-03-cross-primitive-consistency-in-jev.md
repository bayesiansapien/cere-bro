---
source: farmer/huggingface
farmed: 2026-11-04T11:17:37.426675+00:00
arxiv_id: 2610.38623
url: https://huggingface.co/papers/2610.38623
arxiv_url: https://arxiv.org/abs/2610.38623
date: 2026-11-03
---

# Cross-Primitive Consistency in Jev

Jev enables efficient decision-making with large language models (LLMs) through typed querying primitives, allowing the same semantic state to be expressed in different formats, such as binary and multiple-choice queries. However, the consistency of decisions across primitives has not been systematically evaluated. This work introduces PrimaCons, a four-axis benchmark for assessing cross-primitive consistency while preserving the semantics of the query. Evaluations across three Jev sizes reveal consistency violations across all four axes. Our analysis shows that these violations follow systematic patterns and that cross-primitive discrepancies predict decision failure with a ROC-AUC of 0.91. To mitigate these inconsistencies, we propose the Cross-Primitive Residual Calibrator (CPRC), which attaches a lightweight residual network to a frozen backbone and jointly optimizes predictive accuracy and cross-primitive consistency. Under a leave-one-domain-out protocol, CPRC reduces cross-primitive inconsistency by 58.57% and improves accuracy by +2.97%., demonstrating its effectiveness in both in-domain and out-of-domain settings. Our findings establish cross-primitive consistency as a key dimension for evaluating Jev and provide a practical approach to improving the reliability of its decisions. Code and benchmark is available at https://github.com/67L1/PrimaCons-CRPR.
