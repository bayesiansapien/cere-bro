---
source: farmer/huggingface
farmed: 2026-10-29T10:37:09.995136+05:30
arxiv_id: 2610.36791
url: https://huggingface.co/papers/2610.36791
arxiv_url: https://arxiv.org/abs/2610.36791
date: 2026-10-28
---

# RynnWorld-Latent: A Cross-Embodiment World Model Conditioned on Universal Latent Actions

Learning controllable world dynamics from heterogeneous interaction videos is challenging because robot embodiments use incompatible action spaces, while human videos lack native control labels. We present RynnWorld-Latent, a cross-embodiment video world model that uses the 3D-grounded latent actions introduced by RynnLAM as a shared conditioning interface. This representation enables joint pretraining on human interaction videos, robot demonstrations, and simulation rollouts without requiring a common native action space. Built on a pretrained video transformer, RynnWorld-Latent combines global action tokens with an identity-initialized local pathway that aligns actions with future video latents. We pretrain on 23 datasets comprising approximately 553.5M frames and adapt the model to target robots through post-training. The framework supports two data-generation routes: digital teleoperation uses target robot commands to generate action-video demonstrations, while latent-action synthesis transfers source motion to an edited initial frame and pairs the resulting rollout with retargeted pseudo robot actions. Experiments show improved video prediction metrics on public benchmarks and two real-robot platforms, alongside qualitative action following when different action sequences share the same initial observation. Synthetic mid-training improves policy success rates on LIBERO and LIBERO-Plus, and both generation routes improve real-world policy success rates over real-demonstration-only training in the evaluated settings. These results support universal latent actions as a scalable interface for learning controllable visual dynamics across heterogeneous embodiments.
