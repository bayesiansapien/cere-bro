---
source: farmer/huggingface
farmed: 2026-11-03T14:58:56.502819+05:30
arxiv_id: 2610.41260
url: https://huggingface.co/papers/2610.41260
arxiv_url: https://arxiv.org/abs/2610.41260
date: 2026-11-02
---

# SketchDirector: Complex Scene Sketching via Agentic Layout Reasoning and Detail Refinement

Existing sketch generation methods often rely on image guidance and are largely limited to individual objects or simplified scenes, leaving text-guided complex scene sketching underexplored. We present SketchDirector, an agentic framework that mimics the human sketching workflow for automatic multi-concept scene sketching. Given a scene-level text prompt, SketchDirector first employs a large language model~(LLM) to decompose the scene into multiple draft assets, where each is represented by a set of Bézier curves. Then, an agentic reasoning loop iteratively plans and executes their spatial arrangement, guided by self-evolving memory. Finally, a detail refinement module leverages diffusion priors to enhance sketch quality while preserving geometric structure. To support future research and applications in multi-concept scene sketch generation, we further introduce the MCSketch8K dataset, comprising editable vector assets, compositional layouts, and object-level manipulation annotations. Extensive experiments show that SketchDirector outperforms state-of-the-art baselines in semantic and compositional quality while effectively preserving overall contour organization during refinement. The project page is: https://yiki77.github.io/SketchDirector/{https://yiki77.github.io/SketchDirector/}.
