---
source: farmer/huggingface
farmed: 2026-05-31T09:25:04Z
arxiv_id: 2605.30347
url: https://huggingface.co/papers/2605.30347
arxiv_url: https://arxiv.org/abs/2605.30347
date: 2026-05-31
---

# NeuROK: Generative 4D Neural Object Kinematics

Data-driven approaches have revolutionized 3D vision, enabling transformers to effectively reconstruct and generate static 3D objects. However, generating simulative 4D dynamics -- realistic temporal deformations of static objects under various physical conditions -- remains challenging and often ad hoc, despite its importance in building comprehensive 3D world models. Most existing methods assume a predefined physical model and use system identification to estimate parameters, restricting these methods to specific categories and small-scale datasets. We propose that these restrictions can be overcome by learning a data-driven kinematic state parameterization for object-centric physical systems. Specifically, we learn both a latent space representing all possible states of the object and a decoder that maps any sampled latent to a plausibly deformed shape of the object. We refer to this parameterization as Neural Object Kinematics (NeuROK), and learn a transformer-based encoder-decoder model on a curated large-scale 4D dataset. This formulation and the learned model significantly simplify the generation of simulative dynamics since we only need to consider the dynamics within a low-dimensional latent space from the Lagrangian mechanics' perspective in classical physics. We demonstrate the effectiveness and generality of this neural simulation framework across diverse dynamic object types, showing clear advantages over prior works. Project page: https://chen-geng.com/neurok
