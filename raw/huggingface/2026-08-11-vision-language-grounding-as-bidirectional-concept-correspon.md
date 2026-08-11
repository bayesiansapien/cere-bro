---
source: farmer/huggingface
farmed: 2026-08-11T13:25:26.002773
arxiv_id: 2608.07886
url: https://huggingface.co/papers/2608.07886
arxiv_url: https://arxiv.org/abs/2608.07886
date: 2026-08-11
---

# Vision-Language Grounding as Bidirectional Concept Correspondence

Vision-language grounding connects language to visual content, yet most existing formulations reduce grounding to a unidirectional localization problem: given a prespecified text phrase or category name, identify the corresponding image region. This setup assumes that the relevant linguistic unit is already known, overlooking a more basic challenge in grounded communication: determining which parts of the text are visually referential and how they correspond to entities in the image. We formulate grounding as bidirectional concept correspondence over an image-text pair. Given an image and its paired text, the goal is to recover all correspondences between visually referential text spans and instance-level image segments, without assuming that the relevant text spans are provided. This formulation unifies common grounding tasks, including phrase grounding, referring expression grounding, and open-vocabulary detection, by treating text segmentation, image segmentation, and cross-modal alignment as a single correspondence prediction problem. To address this task, we introduce ConCor-1, a grounding model built on top of a pretrained vision-language model. It uses learnable bridge tokens to represent candidate image-text correspondences and predicts, for each token, a text mask, an image mask, and a correspondence presence score. To train and evaluate this task, we convert diverse grounding and segmentation datasets into a unified correspondence format. Experiments show that ConCor-1 consistently outperforms baselines, improving correspondence F1 by 48% on the long-caption dataset and by 29% on zero-shot LVIS, where the large category list serves as the text input.
