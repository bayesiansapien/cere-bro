---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13692
category: cs.CL
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13692
published: 2026-04-16
authors: Xiao Pu, Zepeng Cheng, Lin Yuan
---

# Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection

**arXiv:** https://arxiv.org/abs/2604.13692
**Authors:** Xiao Pu, Zepeng Cheng, Lin Yuan

## Abstract

arXiv:2604.13692v1 Announce Type: new  Abstract: As large language models (LLMs) generate text that increasingly resembles human writing, the subtle cues that distinguish AI-generated content from human-written content become increasingly challenging to capture. Reliance on generator-specific artifacts is inherently unstable, since new models emerge rapidly and reduce the robustness of such shortcuts. This generalizes unseen generators as a central and challenging problem for AI-text detection. To tackle this challenge, we propose a progressively structured framework that disentangles AI-detection semantics from generator-aware artifacts. This is achieved through a compact latent encoding that encourages semantic minimality, followed by perturbation-based regularization to reduce residual entanglement, and finally a discriminative adaptation stage that aligns representations with task objectives. Experiments on MAGE benchmark, covering 20 representative LLMs across 7 categories, demonstrate consistent improvements over state-of-the-art methods, achieving up to 24.2% accuracy gain and 26.2% F1 improvement. Notably, performance continues to improve as the diversity of training generators increases, confirming strong scalability and generalization in open-set scenarios. Our source code will be publicly available at https://github.com/PuXiao06/DRGD.
