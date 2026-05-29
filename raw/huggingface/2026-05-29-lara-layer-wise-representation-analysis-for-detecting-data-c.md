---
source: farmer/huggingface
farmed: 2026-05-29T09:54:41Z
arxiv_id: 2605.29888
url: https://huggingface.co/papers/2605.29888
arxiv_url: https://arxiv.org/abs/2605.29888
date: 2026-05-29
---

# LaRA: Layer-wise Representation Analysis for Detecting Data Contamination in RL Post-Training

Reinforcement learning (RL) post-training has shown to improve reasoning in large language models (LLMs). However, there has been little exploration on the problem of data contamination in RL post-training, potentially undermining generalization and evaluation reliability of the training process itself. Existing detection methods primarily rely on output-level signals such as likelihood or entropy, which become unreliable for RL-trained models since RL shapes behavior through trajectory-level rewards rather than token likelihoods. We propose LaRA, a layer-wise representation analysis framework for detecting contamination in RL post-trained LLMs. LaRA introduces three complementary metrics, measuring perturbation sensitivity, directional collapse, and local representation rigidity under controlled perturbations. We find that contamination produces progressive geometric deviations across layers, including amplified perturbation sensitivity, stronger directional collapse, and enhanced local rigidity. Based on our findings, we also develop a contamination detection protocol that aggregates representation-level deviations across layers and metrics. Experiments on RL-trained reasoning models show that our protocol outperforms existing output-level baselines for contamination detection.
