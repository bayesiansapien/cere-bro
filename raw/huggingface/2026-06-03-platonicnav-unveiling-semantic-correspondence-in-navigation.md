---
source: farmer/huggingface
farmed: 2026-06-03T06:14:02Z
arxiv_id: 2606.01788
url: https://huggingface.co/papers/2606.01788
arxiv_url: https://arxiv.org/abs/2606.01788
date: 2026-06-03
---

# PlatonicNav: Unveiling Semantic Correspondence in Navigation with Platonic Topological Maps

Embodied visual navigation, where an agent perceives a complex environment and acts to reach a goal from raw sensory input, underpins a wide range of applications such as household service robotics, assistive robotics, and large-scale autonomous exploration. However, recent attempts to unify vision-and-language navigation (VLN) and object goal navigation (ObjNav) remain at the level of architectural fusion, mixed-task training, and large vision-language pretraining, without examining whether independently trained vision and language encoders may already share a common semantic structure. Moreover, even object-centric topological maps still ground language goals through explicit cross-modal supervision such as CLIP or large vision-language models, leaving open whether such grounding is possible from a purely vision-built map. To address these challenges, we extend the Platonic Representation Hypothesis to embodied navigation and recast vision-only ObjNav, cross-modal ObjNav, and VLN as three different interfaces to the same object-centric semantic manifold. We further introduce PlatonicNav, a training-free framework whose Platonic Topological Map fuses geometric and semantic node distances from a self-supervised visual encoder, and grounds language goals via blind matching without any paired vision-language data. Extensive experiments on simulation benchmarks including HM3D-IIN, OVON, and R2R-CE on MP3D, together with deployment on Unitree Go2, demonstrate that PlatonicNav generalizes across tasks, modalities, and embodiments without explicit cross-modal training. Code: https://github.com/AIGeeksGroup/PlatonicNav. Website: https://aigeeksgroup.github.io/PlatonicNav.
