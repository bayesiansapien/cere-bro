---
source: farmer/huggingface
farmed: 2026-06-16T00:00:00Z
arxiv_id: 2606.17049
url: https://huggingface.co/papers/2606.17049
arxiv_url: https://arxiv.org/abs/2606.17049
date: 2026-06-16
---

# BRDFusion: Physics Meets Generation for Urban Scene Inverse Rendering

Inverse rendering of urban scenes from captured videos enables numerous applications, including content creation and autonomous driving simulation. Physically-based rendering methods follow and control lighting physics, but suffer from reconstruction and rendering artifacts. While generative models produce realistic videos, they offer limited consistency and controllability. We present BRDFusion, a unified framework that combines two complementary models for inverse and forward rendering. Specifically, BRDFusion recovers explicit, consistent scene properties with physical modeling and alleviates optimization ambiguity with generative priors. During forward rendering, the physical model provides controllable rendering from the scene configuration, and the generative model denoises and fixes artifacts. Therefore, our method produces high-quality videos while allowing precise control, outperforming baselines in real and synthetic scenes. Moreover, BRDFusion supports novel-view relighting, night simulation, and dynamic object insertion/editing. Project page: https://shigon255.github.io/brdfusion-page/
