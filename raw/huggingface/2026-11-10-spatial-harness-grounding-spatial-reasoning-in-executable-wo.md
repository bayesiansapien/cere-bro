---
source: farmer/huggingface
farmed: 2026-11-11T05:06:31.327912+00:00
arxiv_id: 2611.11344
url: https://huggingface.co/papers/2611.11344
arxiv_url: https://arxiv.org/abs/2611.11344
date: 2026-11-10
---

# Spatial Harness: Grounding Spatial Reasoning in Executable World States with Physics Engines

Spatial reasoning requires understanding how objects and observers are arranged in a scene and how their relations change with viewpoint or movement. Vision-language models (VLMs) typically perform both steps through model-internal reasoning, forming an implicit scene interpretation from partial views and imagining the consequences of spatial transformations. A misread scene can lead to a wrong answer, while even a correct interpretation does not ensure that imagined transformations satisfy spatial constraints. We introduce Spatial Harness, which represents scenes as explicit and executable world states to ground spatial reasoning in physics-engine feedback. A Perceiver integrates scene constraints extracted from the question with specialized visual estimates to place objects and cameras in a shared coordinate frame. The resulting state is instantiated in a physics engine, where a Reasoner executes viewpoint changes and uses computed measurements and rendered views to guide reasoning. We evaluate on MindCube, SAT, MMSI-Bench, and SpatialRGPT-Bench with open- and closed-weight VLMs. On MindCube, Spatial Harness improves Qwen3.5-27B from 52.70% to 71.14%, surpassing pySpatial by 7.52 percentage points. Given identical annotated object and camera poses, it reaches 98.25% versus 71.81% for model-internal reasoning. Code is publicly available at: https://github.com/tmlr-group/Spatial-Harness
