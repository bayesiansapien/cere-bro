---
source: farmer/huggingface
farmed: 2026-06-18T00:00:00Z
arxiv_id: 2606.17539
url: https://huggingface.co/papers/2606.17539
arxiv_url: https://arxiv.org/abs/2606.17539
date: 2026-06-18
---

# Reinforcing Dual-Path Reasoning in Spatial Vision Language Models

Spatial VLMs have made substantial progress in geometric perception, yet complex spatial reasoning requiring multi-step inference over depth, distance, and scene relations remains challenging. Moreover, different spatial queries call for fundamentally different strategies: some are best addressed through purely linguistic, step-by-step deduction, while others require explicit 3D grounding before quantitative inference. We present Dual-Path Spatial Reasoning via Reinforcement Learning for Spatial VLMs (SR-REAL), a unified framework that equips a spatial VLM with two complementary reasoning paths: Language-Only Reasoning (LOR), which performs step-by-step linguistic deduction, and Detect-Then-Reason (DTR), which detects 3D geometric cues (e.g., centers or bounding boxes) via region tokens before explicit geometric inference. SR-REAL begins with a cold-start supervised fine-tuning stage that constructs LOR and DTR chain-of-thought supervision and exposes a region-to-3D interface, followed by RL that optimizes the policy model with accuracy and format rewards; for DTR, a discrete center-based detection reward further refines geometric alignment. Across diverse spatial benchmarks, SR-REAL significantly outperforms spatial VLM baselines: (i) a single RL-trained model supports both reasoning paths, with DTR excelling in region-aware tasks through precise 3D localization and LOR enhancing general spatial reasoning; (ii) jointly training both paths fosters mutual reinforcement; (iii) high-quality, blended cold-start data is crucial for stable RL optimization; and (iv) the model generalizes across datasets and domains without per-task tuning, demonstrating positive transfer between LOR and DTR.
