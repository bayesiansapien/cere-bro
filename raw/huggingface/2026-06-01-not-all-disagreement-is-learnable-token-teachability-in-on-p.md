---
source: farmer/huggingface
farmed: 2026-06-01T09:02:45Z
arxiv_id: 2605.26844
url: https://huggingface.co/papers/2605.26844
arxiv_url: https://arxiv.org/abs/2605.26844
date: 2026-06-01
---

# Not All Disagreement Is Learnable: Token Teachability in On-Policy Distillation

On-policy distillation (OPD) trains a student on its own rollouts with token-level teacher supervision. Recent selective OPD methods exploit the non-uniformity of OPD signals by prioritizing high-entropy or high-disagreement tokens. We revisit this principle and ask: which token-level teacher signals are actually learnable? Using a fixed-context diagnostic that measures same-context teacher-student KL reduction, we show that raw KL disagreement is a coarse proxy for learning value. It conflates learnable disagreement, where the teacher assigns corrective mass to the student's top-K candidates, with incompatible disagreement, where the teacher places mass mostly off the student's current support. We formalize this local compatibility as token teachability and show that it better predicts fixed-context improvement than raw KL alone. Motivated by this finding, we propose Teachability-Aware OPD (TA-OPD), a lightweight token-position selection method that applies OPD loss to high-teachability positions without reward models or verifiers. Across Qwen2.5 and Qwen 3 teacher-student settings, TA-OPD often surpasses full-token OPD with only 5% retained tokens and improves over entropy- and divergence-based baselines. Our results reframe selective OPD as selecting learnable teacher signals rather than merely salient tokens.
