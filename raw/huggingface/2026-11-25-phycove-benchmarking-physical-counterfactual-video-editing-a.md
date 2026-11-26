---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.29184
url: https://huggingface.co/papers/2611.29184
arxiv_url: https://arxiv.org/abs/2611.29184
date: 2026-11-25
---

# PhyCoVE: Benchmarking Physical Counterfactual Video Editing across Diverse Material Dynamics

Physical counterfactual video editing turns a source video and a language-specified physical edit at a given execution frame into a counterfactual video that shows how the scene would evolve after the edit. Existing evaluations with counterfactual target videos mainly cover object removal or specific rigid-body motions, although real scenes also involve elastic deformation, fluid flow, and interactions among rigid bodies, elastic solids, and fluids. We introduce PhyCoVE, a benchmark of 533 cases on 110 source videos that covers rigid, elastic, and fluid dynamics in five interaction patterns, with edits that remove an object, change a physical quantity, or insert a new object. For the simulated cases, a language model proposes scene designs, coding agents build them with solvers suited to each material and physically based rendering and then simulate each edit from the source scene state, and humans check every stage. For the real cases, we record continuously from one camera position before and after each edit. We also propose counterfactual fidelity, a metric that applies across materials and their interactions and measures how much of the physical change from the source video to the target video a generated video reproduces. We evaluate seven open-source and commercial video editing models and find that counterfactual fidelity ranks them nearly as human preference does, but even the best model reproduces only about one seventh of the physical change. The models change how a scene looks but rarely how it evolves, whereas a physical edit requires understanding the dynamics that it changes. Physical counterfactual video editing thus remains far from solved, and PhyCoVE provides a foundation for developing and evaluating methods for it.
