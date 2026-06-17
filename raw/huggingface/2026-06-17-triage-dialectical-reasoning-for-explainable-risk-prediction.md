---
source: farmer/huggingface
farmed: 2026-06-17T10:05:49Z
arxiv_id: 2606.09030
url: https://huggingface.co/papers/2606.09030
arxiv_url: https://arxiv.org/abs/2606.09030
date: 2026-06-17
---

# TRIAGE: Dialectical Reasoning for Explainable Risk Prediction on Irregularly Sampled Medical Time Series with LLMs

Clinical early warning systems built on electronic health records, in which clinical observations are recorded as irregularly sampled medical time series (ISMTS), must deliver both calibrated risk scores for patient triage and interpretable rationales that clinicians can verify. Large Language Models (LLMs) have been explored for this task, yet they collapse graded clinical risk into overconfident binary predictions. This risk polarization undermines both calibration and cross-patient comparability. To address this, we propose TRIAGE, a framework that trains an LLM to generate dialectical reasoning over competing clinical outcomes by eliciting outcome-specific rationales. This dialectical formulation mitigates risk polarization, enabling a single LLM to yield continuous risk scores grounded in explicit clinical reasoning. Evaluated on three ISMTS benchmarks, TRIAGE achieves an average AUPRC improvement of 3.3% and reduces calibration error by 81% compared to the competitive baselines. An LLM-as-a-judge assessment further shows that our rationales surpass post-hoc explanations from the baseline by 20% in clinical reasoning quality. The source code is available at https://github.com/HyeongWon-Jang/TRIAGE .
