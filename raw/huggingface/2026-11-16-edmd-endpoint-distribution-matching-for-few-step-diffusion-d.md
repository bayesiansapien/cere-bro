---
source: farmer/huggingface
farmed: 2026-11-17T08:29:01.999588+00:00
arxiv_id: 2611.17194
url: https://huggingface.co/papers/2611.17194
arxiv_url: https://arxiv.org/abs/2611.17194
date: 2026-11-16
---

# eDMD: Endpoint Distribution Matching for Few-Step Diffusion Distillation

Distribution matching distillation (DMD) has emerged as a leading paradigm for distilling diffusion models into few-step students, where an auxiliary fake score model tracks the student's distribution and the discrepancy between the teacher and fake predictions drives the student toward the teacher. In multi-step distillation, although only the student's final output is delivered, existing methods train the fake model on intermediate states or across all denoising steps. Consequently, the student's update signal becomes entangled with intermediate distributions, which can distort the matching direction and remain nonzero even after the student's final outputs already match the teacher distribution. To resolve this mismatch, we propose Endpoint Distribution Matching Distillation (eDMD), which trains a single shared fake model exclusively on the student's final outputs and uses it to correct every denoising step. Our theoretical analysis proves that this endpoint reference guarantees that the distribution matching term vanishes if and only if the student's final output distribution matches the teacher's, regardless of intermediate distributions. Beyond the fake reference, we further strengthen teacher supervision through a precise teacher (PT) that replaces single-step guided predictions with short multi-step trajectories on the final noise interval, paired with a calibrated query density for intermediate steps. Experiments on SD3-Medium, FLUX.2-klein (4B and 9B), and Qwen-Image-2.1 demonstrate that eDMD consistently outperforms existing distribution matching methods for 4-step generation.
