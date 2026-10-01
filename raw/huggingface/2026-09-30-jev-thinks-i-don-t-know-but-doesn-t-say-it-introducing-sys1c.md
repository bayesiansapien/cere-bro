---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.35342
url: https://huggingface.co/papers/2609.35342
arxiv_url: https://arxiv.org/abs/2609.35342
date: 2026-09-30
---

# Jev thinks "I don't know'', but doesn't say it: Introducing Sys1Cal-v1 Dataset for Probability Calibration

The appearance of Jev marked the era of System One Models, foundation models that return structured decisions with probability distributions rather than text. Aside from low cost and great speed, Jev's central promise is that these probabilities are calibrated: such claim is not backed by any public test and available external benchmarks evaluate confidence calibration, not whether every returned option probability has the right numerical meaning. To tackle this issue, we introduce Sys1Cal-v1, a dataset of True/False questions about a proposition A for which the exact probability P(A) is known by construction. Each item is queried through the three Jev primitives - Noul, Choice and Score - and evaluated by total variation distance from the ground-truth distribution, which can be used to estimate a soft accuracy of System One Models.
  We showcase the utility of Sys1Cal-v1 as a benchmark dataset by evaluating Jev and SemIf, an open-source Choice-style baseline. In this work, however, we focus even more deeply on Jev, by studying the calibration of its Score and Choice answers. In particular, we discover a peculiar behaviour that can be explained by assuming that Jev suppresses a third truth value, going beyond True and False. In other words, in Choice answers, P(A) and P(neg A) are presented as if P(A)+P(neg A)=1, while a term P(U)neq0 is missing in the sum. Recovering P(U) leads to an improvement of median soft accuracy in Choice answers from 0.771 to 0.978, suggesting that, even in binary decisions, Jev wants to answer with a third option:``I don't know''.
