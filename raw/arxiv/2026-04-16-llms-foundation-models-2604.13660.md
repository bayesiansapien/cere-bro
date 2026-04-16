---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13660
category: cs.CV
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13660
published: 2026-04-16
authors: Hui Han, Shunli Wang, Yandan Zhao
---

# VRAG-DFD: Verifiable Retrieval-Augmentation for MLLM-based Deepfake Detection

**arXiv:** https://arxiv.org/abs/2604.13660
**Authors:** Hui Han, Shunli Wang, Yandan Zhao

## Abstract

arXiv:2604.13660v1 Announce Type: new  Abstract: In Deepfake Detection (DFD) tasks, researchers proposed two types of MLLM-based methods: complementary combination with small DFD detectors, or static forgery knowledge injection.The lack of professional forgery knowledge hinders the performance of these DFD-MLLMs.To solve this, we deeply considered two insightful issues: How to provide high-quality associated forgery knowledge for MLLMs? AND How to endow MLLMs with critical reasoning abilities given noisy reference information? Notably, we attempted to address above two questions with preliminary answers by leveraging the combination of Retrieval-Augmented Generation (RAG) and Reinforcement Learning (RL).Through RAG and RL techniques, we propose the VRAG-DFD framework with accurate dynamic forgery knowledge retrieval and powerful critical reasoning capabilities.Specifically, in terms of data, we constructed two datasets with RAG: Forensic Knowledge Database (FKD) for DFD knowledge annotation, and Forensic Chain-of-Thought Dataset (F-CoT), for critical CoT construction.In terms of model training, we adopt a three-stage training method (Alignment->SFT->GRPO) to gradually cultivate the critical reasoning ability of the MLLM.In terms of performance, VRAG-DFD achieved SOTA and competitive performance on DFD generalization testing.
