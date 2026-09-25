---
source: farmer/huggingface
farmed: 2026-09-25T22:51:58.846051
arxiv_id: 2609.28923
url: https://huggingface.co/papers/2609.28923
arxiv_url: https://arxiv.org/abs/2609.28923
date: 2026-09-25
upvotes: 2
---

# ViRDM: Taming Representation Distribution Matching for Few-Step Causal Video Generation

Few-step autoregressive (AR) video diffusion enables low-latency streaming generation, but existing post-training methods predominantly rely on Distribution Matching Distillation (DMD), requiring both a large pretrained teacher and an online critic to estimate distributional discrepancies through diffusion scores. In this work, we ask whether this resource-intensive teacher--critic stack can be eliminated by post-training only the generator against a precomputed target distribution. Drawing inspiration from representation distribution matching (RDM) for one-step image generation, we systematically study its transfer to few-step causal video generation and identify three key barriers: a memory-intractable gradient path, a distinct video optimization regime, and representation distributions that underconstrain temporal dynamics. We introduce ViRDM, a teacher- and critic-free video post-training recipe that addresses these barriers sequentially. By coupling RDM with stochastically truncated clean-exit supervision, a lightweight VAE decoder, and staged vector--Jacobian products, ViRDM makes representation distribution matching memory-feasible for multi-step causal video rollouts. We further establish effective generated-population and initialization regimes for video RDM, and introduce lightweight dynamics regularization to compensate for the underconstrained temporal dynamics. ViRDM turns three-network distillation into generator-only post-training, reducing GPU memory use and training time while improving video quality. With only 20 generator updates, the recipe reaches 84.87 on the official VBench evaluation, outperforming the previous best few-step causal baseline by 0.36, while requiring 16 A100 GPU-hours. We additionally report exploratory results demonstrating the potential of the same recipe for lower causal sampling budget and for one-, two-, and four-step bidirectional generation.
