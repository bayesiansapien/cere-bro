---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.16355
url: https://huggingface.co/papers/2610.16355
arxiv_url: https://arxiv.org/abs/2610.16355
date: 2026-10-16
---

# PINT: A Unified Model with Shared Predictive Intent for Robot Manipulation

Generalist robot manipulation can benefit from pretrained vision-language models (VLMs) for semantic reasoning and video generation models (VGMs) for world modeling. However, existing unified models that directly fuse them through shared attention at multiple layers can make it harder to draw on their specialized capabilities. We introduce PINT, a unified model that coordinates semantic reasoning, world modeling, and action generation through a shared chunk-level Predictive Intent while preserving expert-specific pathways. PINT inserts learnable Intent Tokens into the VLM sequence to form this representation, conditioning both the VGM and an Action Expert (AE). It replaces only the VGM's prompt conditioning and retains the VGM at inference, where the AE reads its representations through one-way attention. Rather than prescribing what Predictive Intent should encode, PINT learns it jointly from the native prediction objectives of the VLM, VGM, and AE, which provide complementary views of the same upcoming task execution. Training uses two stages: Stage 1 freezes the VGM so that future video prediction shapes Predictive Intent with task-relevant future dynamics, while Stage 2 fixes the learned Intent and adapts the VGM and AE. Without embodied pretraining, PINT achieves strong in-distribution (ID) performance and substantially improves out-of-distribution (OOD) generalization, reaching 15.5% on RoboTwin 2.0-Hard compared with 1.8% for Fast-WAM and 3.2% for StarVLA, and 79.5% on LIBERO-Plus compared with 51.5% and 75.0%, respectively. Across five real-world bimanual tasks, PINT reaches 68% ID and 24% OOD success, compared with 35%/9% for pretrained Motus and 67%/35% for pretrained π_{0.5}.
