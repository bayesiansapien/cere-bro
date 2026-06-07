---
source: farmer/huggingface
farmed: 2026-06-07T04:51:04Z
arxiv_id: 2606.01753
url: https://huggingface.co/papers/2606.01753
arxiv_url: https://arxiv.org/abs/2606.01753
date: 2026-06-07
---

# Quality-Guided Semi-Supervised Learning for Medical Image Segmentation

Training accurate medical image segmentation models requires large amounts of densely annotated data, which is costly and time-consuming to obtain. Semi-supervised learning (SSL) alleviates this by learning from both abundant unlabeled data and limited labeled data. However, most modern SSL methods rely on pseudolabels for unlabeled data, and typically assess their reliability through model confidence or uncertainty, measures that are self-referential and lack explicit grounding in segmentation quality. Instead, we propose a quality-guided SSL framework that trains a dedicated network to estimate segmentation quality from image-mask pairs. The predictor is trained on variable-quality masks generated through synthetic corruptions augmented with imperfect outputs from partially trained segmentation models, capturing realistic error patterns encountered during training. We integrate the quality predictor into SSL through two complementary mechanisms: a quality-aware regularization loss and a quality-based pseudolabel sample reweighting scheme. We show that our method serves as a drop-in enhancement to existing SSL frameworks. Extensive experiments across five datasets and multiple architectures demonstrate consistent improvements over competing SSL methods, advancing the state-of-the-art in semi-supervised medical image segmentation.
