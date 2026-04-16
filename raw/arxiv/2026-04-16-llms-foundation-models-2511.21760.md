---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2511.21760
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2511.21760
published: 2026-04-16
authors: Yuxiang Wei, Yanteng Zhang, Xi Xiao
---

# fMRI-LM: Towards a Universal Foundation Model for Language-Aligned fMRI Understanding

**arXiv:** https://arxiv.org/abs/2511.21760
**Authors:** Yuxiang Wei, Yanteng Zhang, Xi Xiao

## Abstract

arXiv:2511.21760v3 Announce Type: replace-cross  Abstract: Recent advances in multimodal large language models (LLMs) have enabled unified reasoning across images, audio, and video, but extending such capability to brain imaging remains largely unexplored. Bridging this gap is essential to link neural activity with semantic cognition and to develop cross-modal brain representations. To this end, we present fMRI-LM, a foundational model that bridges functional MRI (fMRI) and language through a three-stage framework. In Stage 1, we learn a neural tokenizer that maps fMRI into discrete tokens embedded in a language-consistent space. In Stage 2, a pretrained LLM is adapted to jointly model fMRI tokens and text, treating brain activity as a sequence that can be temporally predicted and linguistically described. To overcome the lack of natural fMRI-text pairs, we construct a large descriptive corpus that translates diverse imaging-based features into structured textual descriptors, capturing the low-level organization of fMRI signals. In Stage 3, we perform multi-task, multi-paradigm instruction tuning to endow fMRI-LM with high-level semantic understanding, supporting diverse downstream applications. Across various benchmarks, fMRI-LM achieves strong zero-shot and few-shot performance, and adapts efficiently with parameter-efficient tuning (LoRA), establishing a scalable pathway toward a language-aligned, universal model for structural and semantic understanding of fMRI.
