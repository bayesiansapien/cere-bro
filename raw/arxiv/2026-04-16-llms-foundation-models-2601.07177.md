---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2601.07177
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2601.07177
published: 2026-04-16
authors: Mingxiang Tao, Yu Tian, Wenxuan Tu
---

# Safe-FedLLM: Delving into the Safety of Federated Large Language Models

**arXiv:** https://arxiv.org/abs/2601.07177
**Authors:** Mingxiang Tao, Yu Tian, Wenxuan Tu

## Abstract

arXiv:2601.07177v3 Announce Type: replace-cross  Abstract: Federated learning (FL) addresses privacy and data-silo issues in the training of large language models (LLMs). Most prior work focuses on improving the efficiency of federated learning for LLMs (FedLLM). However, security in open federated environments, particularly defenses against malicious clients, remains underexplored. To investigate the security of FedLLM, we conduct a preliminary study to analyze potential attack surfaces and defensive characteristics from the perspective of LoRA updates. We find two key properties of FedLLM: 1) LLMs are vulnerable to attacks from malicious clients in FL, and 2) LoRA updates exhibit distinct behavioral patterns that can be effectively distinguished by lightweight classifiers. Based on these properties, we propose Safe-FedLLM, a probe-based defense framework for FedLLM, which constructs defenses across three levels: Step-Level, Client-Level, and Shadow-Level. The core concept of Safe-FedLLM is to perform probe-based discrimination on each client's local LoRA updates, treating them as high-dimensional behavioral features and using a lightweight classifier to determine whether they are malicious. Extensive experiments demonstrate that Safe-FedLLM effectively improves FedLLM's robustness against malicious clients while maintaining competitive performance on benign data. Notably, our method effectively suppresses the impact of malicious data without significantly affecting training speed, and remains effective even under high malicious client ratios.
