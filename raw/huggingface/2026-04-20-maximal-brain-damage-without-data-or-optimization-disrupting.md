---
source: farmer/huggingface
farmed: 2026-04-20T00:00:00
arxiv_id: 2502.07408
url: https://huggingface.co/papers/2502.07408
arxiv_url: https://arxiv.org/abs/2502.07408
date: 2026-04-20
---

# Maximal Brain Damage Without Data or Optimization: Disrupting Neural Networks via Sign-Bit Flips

Deep Neural Networks (DNNs) can be catastrophically disrupted by flipping only a handful of parameter bits. We introduce Deep Neural Lesion (DNL), a data-free and optimization-free method that locates critical parameters, and an enhanced single-pass variant, 1P-DNL, that refines this selection with one forward and backward pass on random inputs. We show that this vulnerability spans multiple domains, including image classification, object detection and instance segmentation, and reasoning large language models. In image classification, flipping just two sign bits in ResNet-50 on ImageNet reduces accuracy by 99.8%. In object detection and instance segmentation, one or two sign flips in the backbone collapse COCO detection and mask AP for Mask R-CNN and YOLOv8-seg models. In language modeling, two sign flips into different experts reduce Qwen3-30B-A3B-Thinking from 78% to 0% accuracy. We also show that selectively protecting a small fraction of vulnerable sign bits provides a practical defense against such attacks.
