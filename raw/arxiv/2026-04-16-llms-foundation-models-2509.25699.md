---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2509.25699
category: cs.CV
concept: llms-foundation-models
url: https://arxiv.org/abs/2509.25699
published: 2026-04-16
authors: Xiping Li, Jianghong Ma
---

# AIM-CoT: Active Information-driven Multimodal Chain-of-Thought for Vision-Language Reasoning

**arXiv:** https://arxiv.org/abs/2509.25699
**Authors:** Xiping Li, Jianghong Ma

## Abstract

arXiv:2509.25699v2 Announce Type: replace  Abstract: Interleaved-Modal Chain-of-Thought (I-MCoT) advances vision-language reasoning, such as Visual Question Answering (VQA). This paradigm integrates specially selected visual evidence from the input image into the context of Vision-Language Models (VLMs), enabling them to ground their reasoning logic in these details. Accordingly, the efficacy of an I-MCoT framework relies on identifying what to see (evidence selection) and when to see it (triggering of insertions). However, existing methods fall short in both aspects. First, for selection, they rely on attention signals, which are unreliable -- particularly under severe granularity imbalance between the brief textual query and the informative image. Second, for triggering, they adopt static triggers, which fail to capture the VLMs' dynamic needs for visual evidence. To this end, we propose a novel I-MCoT framework, Active Information-driven Multi-modal Chain-of-Thought (AIM-CoT), which aims to improve both evidence selection and insertion triggering via: (1) Context-enhanced Attention-map Generation (CAG) to mitigate granularity imbalance via textual context enhancement; (2) Active Visual Probing (AVP) to proactively select the most informative evidence via an information foraging process; and (3) Dynamic Attention-shift Trigger (DAT) to precisely activate insertions when VLM's attention shifts from text to visual context. Experiments across three benchmarks and four backbones demonstrate AIM-CoT's consistent superiority. Our code is available at https://anonymous.4open.science/r/AIMCoT.
