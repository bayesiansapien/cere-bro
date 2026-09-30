---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.931772+00:00
arxiv_id: 2609.33399
url: https://huggingface.co/papers/2609.33399
arxiv_url: https://arxiv.org/abs/2609.33399
date: 2026-09-29
---

# SciGen-Verifier: A Multimodal Reasoner for Explainable Verification in Scientific Image Generation

In realistic education, a solution is often expressed not only in words but in a drawing--a circuit, a geometric construction, a function plot--and a teacher must grade the drawing as carefully as the text. Recent advances in unified multimodal models have enabled scientific image generation, yet verifying the correctness of these specialized visual outputs remains a critical bottleneck: errors often arise from intricate domain knowledge, structural reasoning, and multi-step instruction rather than surface-level artifacts. Existing verifiers mainly target natural images and compress judgement into scalar scores, leaving scientific coverage and explainable feedback for error correction underexplored. To bridge this gap, we make three main contributions. (1) We construct SciGen-Verify, a benchmark dedicated to explainable verification of scientific image generation, spanning instruction following, multidisciplinary reasoning, and world knowledge domains. It contains a three-tier hierarchical protocol over the binary judgement, supporting explanation, and corrective editing instruction. (2) We develop SciGen-Verifier, a reasoning-driven multimodal verifier trained via cold-start supervised fine-tuning followed by a curriculum-based two-stage reinforcement learning pipeline. The rubric-guided process rewards first strengthen scientific reasoning exploration and outcome rewards subsequently align output with ground-truth annotation. (3) On SciGen-Verify, SciGen-Verifier achieves competitive performance against much larger proprietary models. It further serves as a practical online critic for iterative image rectification.
