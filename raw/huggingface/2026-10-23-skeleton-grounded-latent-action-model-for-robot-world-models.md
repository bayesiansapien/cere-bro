---
source: farmer/huggingface
farmed: 2026-10-24T12:49:20.888024+00:00
arxiv_id: 2610.31474
url: https://huggingface.co/papers/2610.31474
arxiv_url: https://arxiv.org/abs/2610.31474
date: 2026-10-23
---

# Skeleton-Grounded Latent Action Model for Robot World Models

Robot world models simulate how environments evolve in response to robot actions. Latent action models enable learning dynamics from videos by encoding visual transitions as proxy actions. However, reconstruction-driven latent actions mix robot motion with object responses and other scene changes, complicating their correspondence with robot controls. We propose SkeLAM, a skeleton-guided latent action model for controllable robot world modeling. SkeLAM decomposes latent actions into a kinematic component grounded by robot skeleton supervision and a residual component retaining complementary visual dynamics. Cross-modal swap reconstruction encourages RGB-derived and skeleton-derived kinematic representations to be interchangeable during video reconstruction. The world model incorporates both components through separate conditioning pathways, while branch dropout reduces its dependence on future-derived residual information. A lightweight adapter maps robot actions to the kinematic space, and subsequent world-model fine-tuning adapts generation to these predicted conditions. At inference, the model generates future observations from the current observation and robot actions. On DROID, SkeLAM reduces end-effector ADE by 19.5% and LPIPS by 11.1% compared with DreamDojo. Motion probing supports kinematic specialization, while qualitative results demonstrate zero-shot human-to-robot motion transfer in generated rollouts. Policy evaluation shows agreement between predicted success rates and those measured in real robot executions.
