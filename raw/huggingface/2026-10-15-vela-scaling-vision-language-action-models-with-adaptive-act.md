---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.232717+05:30
arxiv_id: 2610.05230
url: https://huggingface.co/papers/2610.05230
arxiv_url: https://arxiv.org/abs/2610.05230
date: 2026-10-15
---

# Vela: Scaling Vision-Language-Action Models with Adaptive Action Curve Parametrization

Most vision-language-action models represent future motion as fixed-rate action chunks, tying temporal resolution and prediction horizon to a fixed output budget. This pointwise representation wastes capacity on highly correlated neighboring actions, leaves temporal continuity and smoothness to be learned implicitly, and forces a tradeoff between long-horizon coverage and the local precision required for contact-rich manipulation. To address these limitations, we introduce Vela, a vision-language-action foundation model that represents future robot behavior as continuous trajectories. Vela combines a compact spline-based action representation with motion-dependent temporal support and a shared action interface for heterogeneous embodiments, allowing a fixed output budget to adapt its temporal resolution across motions. We pretrain Vela on large-scale multi-embodiment robot data and evaluate it on LIBERO-X, EBench, and two real-world long-horizon tasks, egg-cake cooking and potato shredding, obtaining promising results across simulation and physical manipulation. These results highlight the potential of continuous action representations as a foundation for future embodied foundation models. Project page and more results: https://clementine24.github.io/Vela/ .
