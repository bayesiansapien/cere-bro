---
source: farmer/huggingface
farmed: 2026-09-11T21:57:41.002444
arxiv_id: 2609.07064
url: https://huggingface.co/papers/2609.07064
arxiv_url: https://arxiv.org/abs/2609.07064
date: 2026-09-11
---

# SpatialBlock: Enhancing Spatial Intelligence in LVLMs via Synthetic Block-Stacking Problem

Large Vision-Language Models (LVLMs) have achieved strong performance on diverse visual tasks, yet their ability to reconstruct and reason about the 3D structure of the scene depicted in 2D images -- referred to as spatial intelligence -- remains limited. Existing approaches attempt to address this gap by using real-scene spatial question answering datasets that require dense geometric annotations. However, constructing such labels is costly, time-consuming, and often noisy due to reliance on external perception modules. In this work, we propose a novel paradigm inspired by human cognitive development: learning foundational spatial skills through structured block-manipulation tasks. We introduce SpatialBlock-15k, a synthetic dataset of 15,000 block-stacking problems covering 3D-to-2D projection, viewpoint transformation, and structural combination. The dataset further incorporates controlled color modulation as visual cues to encourage anchor-based reasoning in visually complex conditions. Experiments demonstrate that LVLMs trained on our dataset through either direct answering or reasoning-based prediction significantly outperform baselines and generalize to real-world spatial tasks, despite the dataset's synthetic and compact nature. Code and data are available at https://github.com/rsoohyun/SpatialBlock.
