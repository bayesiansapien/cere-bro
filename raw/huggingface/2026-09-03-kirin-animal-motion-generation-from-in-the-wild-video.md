---
source: farmer/huggingface
farmed: 2026-09-03T17:01:45.591071
arxiv_id: 2609.01823
url: https://huggingface.co/papers/2609.01823
arxiv_url: https://arxiv.org/abs/2609.01823
date: 2026-09-03
---

# Kirin: Animal Motion Generation from In-the-Wild Video

Understanding animal motion is fundamental to modeling animal behavior and biomechanics, yet progress in this area lags far behind human motion research due to the scarcity of high-quality motion data. While human motion can be captured in controlled environments, it is impractical for most animal species, resulting in small, domain-limited datasets that restrict downstream applications such as animation. To address this challenge, we introduce Kirin, a framework that reconstructs motion from video, learns motion priors at scale, and generates realistic motion that can be directly applied to animated assets. Using large collections of in-the-wild animal videos, we reconstruct 3D motion sequences and pair them with captions to create AiM3D, the first large-scale dataset offering aligned video-text-motion tuples for quadruped animals. Building on this dataset, we develop a visual-guided motion generation model that conditions on both text and image to guide the generation of realistic motion across diverse animal species. Finally, by leveraging an off-the-shelf image-to-3D model, we automatically rig and animate 3D meshes using generated motion, producing ready-to-render animated animals. Together, our dataset and framework establish a new foundation for large-scale, text and image conditioned animal motion generation and animation. Project page: https://kirin-ani.github.io/.
