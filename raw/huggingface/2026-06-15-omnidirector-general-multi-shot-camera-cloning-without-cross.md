---
source: farmer/huggingface
farmed: 2026-06-15T06:21:28Z
arxiv_id: 2606.13432
url: https://huggingface.co/papers/2606.13432
arxiv_url: https://arxiv.org/abs/2606.13432
date: 2026-06-15
---

# OmniDirector: General Multi-Shot Camera Cloning without Cross-Paired Data

Cloning camera motion from reference videos is an important task in video generation, as videos provide intuitive and precise control. Existing methods either directly use parametric representations that fail to handle multi-shot generation or synthesize cross-paired data, which suffer from data scarcity, resulting in poor performance in complicated camera motion cloning. To address these issues, we introduce a general camera motion representation that encodes cameras as grid motion videos. This camera grid represents the camera parameters visually and supports the integration of diverse trajectories for multi-shot video generation. Building upon this, we propose OmniDirector, a unified framework trained on a million-scale camera grid-video pairs that coordinates characters, actions, and cameras to provide director-level control for multimodal diffusion transformers. Furthermore, we design a novel hierarchical prompt expansion agent that harmoniously integrates different control signals by systematically describing camera motion and visual content through understanding signal relationships. Extensive experiments demonstrate the superior performance and outstanding controllability of our framework. Project page: https://ymlinfeng.github.io/OmniDirector.github.io/
