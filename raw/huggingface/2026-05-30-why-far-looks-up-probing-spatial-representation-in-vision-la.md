---
source: farmer/huggingface
farmed: 2026-05-30T09:33:08Z
arxiv_id: 2605.30161
url: https://huggingface.co/papers/2605.30161
arxiv_url: https://arxiv.org/abs/2605.30161
date: 2026-05-30
---

# Why Far Looks Up: Probing Spatial Representation in Vision-Language Models

Vision-language models (VLMs) achieve strong performance on spatial reasoning benchmarks, yet it remains unclear whether this reflects structured 3D understanding or reliance on statistical shortcuts in natural images. We introduce a representation-level analysis framework that constructs minimal contrastive pairs to measure how spatial axes are organized and disentangled within VLM embeddings. Our analysis across multiple model families reveals a consistent vertical-distance entanglement: models conflate vertical image position with distance, mirroring the perspective bias of natural photographs. This bias produces a significant accuracy gap between perspective-consistent and counter-heuristic examples, and intensifies under data scaling even as overall benchmark accuracy improves. We further show that models with similar benchmark scores can exhibit different internal representations, and that these differences predict accuracy and robustness across diverse spatial reasoning benchmarks. To isolate this bias from evaluation-set skew, we introduce SpatialTunnel, a synthetic benchmark designed to expose spatial shortcut biases by removing common correlations present in natural images. Experiments confirm that the entanglement is model-intrinsic, and that models with well-separated spatial axes exhibit greater robustness, suggesting that well-structured spatial representations lead to more reliable spatial reasoning across diverse benchmarks. Code and benchmark are available on the project page: https://cheolhong0916.github.io/whyfarlooksup.github.io/.
