---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.936144+00:00
arxiv_id: 2609.36219
url: https://huggingface.co/papers/2609.36219
arxiv_url: https://arxiv.org/abs/2609.36219
date: 2026-09-29
---

# LeRF: Learning Reference Coordinate Frames for Perspective Taking Reasoning

Perspective taking is a fundamental component of spatial intelligence, requiring models interpret spatial relations from a specified viewpoint, such as that of another entity or an imagined observer. Despite the increasing spatial reasoning capabilities of Vision-Language Models (VLMs), they still struggle with perspective taking, often defaulting to the camera viewpoint when a query requires reasoning from a different perspective. We introduce Learning Reference Coordinate Frames for Perspective Taking (LeRF), a framework that trains VLMs to construct and use explicit reference frames for viewpoint-dependent reasoning. Given an image and a query, LeRF decides whether a coordinate frame is necessary. If so, it grounds the reference entity and predicts the frame's origin and entity-centered reference frame. A lightweight renderer overlays the frame onto the image, enabling subsequent reasoning over these visual cues without external perception models or explicit 3D reconstruction. To learn this process, we first perform supervised fine-tuning to teach selective tool invocation and reference coordinate frame prediction, followed by reinforcement learning on spatial VQA pairs to improve frame-guided reasoning. Across diverse perspective-taking benchmarks, LeRF consistently improves over its backbone and achieves strong performance against existing open-source methods. Further evaluations also show improved reference-frame grounding and orientation estimation, supporting the effectiveness of learned reference frames for viewpoint-dependent reasoning.
