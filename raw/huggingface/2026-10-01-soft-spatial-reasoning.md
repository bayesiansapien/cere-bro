---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.353910+05:30
arxiv_id: 2609.38717
url: https://huggingface.co/papers/2609.38717
arxiv_url: https://arxiv.org/abs/2609.38717
date: 2026-10-01
---

# Soft Spatial Reasoning

Large Vision-Language Models (LVLMs) commonly perform spatial reasoning through chain-of-thought (CoT), encoding intermediate reasoning as autoregressive sequences of discrete language tokens. Such hard thinking requires committing to a single token at each step, even when the correct spatial interpretation remains uncertain. This early commitment constitutes premature discretization: an incorrect token selection can propagate errors through subsequent reasoning. We propose Soft Spatial Reasoning, a post-training framework that introduces soft thinking for spatial tasks in LVLMs. At each intermediate reasoning step, the LVLM forms a continuous soft state by mixing token embeddings rather than selecting a single token, allowing multiple candidate continuations to influence the next step. The appropriate degree of softness, however, can vary across reasoning steps: retaining multiple candidates may preserve a useful spatial interpretation, but if those candidates imply conflicting spatial relations, mixing them may interfere with subsequent reasoning. At the core of Soft Spatial Reasoning is AdaptSoft, a controller that uses the current hidden state and predictive uncertainty to adapt the degree of softness at each reasoning step. To train AdaptSoft, we introduce a gradient-alignment learning objective that provides a step-specific learning signal for softness control without intermediate reasoning supervision. Across diverse spatial benchmarks, Soft Spatial Reasoning outperforms hard and fixed-soft CoT baselines using the same backbone, as well as a range of existing LVLMs. The source code is available at https://github.com/rafiibnsultan/Soft_Spatial_Reasoning
