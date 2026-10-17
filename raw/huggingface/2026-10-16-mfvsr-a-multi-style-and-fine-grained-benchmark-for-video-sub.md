---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.18461
url: https://huggingface.co/papers/2610.18461
arxiv_url: https://arxiv.org/abs/2610.18461
date: 2026-10-16
---

# MFVSR: A Multi-Style and Fine-Grained Benchmark for Video Subtitle Removal

Video subtitle removal (VSR) is an important video restoration task, yet existing evaluation remains limited by low-resolution datasets, fragmented test sets, and generic video-inpainting protocols that fail to adequately capture localized restoration errors, unintended modifications, temporal instability, and incomplete outputs. In this paper, we introduce MFVSR, a large-scale multi-style benchmark for fine-grained and reliability-aware video subtitle removal evaluation. MFVSR distinguishes itself through three key features: (1) Large-scale and diverse data, comprising 3,000 paired videos from Real-HQ, Real-LQ, and AI-Generated sources, with an auxiliary set of 953 in-the-wild real videos for real-world coverage analysis; (2) Controlled subtitle diversity, spanning 16 languages and four factors covering spatial layout, temporal behavior, visual style, and language mode; (3) Fine-grained evaluation, introducing an information-conditioned, spatially decoupled protocol that separates blind from mask-guided removal and measures Restoration Fidelity, Preservation Fidelity, Temporal Fidelity, coverage, and failures. Experiments on six representative methods reveal substantial discrepancies between local restoration, outside-region preservation, temporal consistency, and full-set reliability that are obscured by conventional full-frame metrics. MFVSR therefore provides a more comprehensive and diagnostic foundation for evaluating and advancing video subtitle removal methods.
