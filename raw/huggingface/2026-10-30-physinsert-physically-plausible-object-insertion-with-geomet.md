---
source: farmer/huggingface
farmed: 2026-10-31T08:06:35.160325+00:00
arxiv_id: 2610.40453
url: https://huggingface.co/papers/2610.40453
arxiv_url: https://arxiv.org/abs/2610.40453
date: 2026-10-30
---

# PhysInsert: Physically Plausible Object Insertion with Geometric Priors and Bidirectional Object-Scene Interactions

We present PhysInsert, a framework for physically plausible reference-based object insertion that jointly adapts objects and their surrounding scenes. Existing methods often rely on masked inputs, generation-based pairs, or training pairs with limited viewpoint variation, leaving pose and illumination adaptation and bidirectional object-scene interactions insufficiently constrained. We construct the Insert World dataset with strictly aligned Blender-rendered counterfactual pairs and object references across viewpoints and lighting conditions. Building on these data, Geometry-Guided Adaptation couples a VGGT geometry stream with image and text streams under target-scene feature supervision to guide spatially consistent insertion. Complementary 2D Object-Scene Spatial Supervision jointly supervises object occupancy and environmental changes while grounding spatial instructions in object regions through image-text attention. We introduce PhysInsert-Bench with dedicated cross-environment and cross-view cases requiring illumination and pose adaptation beyond appearance copying. Experiments on PhysInsert-Bench and DreamBooth demonstrate improved image fidelity; a user study further shows more accurate placement and improved lighting integration, perspective, and pose plausibility.
