---
source: farmer/huggingface
farmed: 2026-06-12T09:05:40Z
arxiv_id: 2606.08063
url: https://huggingface.co/papers/2606.08063
arxiv_url: https://arxiv.org/abs/2606.08063
date: 2026-06-12
---

# Robust-U1: Can MLLMs Self-Recover Corrupted Visual Content for Robust Understanding?

Multimodal Large Language Models (MLLMs) have demonstrated remarkable success in visual understanding, yet their performance degrades significantly under real-world visual corruptions. While existing robustness enhancement approaches exist, they are limited: black-box feature alignment lacks interpretability, and white-box text-based reasoning cannot restore lost pixel-level details. This work investigates a fundamental research question: Can MLLMs recover corrupted visual content by themselves? To address this, we propose Robust-U1, a novel framework that equips MLLMs with explicit visual self-recovery capability for robust understanding. The approach comprises three core stages: supervised fine-tuning for initial reconstruction, reinforcement learning with dual rewards (pixel-level SSIM and semantic-level CLIP similarity) for aligning high visual quality, and multimodal reasoning that jointly considers both the corrupted input and the recovered image. Extensive experiments demonstrate that Robust-U1 achieves state-of-the-art robustness on the real-world corruption benchmark and maintains superior performance under adversarial corruptions on general VQA benchmarks. Analysis confirms that high-quality visual recovery directly enhances reasoning performance, establishing self-recovery as a critical mechanism for robust visual understanding. The source code is available at https://github.com/jqtangust/Robust-U1.
