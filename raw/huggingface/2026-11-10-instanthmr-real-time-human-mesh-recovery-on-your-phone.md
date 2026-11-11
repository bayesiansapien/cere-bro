---
source: farmer/huggingface
farmed: 2026-11-11T05:06:31.327706+00:00
arxiv_id: 2611.09195
url: https://huggingface.co/papers/2611.09195
arxiv_url: https://arxiv.org/abs/2611.09195
date: 2026-11-10
---

# InstantHMR : Real-Time Human Mesh Recovery on Your Phone

Real-time 3D human mesh recovery from a single image on mobile devices is a challenging problem with many applications, including robotics, biomechanics, AR/VR, and exergames. Current state-of-the-art models are either too slow to run efficiently on mobile devices or sacrifice accuracy for speed. We present InstantHMR, a family of open-source single-image regressors suited for mobile inference, based on the Momentum Human Rig (MHR) parametric model and trained exclusively on publicly available annotations from the SAM 3D Body dataset. Our approach achieves remarkable performance on a Samsung Galaxy S23 NPU, recovering a 6,890-vertex body mesh in 5.5 ms per person, and 0.98 ms on an NVIDIA RTX 4070 GPU. This speed surpasses all existing methods we evaluated. On mobile, it is 12x faster than the single mobile-compatible method that slightly outperforms ours in accuracy, while achieving competitive accuracy with 40.0 mm PA-MPJPE on 3DPW, 48.8 mm on EMDB and 41.7 mm on RICH. To ensure fair comparisons, we re-evaluate 11 state-of-the-art methods under a unified protocol aligned with the closest MHR-based competitors, including Meta's official MHR-to-SMPL conversion, and report their reproduction results. Additionally, we measure latency across eight different targets, ranging from desktop TensorRT to two phone NPUs. Code and models are available at https://github.com/Naturalpad-studio/InstantHMR.
