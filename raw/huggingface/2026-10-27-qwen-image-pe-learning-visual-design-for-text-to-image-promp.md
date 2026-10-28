---
source: farmer/huggingface
farmed: 2026-10-28T10:37:11+05:30
arxiv_id: 2610.33472
url: https://huggingface.co/papers/2610.33472
arxiv_url: https://arxiv.org/abs/2610.33472
date: 2026-10-27
---

# Qwen-Image-PE: Learning Visual Design for Text-to-Image Prompt Enhancement

Learning visual design is essential for prompt enhancement (PE) to turn underspecified user requests into coherent visual specifications for text-to-image (T2I) generation. Existing methods preserve user intent and improve overall visual appeal, with less explicit emphasis on fine-grained design dimensions. To address this gap, we introduce Qwen-Image-PE, which learns visual design through two-stage training. Supervised fine-tuning with Caption-Based Reverse Distillation (CRD) uses dense captions of well-designed images as design supervision. Reinforcement learning with Groupwise Design Reward (GDR) jointly compares all candidate images for the same request to refine lighting, composition, layout, and detail. On Qwen-Image-Bench with Qwen-Image-2.1, Qwen-Image-PE-397B improves over original requests by 7.81 points, while Qwen-Image-PE-9B outperforms all evaluated PE baselines. Further evaluations show gains in visual design, aesthetics, image quality, and human preference. We find that PE scales along three axes: training data, model size, and information density, with sufficient information density as a prerequisite for effective enhancement. Moreover, we demonstrate that Qwen-Image-PE generalizes to four additional T2I backbones, even surpassing native prompt enhancers on HunyuanImage-2.1 and FLUX 3 Image Klein. We release Qwen-Image-PE-9B at https://huggingface.co/Qwen/Qwen-Image-2.1-PE-T2I.
