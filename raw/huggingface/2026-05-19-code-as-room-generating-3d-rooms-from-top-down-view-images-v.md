---
source: farmer/huggingface
farmed: 2026-05-19T09:55:00.432604+00:00
arxiv_id: 2605.18451
url: https://huggingface.co/papers/2605.18451
arxiv_url: https://arxiv.org/abs/2605.18451
date: 2026-05-19
---

# Code-as-Room: Generating 3D Rooms from Top-Down View Images via Agentic Code Synthesis

Designing realistic and functional 3D indoor rooms is essential for a wide range of applications, including interior design, virtual reality, gaming, and embodied AI. While recent MLLM-based approaches have shown great potential for 3D room synthesis from textual descriptions or reference images, text-based methods struggle to capture precise spatial information, and existing image-conditioned agents suffer from instability and infinite looping when tasked with holistic room generation from top-down views. To address these limitations, we propose Code-as-Room, an MLLM-based agentic framework equipped with a structured execution harness, which represents 3D rooms with Blender codes. Given a top-down room image, the framework parses the reference image to extract scene elements and their spatial relationships, and synthesizes executable Blender code for geometry, materials, and lighting in a principled, multi-stage pipeline. A cross-stage memory module is maintained throughout to mitigate context forgetting inherent to existing agent-based frameworks. We further introduce a dedicated benchmark for code-based 3D room synthesis, encompassing various evaluation protocols. Based on our benchmark, comprehensive comparisons against existing agent-based methods are conducted to validate the effectiveness of our proposed execution harness.
