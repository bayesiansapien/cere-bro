---
source: farmer/huggingface
farmed: 2026-10-29T10:37:09.996011+05:30
arxiv_id: 2610.36082
url: https://huggingface.co/papers/2610.36082
arxiv_url: https://arxiv.org/abs/2610.36082
date: 2026-10-28
---

# How Much Does the Hint Matter? Scope Conditions for Hindsight Self-Distillation in Financial Reasoning

Financial institutions operating under data-residency constraints are restricted to open-weight models small enough to locally host, which trail frontier systems on multi-step quantitative reasoning. On-policy distillation narrows such gaps by supervising a student on its own rollouts, but traditional OPD requires a strong external teacher, and on-policy self-distillation (OPSD) conditions on a full reference solution. We ask how much of that signal is necessary. We present Fin-SD, a localized hindsight self-distillation recipe for multi-step reasoning. Given a problem the student fails, the student itself identifies the first incorrect reasoning step and writes a short critique of that step. We truncate the student's trajectory immediately before the error (aiming to obtain a correct prefix), condition a frozen copy of the student on the same prefix plus the hint, and distill that hint-conditioned teacher into the student over a short rollout under reverse KL. No external model contributes a gradient. We apply Fin-SD to GPT-OSS-20B on a custom multi-step financial reasoning benchmark that requires deriving formula inputs from realistic scenarios via accounting conventions. We find: (i) replacing the critique with a generic-feedback control matches Fin-SD's entire 3.03 pp accuracy gain over the base model on the FinanceReasoning Hard subset, suggesting the gain comes from where supervision is applied, not hint content; (ii) the model writing the hint does not need to be stronger than the model receiving it: hints from same-family GPT-OSS-120B, at roughly 6x the parameters, yield no materially greater benefits than self-written hints; and (iii) Fin-SD matches on-policy self-distillation from full reference solutions on accuracy while generating 9.5% fewer tokens. With Fin-SD, general reasoning on MMLU-Pro and a fourteen-metric compliance audit on FinTrust show no material regression.
