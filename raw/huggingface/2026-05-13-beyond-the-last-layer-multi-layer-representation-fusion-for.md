---
source: farmer/huggingface
farmed: 2026-05-14T10:39:11Z
arxiv_id: 2605.10780
url: https://huggingface.co/papers/2605.10780
arxiv_url: https://arxiv.org/abs/2605.10780
date: 2026-05-13
---

# Beyond the Last Layer: Multi-Layer Representation Fusion for Visual Tokenization

Representation autoencoders that reuse frozen pretrained vision encoders as visual tokenizers have achieved strong reconstruction and generation quality. However, existing methods universally extract features from only the last encoder layer, discarding the rich hierarchical information distributed across intermediate layers. We show that low-level visual details survive in the last layer merely as attenuated residuals after multiple layers of semantic abstraction, and that explicitly fusing multi-layer features can substantially recover this lost information. We propose DRoRAE (Depth-Routed Representation AutoEncoder), a lightweight fusion module that adaptively aggregates all encoder layers via energy-constrained routing and incremental correction, producing an enriched latent compatible with a frozen pretrained decoder. A three-phase decoupled training strategy first learns the fusion under the implicit distributional constraint of the frozen decoder, then fine-tunes the decoder to fully exploit the enriched representation. On ImageNet-256, DRoRAE reduces rFID from 0.57 to 0.29 and improves generation FID from 1.74 to 1.65 (with AutoGuidance), with gains also transferring to text-to-image synthesis. Furthermore, we uncover a log-linear scaling law (R^2{=}0.86) between fusion capacity and reconstruction quality, identifying representation richness as a new, predictably scalable dimension for visual tokenizers analogous to vocabulary size in NLP.
