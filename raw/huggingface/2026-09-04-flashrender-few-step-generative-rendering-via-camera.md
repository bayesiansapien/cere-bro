---
source: farmer/huggingface
farmed: 2026-09-04T10:50:04.492861
arxiv_id: 2609.03563
url: https://huggingface.co/papers/2609.03563
arxiv_url: https://arxiv.org/abs/2609.03563
date: 2026-09-04
---

# FlashRender: Few-Step Generative Rendering via Camera-Controlled Video MeanFlow

We present FlashRender, a few-step generative rendering framework that retakes a source video along a target camera trajectory in seconds. We identify sampling-step-dependent camera control as a prominent manifestation of discretization error in existing multi-step generative rendering models and show that resolving this inconsistency substantially lowers denoising trajectory curvature, facilitating subsequent step distillation. To this end, we introduce Representation Transformation and Alignment (RETA), which aligns hidden source-video representations with target-video features from a frozen visual geometry model. This directly encodes the geometric transformation within the source-video stream, enabling sampling-step-consistent camera control. We then fine-tune the model with the MeanFlow objective on the lower-curvature denoising trajectory induced by RETA, allowing the model to more effectively address discretization error. Finally, we apply on-policy flow map distillation to correct self-rollout errors under fixed few-step sampling. Extensive experiments show that RETA, MeanFlow, and on-policy flow map distillation play complementary roles in few-step generative rendering. Together, they enable our approach to match multi-step baselines in video quality and geometric consistency at 25x lower sampling cost while achieving superior camera controllability, even under out-of-distribution target camera trajectories.
