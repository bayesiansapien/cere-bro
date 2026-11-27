---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.909846+00:00
arxiv_id: 2611.32473
url: https://huggingface.co/papers/2611.32473
arxiv_url: https://arxiv.org/abs/2611.32473
date: 2026-11-26
---

# OmniPersist: Persistent Dynamic World Modeling via Coupled Panoramic Evolution

Action-conditioned world models play a vital role in robotics and autonomous driving, yet existing video diffusion models struggle to maintain dynamic object persistence. When the camera turns away and returns, out-of-view moving entities fail to evolve plausibly in latent space, often mutating or vanishing entirely due to bounded perspective views. To resolve this issue, we propose OmniPersist, a unified framework that couples perspective video generation with panoramic evolution within a single-stage diffusion model, without relying on auxiliary models or initial panoramic inputs. To maintain efficiency, we model the panoramic stream at a lower frame rate, bridging both views across space and time via Geometric Anchoring (GeoAnch) for spatial correspondence and Temporal Compensation (TemComp) for temporal aggregation. OmniPersist is agnostic to camera-control architectures, supporting both latent-level and attention-level conditioning. Extensive experiments on a newly constructed dynamic benchmark across image-to-video and video continuation tasks demonstrate consistent gains in visual quality, camera controllability, revisit consistency, and dynamic persistence.
