---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.26853
url: https://huggingface.co/papers/2610.26853
arxiv_url: https://arxiv.org/abs/2610.26853
date: 2026-10-20
---

# InfiniDream: Open-Ended Photorealistic 3D Worlds Through Procedural Generation

Procedural generation plays a key role in synthetic data creation and game development, offering greater controllability, editability, and diversity than static mesh representations. However, VLM-based code generation often produces relatively simple 3D assets, while sophisticated photorealistic procedural systems require extensive manual development. Existing VLM-guided procedural methods remain largely constrained by predefined factories and APIs, limiting their ability to create novel asset types. We introduce InfiniDream, a VLM-driven framework for open-ended procedural 3D world generation. First, we propose Symbolically Constrained Asset Generation, which leverages existing procedural algorithms to create novel, photorealistic assets while preserving editability and seed-based diversity. Second, we develop an end-to-end text-to-world pipeline that combines semantic scene planning with Deterministic Frustum-Guided Grid Placement to construct large-scale 3D worlds with precise object placement, procedural population, and animation. Extensive evaluations on 100 object and 20 scene generation tasks demonstrate improvements across four perceptual metrics. Diversity analysis, ablation studies, and human preference evaluations further validate the effectiveness of our framework. Project page: https://yichuanh.github.io/infinidream-page/
