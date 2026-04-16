---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2602.01738
category: cs.CV
concept: llms-foundation-models
url: https://arxiv.org/abs/2602.01738
published: 2026-04-16
authors: Yue Zhou, Xinan He, Kaiqing Lin
---

# Simplicity Prevails: The Emergence of Generalizable AIGI Detection in Visual Foundation Models

**arXiv:** https://arxiv.org/abs/2602.01738
**Authors:** Yue Zhou, Xinan He, Kaiqing Lin

## Abstract

arXiv:2602.01738v2 Announce Type: replace  Abstract: While specialized detectors for AI-Generated Images (AIGI) achieve near-perfect accuracy on curated benchmarks, they suffer from a dramatic performance collapse in realistic, in-the-wild scenarios. In this work, we demonstrate that simplicity prevails over complex architectural designs. A simple linear classifier trained on the frozen features of modern Vision Foundation Models , including Perception Encoder, MetaCLIP 2, and DINOv3, establishes a new state-of-the-art. Through a comprehensive evaluation spanning traditional benchmarks, unseen generators, and challenging in-the-wild distributions, we show that this baseline not only matches specialized detectors on standard benchmarks but also decisively outperforms them on in-the-wild datasets, boosting accuracy by striking margins of over 30\%. We posit that this superior capability is an emergent property driven by the massive scale of pre-training data containing synthetic content. We trace the source of this capability to two distinct manifestations of data exposure: Vision-Language Models internalize an explicit semantic concept of forgery, while Self-Supervised Learning models implicitly acquire discriminative forensic features from the pretraining data. However, we also reveal persistent limitations: these models suffer from performance degradation under recapture and transmission, remain blind to VAE reconstruction and localized editing. We conclude by advocating for a paradigm shift in AI forensics, moving from overfitting on static benchmarks to harnessing the evolving world knowledge of foundation models for real-world reliability.
