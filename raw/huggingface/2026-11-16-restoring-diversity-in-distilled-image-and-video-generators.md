---
source: farmer/huggingface
farmed: 2026-11-17T08:29:02.002919+00:00
arxiv_id: 2611.18550
url: https://huggingface.co/papers/2611.18550
arxiv_url: https://arxiv.org/abs/2611.18550
date: 2026-11-16
---

# Restoring Diversity in Distilled Image and Video Generators by Probing Activations

Distilling diffusion models into few-step student models substantially reduces sampling latency, but induces severe diversity collapse: samples generated from different random seeds show minimal variation. In this work, we investigate the root cause of this failure by probing the internal representations of student models relative to their teachers. We find that distilled students maintain total activation variance comparable to their teachers, but concentrate it into substantially fewer directions. This directional collapse is localized to an identifiable intermediate block at the initial denoising step. Consequently, diversity collapse stems from a misallocation of activation variance rather than an inherent loss of generative capacity. Guided by this finding, we propose ReDiverse to reinstate the missing variance directions. At training time, ReDiverse-FT fine-tunes a lightweight adapter that regresses student activations onto the teacher's, reviving the teacher's feature variance characteristic. At inference time, ReDiverse-TF introduces a training-free mechanism that steers activations along precomputed teacher principal directions. Across image and video distillation benchmarks, ReDiverse consistently restores sample diversity while preserving generation quality, further supported by the user study.
