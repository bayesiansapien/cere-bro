---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2603.19790
category: cs.CV
concept: llms-foundation-models
url: https://arxiv.org/abs/2603.19790
published: 2026-04-16
authors: Weile Gong, Yiping Zuo, Zijian Lu
---

# From Plausibility to Verifiability: Risk-Controlled Generative OCR with Vision-Language Models

**arXiv:** https://arxiv.org/abs/2603.19790
**Authors:** Weile Gong, Yiping Zuo, Zijian Lu

## Abstract

arXiv:2603.19790v3 Announce Type: replace  Abstract: Modern vision-language models (VLMs) can act as generative OCR engines, yet open-ended decoding can expose rare but consequential failures. We identify a core deployment misalignment in generative OCR. Autoregressive decoding favors semantic plausibility, whereas OCR requires outputs that are visually grounded and geometrically verifiable. This mismatch produces severe errors, especially over-generation and unsupported substitutions, creating deployment risk even when benchmark accuracy remains high. We therefore formulate frozen VLM OCR as a selective accept/abstain problem and propose a model-agnostic Geometric Risk Controller. The controller probes multiple structured views of the same input, applies lightweight structural screening, and accepts a transcription only when cross-view consensus and stability satisfy predefined criteria, yielding a small family of operating points. Experiments on frozen VLM backbones and standard OCR benchmarks show consistent reductions in extreme-error risk and catastrophic over-generation at predictable coverage costs. Reliable deployment of generative OCR with frozen VLMs benefits from explicit system-level risk control rather than unconstrained generation.
