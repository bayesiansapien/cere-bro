---
source: farmer/huggingface
farmed: 2026-05-09T03:37:34Z
arxiv_id: 2605.01640
url: https://huggingface.co/papers/2605.01640
arxiv_url: https://arxiv.org/abs/2605.01640
date: 2026-05-09
---

# Prescriptive Scaling Laws for Data Constrained Training

Training compute is increasingly outpacing the availability of high-quality data. The widely adopted Chinchilla scaling law assumes every training token is unique, limiting its ability to guide pretraining decisions in data-constrained regimes. We model the excess loss under repetition with a simple additive overfitting penalty and find that it accurately describes model behavior. Our scaling law yields qualitatively new compute-optimal allocation advice: beyond a point, further repetition is counterproductive and compute is better spent on model capacity. We show that strong weight decay (lambda=1.0) reduces the overfitting coefficient by approximately 70%, providing a scaling-law explanation for recent findings that optimal weight decay in data-constrained regimes is an order of magnitude larger than standard practice.
