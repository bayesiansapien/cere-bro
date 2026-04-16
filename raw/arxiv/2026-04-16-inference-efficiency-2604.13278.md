---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13278
category: cs.LG
concept: inference-efficiency
url: https://arxiv.org/abs/2604.13278
published: 2026-04-16
authors: Yann V. Bellec
---

# DroneScan-YOLO: Redundancy-Aware Lightweight Detection for Tiny Objects in UAV Imagery

**arXiv:** https://arxiv.org/abs/2604.13278
**Authors:** Yann V. Bellec

## Abstract

arXiv:2604.13278v1 Announce Type: cross  Abstract: Aerial object detection in UAV imagery presents unique challenges due to the high prevalence of tiny objects, adverse environmental conditions, and strict computational constraints. Standard YOLO-based detectors fail to address these jointly: their minimum detection stride of 8 pixels renders sub-32px objects nearly undetectable, their CIoU loss produces zero gradients for non-overlapping tiny boxes, and their architectures contain significant filter redundancy. We propose DroneScan-YOLO, a holistic system contribution that addresses these limitations through four coordinated design choices: (1) increased input resolution of 1280x1280 to maximize spatial detail for tiny objects, (2) RPA-Block, a dynamic filter pruning mechanism based on lazy cosine-similarity updates with a 10-epoch warm-up period, (3) MSFD, a lightweight P2 detection branch at stride 4 adding only 114,592 parameters (+1.1%), and (4) SAL-NWD, a hybrid loss combining Normalized Wasserstein Distance with size-adaptive CIoU weighting, integrated into YOLOv8's TaskAligned assignment pipeline. Evaluated on VisDrone2019-DET, DroneScan-YOLO achieves 55.3% mAP@50 and 35.6% mAP@50-95, outperforming the YOLOv8s baseline by +16.6 and +12.3 points respectively, improving recall from 0.374 to 0.518, and maintaining 96.7 FPS inference speed with only +4.1% parameters. Gains are most pronounced on tiny object classes: bicycle AP@50 improves from 0.114 to 0.328 (+187%), and awning-tricycle from 0.156 to 0.237 (+52%).
