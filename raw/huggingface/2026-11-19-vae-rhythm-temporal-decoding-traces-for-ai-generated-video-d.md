---
source: farmer/huggingface
farmed: 2026-11-20T05:04:58.145273+00:00
arxiv_id: 2611.21114
url: https://huggingface.co/papers/2611.21114
arxiv_url: https://arxiv.org/abs/2611.21114
date: 2026-11-19
---

# VAE Rhythm: Temporal Decoding Traces for AI-Generated Video Detection

Visible artifacts are an unreliable cue for detecting generated videos, because newer generators learn to remove them. We instead detect a trace left by the generation pipeline itself. Most video generators decode latents with a 3D causal VAE that groups consecutive frames in time, so the fidelity of generated frames rises and falls periodically with their position in a group. We call this periodic trace VAE Rhythm. Real videos are captured frame by frame and do not have it. To reveal it without training, we propose a phase scan. The scan reconstructs a clip with an off-the-shelf VAE from successive start offsets and measures the periodicity of the reconstruction error across these offsets. We find VAE Rhythm in most of the 39 variants of 31 generators we test, including the closed-source Sora, Kling 3.0 and Seedance 2.0. We use the rhythm as a zero-shot score, as a plug-in for existing detectors and as a data engine that pairs real videos with their VAE reconstructions to train our detector CaDet. On DF26, the training-free rhythm score outperforms all 15 retrained baselines, and as a plug-in it improves all 19 tested detectors by 6.7% to 23.7% AUROC. CaDet achieves the best AUROC on AIGVDBench, DF26 and three 2026 closed-source models, and its variant trained without any generated video still exceeds 90% on AIGVDBench.
