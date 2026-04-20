---
source: farmer/huggingface
farmed: 2026-04-20T00:00:00
arxiv_id: 2604.16254
url: https://huggingface.co/papers/2604.16254
arxiv_url: https://arxiv.org/abs/2604.16254
date: 2026-04-20
---

# ArtifactNet: Detecting AI-Generated Music via Forensic Residual Physics

We present ArtifactNet, a lightweight framework that detects AI-generated music by reframing the problem as forensic physics -- extracting and analyzing the physical artifacts that neural audio codecs inevitably imprint on generated audio. A bounded-mask UNet (ArtifactUNet, 3.6M parameters) extracts codec residuals from magnitude spectrograms, which are then decomposed via HPSS into 7-channel forensic features for classification by a compact CNN (0.4M parameters; 4.0M total). We introduce ArtifactBench, a multi-generator evaluation benchmark comprising 6,183 tracks (4,383 AI from 22 generators and 1,800 real from 6 diverse sources). Each track is tagged with bench_origin for fair zero-shot evaluation. On the unseen test partition (n=2,263), ArtifactNet achieves F1 = 0.9829 with FPR = 1.49%, compared to CLAM (F1 = 0.7576, FPR = 69.26%) and SpecTTTra (F1 = 0.7713, FPR = 19.43%) evaluated under identical conditions with published checkpoints. Codec-aware training (4-way WAV/MP3/AAC/Opus augmentation) further reduces cross-codec probability drift by 83% (Delta = 0.95 -> 0.16), resolving the primary codec-invariance failure mode. These results establish forensic physics -- direct extraction of codec-level artifacts -- as a more generalizable and parameter-efficient paradigm for AI music detection than representation learning, using 49x fewer parameters than CLAM and 4.8x fewer than SpecTTTra.
