---
source: farmer/huggingface
farmed: 2026-11-18T05:07:04.109596+00:00
arxiv_id: 2611.20254
url: https://huggingface.co/papers/2611.20254
arxiv_url: https://arxiv.org/abs/2611.20254
date: 2026-11-17
---

# VoxMel TTS Technical Report

Continuous autoregressive TTS relies on an acoustic target that enables stable next-latent modeling while preserving fine-grained acoustic details. While existing approaches employ learned compressed representations (e.g., continuous VAE latents) to render prediction tractable, they rely on complex neural encoders that often cap generation fidelity. Conversely, training-free targets like mel-spectrograms eliminate encoder overhead, yet their potential for autoregressive generation remains largely underexplored. In this work, we propose VoxMel, a tokenizer-free framework for autoregressive TTS that makes stable mel modeling tractable through a fixed, exactly invertible two-axis Haar transform. The transform first decomposes each mel spectrogram along frequency into local averages and a frequency residual, then splits the averaged component along time into Coarse-Mel and a temporal residual. A language-model backbone with a flow-matching head autoregressively generates Coarse-Mel. Non-autoregressive residual tiers then predict the temporal residual from Coarse-Mel, followed by the frequency residual conditioned on the reconstructed Frequency-Averaged Mel. Neither residual is fed back into the autoregressive history. Trained on 100K hours of Emilia, the supervised 0.6B model obtains 1.51\% WER and 0.738 speaker similarity (SIM) on test-en, and 1.29\% CER and 0.755 SIM on test-zh. GRPO improves these results to 1.15\% WER / 0.753 SIM and 1.17\% CER / 0.776 SIM, respectively. We also distill the guided flow head into two- and four-step students, requiring 2 or 4 head evaluations per coarse frame. The four-step student retains competitive SIM and nearly matches the supervised model in WER/CER.
