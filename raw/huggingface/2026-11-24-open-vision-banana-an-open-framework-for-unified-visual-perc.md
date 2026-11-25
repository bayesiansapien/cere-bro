---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.921920+00:00
arxiv_id: 2611.28489
url: https://huggingface.co/papers/2611.28489
arxiv_url: https://arxiv.org/abs/2611.28489
date: 2026-11-24
---

# Open Vision Banana: An Open Framework for Unified Visual Perception through Generation in RGB Space

Vision Banana showed that a closed image generator, instruction-tuned to paint perception outputs as RGB images, becomes a generalist vision model. Does this carry over to open generators, and if not, what fails? We answer with Open Vision Banana (OVB), an open framework that adapts the 7B diffusion generator of Qwen-Image-2.1 into one instruction-driven model for metric depth, semantic, instance, and referring segmentation, using a single shared low-rank adapter and public data. Each task is a task contract whose RGB encoder, instruction, and decoder share one specification and are checked before training. Studying 42 externally evaluated checkpoints from two 100k-update runs, six exact weight-space merges, and eight controlled shorter runs, we find that the gap to the closed system is specific and measurable. Geometry is learned early while absolute scale is not: median-aligned NYUv2 δ_1 stays at 0.89--0.93 throughout training as unaligned δ_1 wanders between 0.11 and 0.50. The scale is not committed by a single sample: a ten-seed ensemble lifts unaligned δ_1 from 0.348 to 0.516 without retraining. Depth and 2D segmentation compete for the shared adapter, and weight merging moves along this trade-off without escaping it. Finally, lower validation flow loss comes with lower Cityscapes accuracy (Spearman ρapprox-0.9 between loss reduction and mIoU), so the loss cannot select checkpoints. We release code, contracts, training data, and all evaluation outputs.
