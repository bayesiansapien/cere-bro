---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.34962
url: https://huggingface.co/papers/2609.34962
arxiv_url: https://arxiv.org/abs/2609.34962
date: 2026-09-30
---

# ALICE: In-context, Zero-shot, Mutual Information Estimation

Estimating mutual information (MI) from samples is a central objective in a variety of scientific fields. Modern neural estimators are accurate in the large-data regime, but they fall short when data is scarce, and each must be fit anew for every distribution under study. Current estimators are moreover tied to specific data types. These constraints limit their adoption in many applications where per-distribution training is impractical and sample sizes are small.
  We present ALICE, a foundation model that removes per-distribution training, while achieving competitive estimation accuracy. Trained exclusively on a broad family of synthetic distributions, ALICE acts as an in-context estimator of rectified-flow velocity fields: conditioned on samples of an unseen distribution, it estimates that distribution's velocity field without any explicit training. MI is then obtained through a fixed identity that integrates the squared difference between the joint and conditional fields. We validate ALICE on a standard, challenging benchmark and apply it in three domains, biology, genetics, and neuroscience, whose data the model has never seen. For the first time, we show that a single model closes the gap with neural estimators trained separately for each distribution, while natively supporting different data dimensionality and sample cardinality, enabling zero-shot MI analysis across scientific domains.
