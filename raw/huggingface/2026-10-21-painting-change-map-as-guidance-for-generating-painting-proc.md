---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.642264
arxiv_id: 2610.25369
url: https://huggingface.co/papers/2610.25369
arxiv_url: https://arxiv.org/abs/2610.25369
date: 2026-10-21
---

# Painting Change Map as guidance for generating painting processes

Digital art generation has undergone a massive paradigm shift, moving from static image synthesis to dynamic video generation that can mimic the human painting process. While existing models can synthesize visually stunning time-lapses of paintings being created or "unpainted," they largely treat the creative process as a black box. Current conditioning mechanisms are either too rigid, relying on static geometric cues like Canny edges or depth maps, or too holistic, utilizing simple scalar progress variables that offer no localized control. Consequently, users lack the agency to steer how a painting evolves over time. In this work, we argue that true control over the video generation of artwork requires a joint understanding of two fundamental dimensions: where an artist acts, and when those actions take place. To achieve this, we introduce the Painting Change Map, a novel spatio-temporal control mechanism that explicitly tracks normalized structural changes across a 1,000-timestep continuum, a resolution sufficient to capture fine-grained stroke-level changes while remaining computationally tractable. By mapping localized visual differences into an encoded RGB space, our representation enables fine-grained guidance for both the forward painting and reverse unpainting processes. Extensive benchmarking demonstrates the efficacy of our approach. We outperform existing control baselines and achieve competitive or superior results compared to state-of-the-art painting methods. Furthermore, under oracle conditions, our method surpasses all baselines by a significant margin. Code is available at https://github.com/Markus-Pobitzer/painting-change-map.
