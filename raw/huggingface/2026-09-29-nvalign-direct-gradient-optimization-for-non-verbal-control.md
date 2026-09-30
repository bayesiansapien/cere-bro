---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.934370+00:00
arxiv_id: 2609.31892
url: https://huggingface.co/papers/2609.31892
arxiv_url: https://arxiv.org/abs/2609.31892
date: 2026-09-29
---

# NVAlign: Direct-Gradient Optimization for Non-Verbal Control in Continuous Autoregressive Flow Matching Text-to-Speech

While modern text-to-speech (TTS) systems generate highly natural speech and support inline non-verbal vocalization (NVV) tags, accurate control over these events remains challenging. A key gap is the lack of established post-training methods for non-verbal control in continuous autoregressive flow-matching TTS. To this end, we present NVAlign, a direct-gradient post-training framework for NVV tag-following in this architecture. We first perform supervised fine-tuning (SFT) of TTS models and an NVV-aware automatic speech recognition (NV-ASR) model on NVV-annotated speech, then freeze the NV-ASR model to serve as the reward model for post-training. A two-step gradient surrogate enables efficient reward backpropagation through the flow-matching sampler to jointly update the autoregressive backbone and acoustic flow head. Fidelity penalties and reference-velocity regularization help preserve speaker similarity and speech quality. Results from NVV-SuperBench and human listening evaluations show that NVAlign improves tag-following accuracy over SFT and Flow-GRPO baselines. These findings demonstrate that direct reward-gradient optimization can improve non-verbal control in continuous autoregressive flow-matching TTS. Audio samples are available at https://nvalign.github.io/.
