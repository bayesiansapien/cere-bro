---
source: farmer/huggingface
farmed: 2026-11-03T14:58:56.498284+05:30
arxiv_id: 2610.37918
url: https://huggingface.co/papers/2610.37918
arxiv_url: https://arxiv.org/abs/2610.37918
date: 2026-11-02
---

# Venus-DefakerOne2: A Vision-Forensics Foundation Model with Broader Coverage

Real-world forgery is inherently heterogeneous: it manifests not only as digital manipulation but also as physical spoofing, and is carried not only by images but also by videos. Despite substantial progress, a unified anti-forgery foundation model covering such a broad threat spectrum remains absent. In this paper, we present Venus-DefakerOne2, which substantially extends the forensic capability boundary along both the forgery-form and media-type dimensions. Trained on tens of millions of open-source and in-house samples, it incorporates two key designs. Tide-Style-Tuning alternates LoRA and full-parameter fine-tuning to balance computational efficiency, generalization, and hard-sample fitting while mitigating catastrophic forgetting. Entropy-based Test Adaptation determines the optimal prediction modality by analyzing prediction entropy. Venus-DefakerOne2 achieves new state-of-the-art performance across a comprehensive suite of benchmarks, including DeepFake faces (96.7%), AI-generated images (93.3%), tampered documents (87.6%), manipulated natural images (89.6%), physical spoofs (93.1%), and AI-generated videos (96.0%). It significantly outperforms both specialized expert models and its predecessor, DefakerOne, establishing itself as a powerful and versatile foundation model for binary-decision forensic tasks.
