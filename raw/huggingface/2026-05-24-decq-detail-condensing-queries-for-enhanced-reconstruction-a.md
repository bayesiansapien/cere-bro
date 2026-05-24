---
source: farmer/huggingface
farmed: 2026-05-24T05:07:38.368292+00:00
arxiv_id: 2605.22777
url: https://huggingface.co/papers/2605.22777
arxiv_url: https://arxiv.org/abs/2605.22777
date: 2026-05-24
---

# DecQ: Detail-Condensing Queries for Enhanced Reconstruction and Generation in Representation Autoencoders

Representation Autoencoders (RAEs) leverage frozen vision foundation models (VFMs) as tokenizer encoders, providing robust high-level representations that facilitate fast convergence and high-quality generation in latent diffusion models. However, freezing the VFM inherently constrains its spatial reconstruction capacity, limiting fine-grained generation and image editing; in contrast, incorporating reconstruction-oriented signals via fine-tuning disrupts the pretrained semantic space and degrades generative fidelity. To address this trade-off, we propose DecQ, a simple yet effective framework for RAEs. Specifically, DecQ introduces lightweight detail-condensing queries that extract fine-grained information from intermediate VFM features through condenser modules. These queries are incorporated into the decoder to support reconstruction and are jointly generated with patch tokens during generative modeling. By aggregating information from both shallow and deep layers, DecQ effectively mitigates the reconstruction--generation trade-off, improving both reconstruction quality and generative performance. Our experiments demonstrate that: (1) with only 8 additional queries and 3.9% extra computation, DecQ improves reconstruction over the frozen DINOv2-based RAE, increasing PSNR from 19.13 dB to 22.76 dB; and (2) for generative modeling, DecQ achieves 3.3times faster convergence than RAE, attaining an FID of 1.41 without guidance and 1.05 with guidance.
