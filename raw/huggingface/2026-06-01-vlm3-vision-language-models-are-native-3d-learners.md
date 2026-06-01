---
source: farmer/huggingface
farmed: 2026-06-01T09:02:45Z
arxiv_id: 2605.30561
url: https://huggingface.co/papers/2605.30561
arxiv_url: https://arxiv.org/abs/2605.30561
date: 2026-06-01
---

# VLM3: Vision Language Models Are Native 3D Learners

Vision Language Models (VLMs) enable a unified model to solve various vision tasks through prompting. They have shown promising performance in semantic understanding. However, 3D understanding still largely relies on expert vision models with complex task-specific designs. The key argument this work wants to make is that VLMs are native 3D learners. Our in-depth large scale study shows that 1) focal length unification, 2) text-based pixel reference and 3) data mixture and scaling, are all you need for effective 3D learning. Model architecture changes, large models, heavy data augmentations, and complex losses including the regression formulation, many of which form the foundation of expert vision models, are actually not necessary conditions. As a result, we propose VLM3, a scalable method with the simplest design that enables standard VLMs to master diverse 3D tasks. VLM3 not only advances the VLM depth estimation accuracy by a large margin (0.84 -> 0.9), but also enables diverse 3D tasks such as pixel correspondence, camera pose estimation and object-level 3D understanding, matching expert vision model accuracy while maintaining standard architectures and text-based training.
