---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.14074
category: cs.CV
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.14074
published: 2026-04-16
authors: Laurence Bonat, Francesco Tonini, Elisa Ricci
---

# Training-Free Semantic Multi-Object Tracking with Vision-Language Models

**arXiv:** https://arxiv.org/abs/2604.14074
**Authors:** Laurence Bonat, Francesco Tonini, Elisa Ricci

## Abstract

arXiv:2604.14074v1 Announce Type: new  Abstract: Semantic Multi-Object Tracking (SMOT) extends multi-object tracking with semantic outputs such as video summaries, instance-level captions, and interaction labels, aiming to move from trajectories to human-interpretable descriptions of dynamic scenes. Existing SMOT systems are trained end-to-end, coupling progress to expensive supervision, limiting the ability to rapidly adapt to new foundation models and new interactions. We propose TF-SMOT, a training-free SMOT pipeline that composes pretrained components for detection, mask-based tracking, and video-language generation. TF-SMOT combines D-FINE and the promptable SAM2 segmentation tracker to produce temporally consistent tracklets, uses contour grounding to generate video summaries and instance captions with InternVideo2.5, and aligns extracted interaction predicates to BenSMOT WordNet synsets via gloss-based semantic retrieval with LLM disambiguation. On BenSMOT, TF-SMOT achieves state-of-the-art tracking performance within the SMOT setting and improves summary and caption quality compared to prior art. Interaction recognition, however, remains challenging under strict exact-match evaluation on the fine-grained and long-tailed WordNet label space; our analysis and ablations indicate that semantic overlap and label granularity substantially affect measured performance.
