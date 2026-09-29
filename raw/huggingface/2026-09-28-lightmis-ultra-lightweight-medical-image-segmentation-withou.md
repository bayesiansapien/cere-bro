---
source: farmer/huggingface
farmed: 2026-09-29T05:05:53.599067+00:00
arxiv_id: 2609.28327
url: https://huggingface.co/papers/2609.28327
arxiv_url: https://arxiv.org/abs/2609.28327
date: 2026-09-28
---

# LightMIS: Ultra-Lightweight Medical Image Segmentation Without a Stage-Wise Decoder

We present LightMIS, a scalable family of ultra-lightweight convolutional networks for 2D binary medical image segmentation without a learned stage-wise decoder. LightMIS aligns the outputs of a five-level encoder to a common resolution using Scale-Aligned Projection blocks, aggregates them once, and refines the fused representation with an Adaptive Fusion Cascade. The cascade combines Adaptive Kernel Fusion with the proposed Progressive Receptive Fusion module, which uses temporary channel expansion, complementary depthwise receptive fields, and progressive cross-branch information transfer. We evaluate LightMIS-T, LightMIS-S, and LightMIS using five-fold cross-validation under a common nnU-Net v2.3.1 protocol on DRIVE, Kvasir-SEG, DSB18, BUSI, ISIC-2017, and ISIC-2018. Full LightMIS contains 0.131 M parameters and requires 0.575 GFLOPs for a 3times256times256 input, achieving modality-macro Dice and IoU scores of 86.71% and 78.99%, respectively. Mobile U-ViT obtains 86.75% Dice and 79.07% IoU, so the observed differences are 0.04 and 0.08 percentage points. Relative to Mobile U-ViT, nnWNet, and nnU-Net, LightMIS reduces parameter count by 90.58-99.61% and GFLOPs by 82.54-96.14%. On an Arm Mali-G52 MC2 GPU, all LightMIS variants achieve full GPU delegation, with median delegated latency ranging from 53.31 ms for LightMIS-T to 138.31 ms for LightMIS. These results demonstrate a favorable accuracy-complexity trade-off and on-device execution feasibility for the evaluated tasks. The code is publicly available at https://github.com/AndreiiArhire/LightMIS.
