---
source: farmer/huggingface
farmed: 2026-09-02T13:31:46.243214
arxiv_id: 2609.00968
url: https://huggingface.co/papers/2609.00968
arxiv_url: https://arxiv.org/abs/2609.00968
date: 2026-09-02
---

# ReFlowSET: Representation-Aligned Latent Flow Matching for SAR-to-EO Image Translation

SAR-to-EO image translation aims to generate electro-optical (EO) imagery from synthetic aperture radar (SAR) observations. Existing latent diffusion approaches typically inherit a predetermined autoencoder, although reconstruction fidelity can vary substantially across codecs and modalities. Because the latent codec affects the round-trip preservation of both SAR conditions and EO targets, codec selection constitutes a fundamental design choice; nevertheless, existing methods largely rely on codecs pretrained on natural images. To remedy this, we introduce ReFlowSET, a conditional latent flow-matching framework that selects its codec through a joint SAR--EO reconstruction audit. Rather than inheriting a heavyweight pretrained generator, ReFlowSET trains a substantially smaller conditional DiT from scratch in the selected latent space, using dual-stream SAR conditioning followed by joint feature refinement. To provide semantic guidance for this from-scratch training, intermediate noisy-EO features are aligned with clean target-EO representations extracted by a frozen vision foundation model. This alignment is used only during training and introduces no additional inference cost. Experiments on QXS-SAROPT and SAR2Opt demonstrate state-of-the-art performance across diverse perceptual fidelity and distributional metrics. Code and pretrained weights are publicly available at https://github.com/KAIST-VICLab/ReFlowSET.
