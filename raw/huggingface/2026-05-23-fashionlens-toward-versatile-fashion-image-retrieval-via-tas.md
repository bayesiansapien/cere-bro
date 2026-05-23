---
source: farmer/huggingface
farmed: 2026-05-23T00:00:00Z
arxiv_id: 2605.22552
url: https://huggingface.co/papers/2605.22552
arxiv_url: https://arxiv.org/abs/2605.22552
date: 2026-05-23
---

# FashionLens: Toward Versatile Fashion Image Retrieval via Task-Adaptive Learning

Fashion image retrieval is a cornerstone of modern e-commerce systems. A unified framework that supports diverse query formats and search intentions is highly desired in practice. However, existing approaches focus on narrow retrieval tasks and do not fully capture such diversity. Therefore, in this work, we aim to develop a unified framework capable of handling diverse realistic fashion retrieval scenarios, achieving truly versatile fashion image retrieval. To establish a data foundation, we first introduce U-FIRE, a comprehensive benchmark that consolidates fragmented fashion datasets into a unified collection, supplemented by two manually curated datasets for testing generalization. Building upon this, we propose FashionLens, a unified framework based on Multimodal Large Language Models. To handle divergent matching objectives, we design a Proposal-Guided Spherical Query Calibrator that dynamically shifts query representations into task-aligned metric spaces via adaptive spherical linear interpolation. Additionally, to mitigate the optimization imbalance caused by varying task complexities and data scales, we develop a Gradient-Guided Adaptive Sampling strategy that automatically re-weights tasks based on realtime learning difficulty and the data scale prior. Experiments on U-FIRE show that FashionLens achieves state-of-the-art performance across diverse retrieval scenarios and generalizes robustly to unseen tasks. The data and code are publicly released at https://github.com/haokunwen/FashionLens.
