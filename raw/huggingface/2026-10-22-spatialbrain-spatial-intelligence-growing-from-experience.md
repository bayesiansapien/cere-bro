---
source: farmer/huggingface
farmed: 2026-10-23T08:19:34.193423+00:00
arxiv_id: 2610.29317
url: https://huggingface.co/papers/2610.29317
arxiv_url: https://arxiv.org/abs/2610.29317
date: 2026-10-22
---

# SpatialBrain: Spatial Intelligence Growing from Experience

Spatial reasoning requires more than access to geometric tools: a reasoner must decide when direct observation is sufficient and when to reconstruct, measure, or change reference frames. We present SpatialBrain, a framework that retains experience about these decisions while keeping its vision-language backbone fixed. The key distinction is between evidence about a scene and experience about how to reason with that evidence. 3DFusionMemory fuses current-scene observations into queryable spatial relations. A Spatial Skill Library provides reusable tool procedures, and Spatial Cognition associates task conditions with experience about when and how to use memory and skills. Completed trajectories are abstracted into process records and consolidated between task blocks, allowing later decisions to draw on earlier execution without transferring scene coordinates or reference answers. Across five spatial-reasoning benchmarks, SpatialBrain improves on direct answers from the same backbone on four and ties on the fifth. Component comparisons, experience-coverage curves, and traced resource decisions characterize how the framework accumulates and uses these resources.
