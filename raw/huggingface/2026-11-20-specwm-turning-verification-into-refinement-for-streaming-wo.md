---
source: farmer/huggingface
farmed: 2026-11-21T10:04:29.391162+00:00
arxiv_id: 2611.26211
url: https://huggingface.co/papers/2611.26211
arxiv_url: https://arxiv.org/abs/2611.26211
date: 2026-11-20
---

# SpecWM: Turning Verification into Refinement for Streaming World Models

Recently, video world models have advanced interactive generation, with large models offering higher quality and smaller models enabling faster inference. Existing speculative methods combine their strengths through fast draft generation and selective target regeneration guided by rewards on decoded frames. However, verification covers only the external scorer's evaluation dimensions and adds decoding and scoring costs. Moreover, these scores provide no correction, requiring costly target regeneration for rejected drafts. To address these limitations, we propose Speculative World Model (SpecWM), a unified, training-free inference framework for streaming world models. It verifies draft chunks using the target's latent velocity field. Verification also yields a reusable correction; two thresholds select Accept, Refine, or Reject. Specifically, one-step refinement reuses it to improve perceptual quality, while three-step refinement strengthens camera following and trajectory consistency. These findings motivate transition-aware refinement. On WBench Navigation, SpecWM improves visual quality at 1.63times speedup over the target and raises NavScore from the draft's 75.99 to 85.63, achieving the best quality-speed-control trade-off. Additionally, our LongSpecBench shows sustained quality and control over long, multi-turn rollouts, while experiments on Hy-Nomas validate SpecWM across backbones and denoising budgets.
