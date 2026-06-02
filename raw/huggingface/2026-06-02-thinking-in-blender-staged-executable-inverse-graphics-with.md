---
source: farmer/huggingface
farmed: 2026-06-02T09:40:06Z
arxiv_id: 2606.02580
url: https://huggingface.co/papers/2606.02580
arxiv_url: https://arxiv.org/abs/2606.02580
date: 2026-06-02
---

# Thinking in Blender: Staged Executable Inverse Graphics with Vision-Language Models

Inverse graphics is a longstanding and highly underconstrained problem that seeks to reconstruct images as editable 3D scenes which can be rendered, relit, and manipulated. In this work, we investigate whether pretrained vision-language models (VLMs) can perform executable inverse graphics directly from a single image by reconstructing a scene as an editable Blender program, without relying on specialized 2D or 3D foundation models, differentiable rendering, or multi-view supervision. We introduce Staged Executable Inverse Graphics (SEIG), an agentic framework that reconstructs a 3D scene from a single image by progressively refining scene factors including geometry, materials, composition, and lighting directly in executable Blender code space. We evaluate our framework across diverse scenes using a range of reconstruction metrics spanning pixel-level, perceptual, and semantic fidelity. Our experiments show that staged reconstruction substantially improves reconstruction fidelity, highlighting the importance of task decomposition for executable inverse graphics with general-purpose VLMs. Finally, we showcase various downstream applications enabled by the reconstructed editable Blender scenes.
