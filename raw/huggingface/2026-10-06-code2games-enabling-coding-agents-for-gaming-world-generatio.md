---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.05033
url: https://huggingface.co/papers/2610.05033
arxiv_url: https://arxiv.org/abs/2610.05033
date: 2026-10-06
---

# Code2Games: Enabling Coding Agents for Gaming World Generation

Generating a high-quality gaming world from a natural-language game intent requires joint reasoning about scene structure, spatial layout, gameplay objectives, interactive entities, and executable gameplay logic. Existing coding agents can generate individual assets, scenes, or scripts, but often struggle to maintain consistency across these components. We propose Code2Games, an agentic framework that builds a structured gaming world upon a base Blender world generated from the same game intent. Code2Games coordinates scene analysis, gameplay planning, constrained gaming-world generation, and gaming-engine customization through a shared scene-gameplay representation with persistent element correspondence. After world generation, Code2Games adapts the generated world to Unreal Engine 5 and employs an execution-guided reconstruction process that uses compilation diagnostics, runtime feedback, and gameplay test results to resolve inconsistencies arising during engine adaptation. To systematically evaluate gaming-world generation, we introduce the GameCode4D benchmark, which comprises ten fixed game prompts spanning different levels of scene and gameplay complexity. We evaluate the generated results across four dimensions: visual quality, interactive fidelity, multimodal artifact quality, and playable-game quality. Experiments demonstrate that, compared with direct gaming-world generation by coding agents and existing baseline methods, Code2Games consistently improves the visual quality and interactive fidelity of generated gaming worlds, as well as the quality of the resulting games after engine adaptation.
