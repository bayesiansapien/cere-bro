---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.351628+05:30
arxiv_id: 2605.22493
url: https://huggingface.co/papers/2605.22493
arxiv_url: https://arxiv.org/abs/2605.22493
date: 2026-10-01
---

# Understanding Multimodality in Generative Behavioral Cloning

Behavioral cloning becomes challenging when the same observation admits several valid actions. We study how generative behavioral-cloning policies represent such multimodal expert behavior and identify different bottlenecks across model parameterizations. For latent-variable policies, preserving demonstrated modes requires action-conditioned information in the latent representation. Excessive posterior-prior regularization can suppress this information and prevent the policy from distinguishing demonstrated modes. Weaker or aggregate regularization can preserve mode information, but shifts the challenge to ensuring that the deployment-time prior covers the relevant latent regions. For action-space generative policies, multimodality is constrained by the smoothness of the base-to-action transport: a map with a small Lipschitz constant cannot assign substantial probability to many well-separated modes. Covering many modes therefore requires either sharp transitions in base space or off-support bridge regions in action space. Experiments on synthetic multimodal navigation and a physical-robot bimodal manipulation task support these mechanisms. In contrast, our analysis reveals limited conditional multimodality in standard robotic simulation benchmarks, where deterministic regression remains competitive.
