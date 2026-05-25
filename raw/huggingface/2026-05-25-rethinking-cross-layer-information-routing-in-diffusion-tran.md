---
source: farmer/huggingface
farmed: 2026-05-25T08:23:16Z
arxiv_id: 2605.20708
url: https://huggingface.co/papers/2605.20708
arxiv_url: https://arxiv.org/abs/2605.20708
date: 2026-05-25
---

# Rethinking Cross-Layer Information Routing in Diffusion Transformers

Diffusion Transformers (DiTs) have become a de facto backbone of modern visual generation, and nearly every major axis of their design -- tokenization, attention, conditioning, objectives, and latent autoencoders -- has been extensively revisited. The residual stream that governs how information accumulates across layers, however, has been directly inherited from the original Transformer. In this paper, we present a systematic empirical analysis of cross-layer information flow in DiTs, jointly along depth and denoising timestep, and identify three concrete symptoms of traditional residual addition, namely monotonic forward magnitude inflation, sharp backward gradient decay, and pronounced block-wise redundancy. Motivated by this diagnosis, we propose Diffusion-Adaptive Routing (DAR), a drop-in residual replacement that performs learnable, timestep-adaptive, and non-incremental aggregation over the history of sublayer outputs. Moreover, the proposed DAR is compatible with many modern Transformer enhancement methods, such as REPA. On ImageNet 256times256, DAR improves SiT-XL/2 by 2.11 FID (7.56 vs.\ 9.67) and matches the baseline's converged quality with 8.75times fewer training iterations. Stacked on top of REPA, it yields a 2times training acceleration in the early stage, suggesting cross-layer information routing as an underexplored design axis in diffusion modeling, one that operates orthogonally to existing representation-alignment objectives. Beyond pretraining, DAR can also be applied during the fine-tuning stage of large-scale T2I models and preserves high-frequency details during Distribution Matching Distillation.
