---
source: farmer/huggingface
farmed: 2026-04-18T00:00:00Z
arxiv_id: 2604.14629
url: https://huggingface.co/papers/2604.14629
arxiv_url: https://arxiv.org/abs/2604.14629
date: 2026-04-18
---

# Switch-KD: Visual-Switch Knowledge Distillation for Vision-Language Models

Vision-Language Models (VLMs) have shown remarkable capabilities in joint vision-language understanding, but their large scale poses significant challenges for deployment in resource-constrained scenarios. Knowledge Distillation (KD) offers a viable way to improve model capabilities without increasing model size or data requirements, making deployment more efficient. However, applying KD to VLMs is challenged by modality-specific supervision: although multimodal knowledge in VLMs is fused within the language space, current methods supervise each modality separately without explicitly addressing multimodal alignment, leading to inconsistent multimodal knowledge transfer. To address this, we propose Switch-KD, a visual-switch distillation framework that unifies vision-language knowledge transfer within a shared text-probability space. Switch-KD comprises two key components: (1) Visual-Switch Distillation, which switches the student's visual outputs into the teacher's language pathway to construct cross-modal probabilistic references for implicit visual knowledge transfer; and (2) Dynamic Bi-directional Logits Difference (DBiLD) loss, which adaptively aligns informative probability regions while preserving the distributional structures of teacher and student through bidirectional supervision. Guided by Switch-KD, a 0.5B TinyLLaVA effectively distills rich multimodal knowledge from its 3B teacher, yielding an average improvement of 3.6 points across 10 multimodal benchmarks without any architectural modification.
