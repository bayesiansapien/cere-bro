---
source: farmer/huggingface
farmed: 2026-10-24T12:49:20.880249+00:00
arxiv_id: 2610.30753
url: https://huggingface.co/papers/2610.30753
arxiv_url: https://arxiv.org/abs/2610.30753
date: 2026-10-23
---

# FilmFlow: Agentic System for 3D Virtual Film Cinematography

Complex camera motion is central to visual storytelling, yet translating cinematographic intent into controllable, executable camera trajectories remains challenging. We introduce FilmFlow, an agentic framework that converts natural-language instructions or reference videos into explicit camera trajectories for dynamic 3D environments. To generate these trajectories, a Director agent constructs executable camera plans by composing high-level motions from concurrent atomic operations that jointly control translation, rotation, and framing. The Director is supported by three specialized agents: an Interpreter that extracts scene-grounded cinematographic intent, a Scout that selects initial viewpoints, and a Critic that evaluates rendered results and provides visual feedback for iterative plan refinement. We also introduce CinemaBench, comprising 150 Blender scenes from self-created and licensed sources, with five camera instructions per scene for 750 text-directed tasks and 60 reference videos associated with a subset of scenes. CinemaBench supports evaluation of both text-directed camera generation and video reference-directed camera generation. Across a diverse set of evaluated baselines, FilmFlow achieves the strongest benchmark performance and the highest user preference, demonstrating effective spatial reasoning, temporal coordination, and visual composition for executable 3D cinematography.
