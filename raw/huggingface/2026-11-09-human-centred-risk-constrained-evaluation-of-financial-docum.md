---
source: farmer/huggingface
farmed: 2026-11-10T05:05:44.205803+00:00
arxiv_id: 2611.02775
url: https://huggingface.co/papers/2611.02775
arxiv_url: https://arxiv.org/abs/2611.02775
date: 2026-11-09
---

# Human-Centred, Risk-Constrained Evaluation of Financial Document Recognition: Evidence, Critical Errors, and Selective Automation

Financial document recognition is often assessed using character and word error rates, although these metrics do not express whether a system preserves the financial facts on which people and organisations act. This paper develops a human-centred, risk-constrained framework for evaluating financial document recognition as evidence recovery and decision support. It defines typed financial facts linked to visible source regions and separates verbatim transcription, deterministic normalization, and business interpretation. A layered quality model covers text, localization, layout, tables, fields, fact correctness, evidence grounding, uncertainty, robustness, and operational performance. Non-compensatory acceptance gates use one-sided uncertainty bounds for critical-field errors, preventing strong aggregate scores from masking failures in amounts, identifiers, signs, periods, or entity associations. Selective automation is formulated as a constrained routing problem that accounts for residual risk, human-review capacity, and review cost. The framework further specifies annotation and adjudication procedures, leakage-resistant benchmark partitions, statistical estimands, subgroup analyses, and a reproducibility card. Formal results establish the limitations of compensatory scoring, the non-zero upper risk bound after zero observed errors, and a loss sensitive decision rule for routing uncertain cases to human review. The contribution is theoretical and methodological; no new model, dataset, or empirical performance result is claimed.
