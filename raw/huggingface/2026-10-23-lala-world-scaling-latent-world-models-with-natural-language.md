---
source: farmer/huggingface
farmed: 2026-10-24T12:49:20.879766+00:00
arxiv_id: 2610.27851
url: https://huggingface.co/papers/2610.27851
arxiv_url: https://arxiv.org/abs/2610.27851
date: 2026-10-23
---

# LaLa-World: Scaling Latent World Models with Natural Language Actions

This paper shows that JEPA-style latent world models (LWMs) can learn across diverse domains and data sources by adopting the language-conditioned interface of video generation models. We establish this approach as an effective and efficient basis for planning with imagination and downstream policy fine-tuning. To this end, we introduce LaLa-World, a Language-conditioned Latent World model that learns from simulation and robot trajectories together with broader image and video data. Two designs make this work. First, we describe both numerical actions and visual changes in language, enabling joint training of a single future predictor across heterogeneous datasets. Second, we build the predictor on a language model, allowing it to interpret language conditions while predicting future latent states. The resulting predictor achieves higher average MPC planning performance than existing LWMs trained separately for each domain or task. Adding image and video data further improves average planning performance and robustness to action phrasing. In a matched comparison with an RAEv2-based video generation model baseline, LaLa-World reaches comparable planning performance with 6times less training cost and 13.9times faster planning. Beyond planning, the pretrained LaLa-World serves as an initialization for LaLa-Policy, which jointly predicts actions and future visual representations. LaLa-Policy performs competitively with Cosmos Policy on LIBERO and RoboCasa, with up to 5.5times faster inference.
