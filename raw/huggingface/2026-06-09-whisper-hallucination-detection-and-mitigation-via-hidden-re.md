---
source: farmer/huggingface
farmed: 2026-06-09T16:28:21
arxiv_id: 2606.07473
url: https://huggingface.co/papers/2606.07473
arxiv_url: https://arxiv.org/abs/2606.07473
date: 2026-06-09
---

# Whisper Hallucination Detection and Mitigation via Hidden Representation Steering and Sparse AutoEncoders

Whisper, a widely adopted ASR model, is known to suffer from hallucinations - coherent transcriptions generated for non-speech audio entirely disconnected from the input. We investigate whether hallucinations can be detected and mitigated through Whisper's internal representations. We extract audio encoder activations and evaluate two representation spaces: raw Whisper activations and Sparse AutoEncoder (SAE) latents. We show that both spaces encode linearly separable hallucination-related information, with discriminative power concentrated in a sparse feature subset and increasing toward deeper encoder layers. We propose two steering strategies: activation-space steering and SAE latent-space steering. SAE-based steering reduces hallucination rate from 72.63% to 14.11% for Whisper small and from 86.88% to 27.33% for Whisper large-v3 on the full non-speech test set, with small WER degradation on speech data, approaching the performance of fine-tuning-based methods.
