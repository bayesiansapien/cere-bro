---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.906403+00:00
arxiv_id: 2611.28010
url: https://huggingface.co/papers/2611.28010
arxiv_url: https://arxiv.org/abs/2611.28010
date: 2026-11-26
---

# Beyond Code and Pixels: Co-Generating Editable and Visually Rich Presentations

Generating PPTX presentations is a structured task that requires semantic planning, visual composition, precise layout, and editability, motivating collaboration among specialized agents. However, programmatic methods offer editability but often produce rigid designs, while image-based methods provide visual richness but flatten content into difficult-to-edit pixels. A hybrid system can combine these strengths, but must coordinate interdependent decisions across content, layout, and appearance. To address this challenge, we propose SlidesWeaver, a hybrid multi-agent system that coordinates language and vision agents through shared deck- and slide-level states. Specifically, it uses staged multimodal commitment, diffusion-based composition planning, and two generation schedules for different priorities between composition freedom and accurate text preservation, while preserving native text and geometry. Across 1,728 generations spanning 24 system-model configurations, SlidesWeaver achieves consistently superior overall quality across all evaluated dimensions while maintaining structural control, editability, and practical generation efficiency.
