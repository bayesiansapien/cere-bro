---
source: farmer/huggingface
farmed: 2026-11-08T17:18:50.595476+00:00
arxiv_id: 2611.04386
url: https://huggingface.co/papers/2611.04386
arxiv_url: https://arxiv.org/abs/2611.04386
date: 2026-11-07
---

# StepX-OPD: Rethinking Multi-Teacher On-Policy Distillation in Diffusion Models

A deployable text-to-image diffusion model must hold several capabilities at once, such as instruction following, text rendering and human preference, and must sample in a few steps. Capabilities and few-step sampling are built in separate stages: a full-step model first consolidates capabilities through multi-teacher on-policy distillation, then serves as a fixed teacher for step distillation. Every full-step model we evaluate scores lower once compressed, and the second stage cannot begin until the first finishes. We introduce StepX-OPD, which merges the two stages: one student acquires every capability while learning to sample in a few steps, so frozen specialists supervise it on the states its own rollout visits rather than on a longer trajectory it never runs. Because a decomposition of the rollout's KL weights velocity mismatch most heavily near the clean end, we also regress the student's velocity on the low-noise part of the rollout. Separately, we find that capability integration makes models write prompt words into images on prompts that never asked for text, and we give a variant that lowers it. We evaluate on SD3.5-Medium and FLUX.1-dev across instruction following, text rendering, image quality and human preference. On both architectures, StepX-OPD attains the highest normalized average score among the four-step methods compared and exceeds the forty-step Flow-OPD model, and on SD3.5-Medium it trains with about 37% fewer GPU-hours than sequential DiffusionOPD followed by step distillation.
