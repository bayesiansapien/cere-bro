---
source: farmer/huggingface
farmed: 2026-05-20T09:54:59.528138+00:00
arxiv_id: 2605.19587
url: https://huggingface.co/papers/2605.19587
arxiv_url: https://arxiv.org/abs/2605.19587
date: 2026-05-20
---

# SceneCode: Executable World Programs for Editable Indoor Scenes with Articulated Objects

Indoor scene synthesis underpins embodied AI, robotic manipulation, and simulation-based policy evaluation, where a useful scene must specify not only what the environment looks like, but also how its objects are structured. Existing pipelines, however, typically represent generated content as static meshes and inherit articulation only from curated asset libraries, which limits object-level controllability and prevents new interactable assets from being produced on demand. We address this gap by formulating physically interactable indoor scene synthesis as programmatic world generation, and present SceneCode, a framework that compiles a natural language prompt into an executable, code-driven indoor world rather than a collection of opaque meshes. A room-level agentic backbone first turns the prompt into a structured house layout and emits per-object AssetRequests through a planner--designer--critic loop. Each request is then routed to one of five code-generation strategies and converted into a synthesized part-wise Blender Python programs that are validated through an execution-guided repair-and-refine loop. The resulting programs are compiled into simulation-ready assets, and exported as SDF for physics simulation. A persistent scene-state registry links object requests, executable programs, rendered geometry, and simulation assets, turning scene assembly into a traceable and locally editable world-building process. We evaluate SceneCode across scene-level synthesis, object-level asset quality, human judgment, and downstream robot interaction. Results show that executable world programs improve prompt-faithful indoor scene generation and produce assets with cleaner mesh structure, and simulator-loadable articulation metadata. Project page: this https URL .
