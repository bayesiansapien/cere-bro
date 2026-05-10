---
source: farmer/huggingface
farmed: 2026-05-10T03:37:12Z
arxiv_id: 2605.01640
url: https://huggingface.co/papers/2605.01640
arxiv_url: https://arxiv.org/abs/2605.01640
date: 2026-05-10
---

# Prescriptive Scaling Laws for Data Constrained Training

Training compute is increasingly outpacing the availability of high-quality data. This shifts the central challenge from optimal compute allocation to extracting maximum value from limited data. The widely adopted Chinchilla scaling law assumes every training token is unique. This limits its ability to guide pretraining decisions in data-constrained regimes. We model the excess loss under repetition with a simple additive overfitting penalty and find that it accurately describes model behavior. Our scaling law yields qualitatively new compute-optimal allocation advice. Beyond a point, further repetition is counterproductive and compute is better spent on model capacity. We show that following our law's recommended configuration improves performance in data-constrained regimes. Finally, because our one-parameter form isolates overfitting in a single coefficient, it enables direct comparison across training configurations. As a case study, we show that strong weight decay (lambda=1.0) reduces this coefficient by approximately 70%, providing a scaling-law explanation for recent findings that optimal weight decay in data-constrained regimes is an order of magnitude larger than standard practice.
