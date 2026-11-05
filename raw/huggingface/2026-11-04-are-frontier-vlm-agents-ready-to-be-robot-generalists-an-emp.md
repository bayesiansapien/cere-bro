---
source: farmer/huggingface
farmed: 2026-11-05T20:36:55.360653+05:30
arxiv_id: 2610.00854
url: https://huggingface.co/papers/2610.00854
arxiv_url: https://arxiv.org/abs/2610.00854
date: 2026-11-04
---

# Are Frontier VLM Agents Ready to Be Robot Generalists? An Empirical Study with the Embodied Agent Arena

A robot generalist must interpret a scene, act on it, and satisfy every condition of a task. How far do frontier vision-language models (VLMs) meet these demands? We introduce Embodied Agent Arena, evaluating ten VLM agents across Geometry, Spatial Reasoning, Affordance, Task Planning, and Manipulation. Its 1,000 cases combine 32 established sources with GeoProbe, our 168-case benchmark for camera, motion, depth, and scale estimation. A minimal harness leaves task decisions to the model through source-native interfaces. Closed-weight models lead all five domains, whereas open-weight VLMs show useful spatial reasoning but substantially lower planning and manipulation success. Beneath these averages, similar geometric errors conceal different scale and shape distortions, and valid region estimates need not identify usable action points. During execution, agents can achieve early subgoals yet lose object control, bind an action to the wrong receiving region, or stop before the required physical state holds. Additional computation does not uniformly resolve these failures: code repair can restore execution without completing the task, while self-review can reverse correct judgments. Failure costs also differ: the strongest planners concentrate failed-token expenditure in prolonged body-control tasks, whereas other models fail broadly across procedures. Matched traces show how successful recovery uses feedback to restore a missing prerequisite and advance the remaining task.
