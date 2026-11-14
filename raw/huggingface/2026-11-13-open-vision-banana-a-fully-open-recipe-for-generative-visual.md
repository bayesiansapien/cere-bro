---
source: farmer/huggingface
farmed: 2026-11-14T05:10:36.527392+00:00
arxiv_id: 2611.15844
url: https://huggingface.co/papers/2611.15844
arxiv_url: https://arxiv.org/abs/2611.15844
date: 2026-11-13
---

# Open Vision Banana: A Fully Open Recipe for Generative Visual Perception

Recent work suggests that pretrained image generators encode real-world understanding beyond image synthesis. Vision Banana exploits this by framing vision tasks as conditional image editing. However, its data, weights, code, and implementation details are not public. We present Open Vision Banana (OVB), a fully open and reproducible recipe for converting pretrained generators into unified multi-task perception systems. Our analyses identify the design choices that matter most for generalization, including color encoding, prompt design, parameter adaptation, and task balancing. These choices interact, so individually helpful choices can hurt when combined with others. Starting from 4B and 9B parameter open-weight base models and using 2.1M-3.8M training pairs from public datasets, OVB surpasses Vision Banana's reported Cityscapes zero-shot performance (73.9 vs. 69.9 mIoU) and rivals state-of-the-art affine-invariant depth estimators. Its non-zero-shot variants come within five points of Vision Banana on referring and reasoning segmentation but remain further behind on instance segmentation. All models largely retain the base model's image-editing abilities. With legend ensembling, we introduce a test-time scaling method for generator-based perception. It segments an image under several class-color legends and fuses the results by majority vote, correcting unstable color-class bindings and improving mIoU by up to 8.7 points on Cityscapes and 15.0 points on COCO-Object without retraining. We release the dataset construction and processing pipeline, the training and evaluation code, as well as the final, intermediate, and ablation checkpoints. Project website: https://openvisionbanana.github.io
