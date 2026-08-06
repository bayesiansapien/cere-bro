---
source: farmer/huggingface
farmed: 2026-08-06T10:35:34.247620Z
arxiv_id: 2608.05042
url: https://huggingface.co/papers/2608.05042
arxiv_url: https://arxiv.org/abs/2608.05042
date: 2026-08-06
---

# BridgeVLA++: A Data-Efficient, Generalizable, and Memory-Augmented Vision-Language-Action Framework for 3D Manipulation

Leveraging pre-trained vision-language models (VLMs) to construct vision-language-action (VLA) models has emerged as a promising paradigm for 3D robot manipulation. However, existing 3D VLA methods remain data-hungry, exhibit limited generalization under distribution shifts, and lack explicit memory of past observations. These limitations hinder their application to data-scarce, open-world, and memory-dependent manipulation scenarios. Our previous work, BridgeVLA, improves data efficiency and generalization by preserving the input--output alignment of a pre-trained VLM during 3D action learning: raw point clouds are projected into multi-view images, and intermediate heatmaps are predicted before generating robot actions. In this work, we develop BridgeVLA++ by equipping BridgeVLA with a unified spatio-temporal memory architecture that models persistent spatial context and temporal interaction history. The resulting memory-augmented framework can reason over observation histories while preserving BridgeVLA's data efficiency and generalization capabilities. Extensive experiments show that our framework achieves strong performance on spatial manipulation tasks while exhibiting robust generalization. BridgeVLA++ further achieves state-of-the-art performance on two challenging memory-dependent manipulation benchmarks without sacrificing the data efficiency and generalization of the original BridgeVLA. In addition, BridgeVLA++ performs effectively in bimanual manipulation settings and is validated on an additional real-world robotic platform, demonstrating its scalability across tasks, environments, and robotic platforms. These results establish BridgeVLA++ as a unified 3D vision-language-action framework that simultaneously supports data-efficient learning, robust generalization, and effective memory-aware robot manipulation. Project website: https://bridgevla-plus.github.io/.
