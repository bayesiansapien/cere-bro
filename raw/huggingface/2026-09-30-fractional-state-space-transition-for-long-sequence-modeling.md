---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.36314
url: https://huggingface.co/papers/2609.36314
arxiv_url: https://arxiv.org/abs/2609.36314
date: 2026-09-30
---

# Fractional State Space Transition for Long Sequence Modeling

State Space Models (SSMs) compress sequence history into a bounded recurrent state, making the resulting memory law a central architectural choice for long-context performance. Most modern SSMs rely on ODE-based dynamics that lead to exponential forgetting, limiting their ability to retain information over broad temporal ranges. We introduce FRAC, a selective SSM architecture derived from fractional dynamics that replaces this exponential decay with power-law long memory. To make fractional dynamics practical, FRAC approximates the heavy-tailed target kernel with a finite-state, log-spaced sum of exponential modes. This construction turns fractional memory into an efficient recurrent module with parallel training and prefill, while retaining bounded-state autoregressive decoding. Extensive experiments, including 1.3B-parameter language modeling, demonstrate that FRAC consistently improves long-context performance over state-of-the-art SSM baselines while staying competitive on short-context. These results show that fractional dynamics provide a practical and effective prior for long-context SSMs.
