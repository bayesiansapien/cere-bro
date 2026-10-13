---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.224028+05:30
arxiv_id: 2610.13316
url: https://huggingface.co/papers/2610.13316
arxiv_url: https://arxiv.org/abs/2610.13316
date: 2026-10-12
---

# ThinkDrag: Semantic Drag-Based Image Editing with Visual Reasoning

Drag-based image editing provides an intuitive interface for spatially controlled image manipulation by allowing users to specify handle and target points. Existing methods have made substantial progress through optimization-based, one-step, and feed-forward formulations, but they often interpret drag instructions as geometric displacements. This limits their effectiveness when the desired edit depends on interpreting image content and inferring a plausible semantic transformation from sparse point constraints. We introduce ThinkDrag, a unified multimodal framework for drag-based image editing with visual reasoning. ThinkDrag is trained to associate point constraints with meaningful object- and scene-level transformations, and can optionally produce an explicit reasoning trace that interprets the intended edit before image generation. This reasoning trace improves interpretability, particularly for ambiguous drags. Drag Endpoint Markers, motivated by an analysis of cross-image attention, provide an explicit correspondence signal that grounds each drag in image space. To support this framework, we construct a supervised dataset of semantic drag transformations paired with reasoning traces and introduce DragBench++, a benchmark targeting challenging drag-based editing scenarios with reference edit solutions. Experiments show that ThinkDrag achieves state-of-the-art performance, improving generation quality and plausibility while maintaining competitive point-following precision.
