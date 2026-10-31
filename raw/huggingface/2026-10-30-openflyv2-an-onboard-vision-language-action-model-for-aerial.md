---
source: farmer/huggingface
farmed: 2026-10-31T08:06:35.161040+00:00
arxiv_id: 2610.39287
url: https://huggingface.co/papers/2610.39287
arxiv_url: https://arxiv.org/abs/2610.39287
date: 2026-10-30
---

# OpenFlyV2: An onboard vision-language-action model for aerial perception and navigation

Human cognition flexibly draws on a shared perceptual foundation to understand environments, attend to referenced entities, reason about spatial relationships, and act. Endowing aerial robots with an analogous functional organization remains challenging, as existing systems are often specialized for individual capabilities, dependent on offboard computation, or unable to sustain closed-loop operation on resource-constrained platforms. We present OpenFlyV2, a unified onboard vision-language-action architecture that uses a shared vision-language representation to support semantic understanding, language-grounded perception, spatial reasoning, and continuous aerial control within a single model. A compact action expert converts the shared multimodal context into short-horizon flight waypoints, while motion-aware temporal memory and action priors reduce the computational cost of closed-loop execution. We construct , a simulation-based dataset comprising approximately 70,000 navigation trajectories and 60,000 vision-language instruction--response pairs. OpenFlyV2 generates action chunks, each comprising 12 waypoints, entirely onboard at 10 Hz using an NVIDIA Jetson Orin NX. It transfers zero-shot from simulation to physical quadrotor flight, achieving a 48\% navigation success rate across four real-world environments without real-world aerial training data. Extensive results demonstrate that broad vision-language competence and continuous closed-loop flight can coexist within a single model on a resource-constrained aerial platform. Code will be made publicly available at https://github.com/Ideal-ljl/AeroBrain.
