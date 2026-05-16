---
source: farmer/huggingface
farmed: 2026-05-16T03:36:10Z
arxiv_id: "2605.13852"
url: "https://huggingface.co/papers/2605.13852"
arxiv_url: "https://arxiv.org/abs/2605.13852"
date: 2026-05-16
---

# Realiz3D: 3D Generation Made Photorealistic via Domain-Aware Learning

We often aim to generate images that are both photorealistic and 3D-consistent, adhering to precise geometry, material, and viewpoint controls. Typically, this is achieved by fine-tuning an image generator, pre-trained on billions of real images, using renders of synthetic 3D assets, where annotations for control signals are available. While this approach can learn the desired controls, it often compromises the realism of the images due to domain gap between photographs and renders. We observe that this issue largely arises from the model learning an unintended association between the presence of control signals and the synthetic appearance of the images. To address this, we introduce Realiz3D, a lightweight framework for training diffusion models, that decouples controls and visual domain. The key idea is to explicitly learn visual domain, real or synthetic, separately from other control signals by introducing a co-variate that, fed into small residual adapters, shifts the domain. Then, the generator can be trained to gain controllability, without fitting to specific visual domain. In this way, the model can be guided to produce realistic images even when controls are applied. We enhance control transferability to the real domain by leveraging insights about roles of different layers and denoising steps in diffusion-based generators, informing new training and inference strategies that further mitigate the gap. We demonstrate the advantages of Realiz3D in tasks as text-to-multiview generation and texturing from 3D inputs, producing outputs that are 3D-consistent and photorealistic.
