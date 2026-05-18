---
source: farmer/huggingface
farmed: 2026-05-18T04:19:52Z
arxiv_id: 2605.15320
url: https://huggingface.co/papers/2605.15320
arxiv_url: https://arxiv.org/abs/2605.15320
date: 2026-05-18
---

# FFAvatar: Few-Shot, Feed-Forward, and Generalizable Avatar Reconstruction

Avatar reconstruction has traditionally relied on per-subject optimization that requires hours of computation or on expensive preprocessing that limits scalability. We introduce FFAvatar, a generalizable feed-forward framework that reconstructs high-quality, animatable 3D Gaussian head avatars from few-shot unposed portrait images in seconds. FFAvatar fuses information from multiple source images into a unified canonical Gaussian representation through Multi-View Query-Former, which is animated via FLAME parameters predicted end-to-end directly from pixels, eliminating the overhead of offline FLAME extraction. We further propose a three-stage training curriculum that achieves both broad generalization and high-fidelity reconstruction: (i) scalable pretraining on extensive monocular video data with over 1M identities to learn strong generalizable priors; (ii) multi-view fine-tuning on a small but high-quality dataset of 360-degree captures to enhance geometric fidelity and extreme-view awareness; and (iii) optional personalization that adapts to specific identities for maximum fidelity within 500 optimization steps. Extensive experiments demonstrate that FFAvatar sets a new standard for identity preservation, geometric consistency, and animation fidelity. On the NeRSemble benchmark, it outperforms the state-of-the-art LAM by a substantial 5.5 PSNR gain. Furthermore, FFAvatar enables real-time deployment, reconstructing avatars in 2 seconds without personalization and 10 seconds with personalization, while supporting 49 FPS animation on a single NVIDIA A100 GPU.
