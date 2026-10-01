---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.33620
url: https://huggingface.co/papers/2609.33620
arxiv_url: https://arxiv.org/abs/2609.33620
date: 2026-09-30
---

# Learning Dynamics of Continual Learning: A Unified View of Data Attribution, Forgetting, and Plasticity Loss

Modern language models are likely to be updated throughout their lifetime rather than trained once and frozen. Each update therefore participates in a recurring cycle: decide which experience to learn from, understand what that update changes, and remain capable of learning from what comes next. We show that these challenges are governed by the same evolving update--behavior interaction. We derive a token- and layer-wise decomposition of how learning from one token changes another prediction. By separating the softmax force, shared readout geometry, and residual connections, it exposes two interaction channels and yields a forward-computable approximation. Following this interaction through time reveals a unified picture of continual adaptation. Positive interaction identifies useful experience; negative interaction produces either concentrated collision or accumulated erosion; over longer horizons, updates reshape the shared geometry mediating future learning signals, reducing their transmission. These predictions lead to effective data selection, mechanism-specific controls for interference, and a readout-based diagnostic of future learnability whose degradation predicts the benefit of restoring the readout. Across models and training regimes, the same local interaction thus explains both what an update changes now and how learning today changes what can be learned tomorrow. This view connects data attribution, forgetting, and plasticity loss as distinct regimes of the same evolving learning dynamics.
