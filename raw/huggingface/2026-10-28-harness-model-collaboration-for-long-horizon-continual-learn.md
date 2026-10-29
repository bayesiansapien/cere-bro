---
source: farmer/huggingface
farmed: 2026-10-29T10:37:09.995697+05:30
arxiv_id: 2610.34724
url: https://huggingface.co/papers/2610.34724
arxiv_url: https://arxiv.org/abs/2610.34724
date: 2026-10-28
---

# Harness-Model Collaboration for Long-Horizon Continual Learning

Long-horizon agents continuously encounter reusable procedural knowledge, yet existing systems typically rely either on model adaptation or external memory, trading persistent learning for rapid reuse. This limitation is especially important for Web agents that repeatedly execute related multi-step workflows. We propose HaMo, a Harness-Model collaborative framework that combines fast non-parametric experience accumulation with slow parametric adaptation. HaMo distills trajectories into strategy-level experience cards for immediate retrieval, while an experience-conditioned continual learning objective trains the model to interpret, ground, and execute retrieved strategies across changing contexts. A retrieval-coverage-based selection mechanism further identifies compact and complementary trajectories for parameter updates. Experiments show that HaMo outperforms harness-only and model-only adaptation under within-domain and cross-domain shifts, improving both retention and adaptation. These results highlight the importance of jointly preserving procedural experience and internalizing the competence to transfer and execute it across tasks.
