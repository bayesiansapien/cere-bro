---
source: farmer/huggingface
farmed: 2026-11-10T05:05:44.201973+00:00
arxiv_id: 2611.03953
url: https://huggingface.co/papers/2611.03953
arxiv_url: https://arxiv.org/abs/2611.03953
date: 2026-11-09
---

# P^2-MOPD: Accelerating Multi-Teacher On-Policy Distillation via Parameter Priors

Multi-teacher on-policy distillation consolidates expert capabilities by supervising student-generated trajectories, whereas task arithmetic offers a training-free alternative through linear parameter combinations. We view the linear combination of student and expert parameters as a single differentiable model and propose P^2-MOPD, which jointly optimizes the mixing coefficients and the student weights under the same on-policy distillation objective. Unlike task arithmetic, which stays within the span of the frozen student and expert parameters for any choice of merging coefficients, P^2-MOPD keeps the student trainable, so the experts act as parameter priors without confining it to this span. Across four domains at 1.7B and 4B scales, P^2-MOPD achieves faster and more balanced recovery than MOPD from the same initialization, surpassing its final average recovery in half the training steps. At the end of training, our 1.7B model reaches 94.7% average recovery, versus 80.9% for MOPD.
