---
source: farmer/huggingface
farmed: 2026-06-11T08:27:36Z
arxiv_id: 2606.11683
url: https://huggingface.co/papers/2606.11683
arxiv_url: https://arxiv.org/abs/2606.11683
date: 2026-06-11
---

# Reason, Then Re-reason: Cross-view Revisiting Improves Spatial Reasoning

Spatial reasoning from egocentric videos is inherently challenging because the observable evidence is constrained by the camera trajectory. Existing methods rely on single-turn inference, forcing models to resolve geometric ambiguity through semantic priors rather than verifiable evidence. We argue that spatial reasoning should be revisitable: conclusions formed under limited evidence should remain open to revision when complementary viewpoints become available. Building on this insight, we propose Reason, then Re-reason (ReRe), a training-free, inference-time framework with two phases: in the Reason Phase, an MLLM forms a spatial hypothesis from the original video; in the Re-reason Phase, it verifies or revises the hypothesis by observing a synthesized novel-view video. To enable effective cross-view revisiting, we design a Geometry-to-Video pipeline that renders strategically complementary novel views from predicted 3D geometry. These views feature an elevated, oblique perspective with scene-spanning coverage, while preserving the MLLM's native video interface without architectural modifications. Extensive evaluations on VSI-Bench and STI-Bench demonstrate that ReRe substantially boosts open-source MLLMs to rival proprietary state-of-the-art performance. Project page: https://zhenjiemao.github.io/ReRe/
