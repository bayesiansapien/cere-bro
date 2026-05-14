---
source: farmer/huggingface
farmed: 2026-05-14T10:39:11Z
arxiv_id: 2605.09936
url: https://huggingface.co/papers/2605.09936
arxiv_url: https://arxiv.org/abs/2605.09936
date: 2026-05-13
---

# Urban-ImageNet: A Large-Scale Multi-Modal Dataset and Evaluation Framework for Urban Space Perception

We present Urban-ImageNet, a large-scale multi-modal dataset and evaluation benchmark for urban space perception from user-generated social media imagery. The corpus contains over 2 Million public social media images and paired textual posts collected from Weibo across 61 urban sites in 24 Chinese cities across 2019-2025, with controlled benchmark subsets at 1K, 10K, and 100K scale and a full 2M corpus for large-scale training and evaluation. Urban-ImageNet is organized by HUSIC, a Hierarchical Urban Space Image Classification framework that defines a 10-class taxonomy grounded in urban theory. The taxonomy is designed to distinguish activated and non-activated public spaces, exterior and interior urban environments, accommodation spaces, consumption content, portraits, and non-spatial social-media content. Rather than treating urban imagery as generic scene data, Urban-ImageNet evaluates whether machine perception models can capture spatial, social, and functional distinctions that are central to urban studies. The benchmark supports three tasks within one standardized library: (T1) urban scene semantic classification, (T2) cross-modal image-text retrieval, and (T3) instance segmentation. Our experiments evaluate representative vision, vision-language, and segmentation models, revealing strong performance on supervised scene classification but more challenging behavior in cross-modal retrieval and instance-level urban object segmentation. A multi-scale study further examines how model performance changes as balanced training data increases from 1K, 10K to 100K images. Urban-ImageNet provides a unified, theory-grounded, multi-city benchmark for evaluating how AI systems perceive and interpret contemporary urban spaces across modalities, scales, and task formulations. Dataset and benchmark are available at: huggingface.co/datasets/Yiwei-Ou/Urban-ImageNet and github.com/yiasun/dataset-2.
