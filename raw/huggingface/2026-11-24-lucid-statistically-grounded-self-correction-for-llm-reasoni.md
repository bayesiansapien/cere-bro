---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.931741+00:00
arxiv_id: 2611.31595
url: https://huggingface.co/papers/2611.31595
arxiv_url: https://arxiv.org/abs/2611.31595
date: 2026-11-24
---

# LUCID: Statistically Grounded Self-Correction for LLM Reasoning Evaluation

Cheap language-model raters grade chain-of-thought reasoning at scale, yet systematic step-rating errors can skew reasoning audits and solution rankings. We introduce LUCID (Loop for Unbiased Calibration via Inference-time Diagnosis), which pairs prompt self-correction with Design-based Supervised Learning (DSL). Without retraining or weight access, LUCID calibrates binary step ratings by aligning predicted and expert soundness rates. From a small expert-labeled set, LUCID summarizes rater bias in plain text and prompts the rater to re-grade unseen steps. For example, on PRM800K, GPT-5-mini grades too strictly, under-rating computation, verification, and late-trace steps most acutely. In one pass, LUCID shrinks GPT-5-mini's calibration gap from 7.8 to 0.9 percentage points in absolute predicted-expert rate difference. LUCID also halves false alarms (sound steps rated unsound) and lifts error-detection F1 on unsound steps by 32%. LUCID retains these gains with 1,000 diagnostic steps or overall-gap feedback alone. The loop also transfers across models and domains: it applies GPT-5-mini's bias profile to lift GLM-5.2's PRM800K accuracy, and it narrows calibration gaps for overly strict but capable raters across math, science, web, and logic benchmarks. Because prompt feedback shifts thresholds without improving class-balanced sound/unsound discrimination, LUCID filters re-grading with pre-/post-checks that skip already calibrated raters and roll back ineffective passes. Finally, we reuse that expert set with raw corpus ratings in DSL for calibration and regression debiasing, and apply DSL to pair-labeled steps for sound-step transitions. DSL's out-of-fold soundness probabilities lift best-of-K selection to match expert labels, while its doubly-robust estimators beat expert-only regression fits at small budgets and cut sound-step transition error by nearly two-thirds.
