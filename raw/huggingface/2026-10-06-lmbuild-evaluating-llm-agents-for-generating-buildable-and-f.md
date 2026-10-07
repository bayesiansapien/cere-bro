---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.04292
url: https://huggingface.co/papers/2610.04292
arxiv_url: https://arxiv.org/abs/2610.04292
date: 2026-10-06
---

# LMBuild: Evaluating LLM Agents for Generating Buildable and Functional Structures

LLM-based agents are increasingly capable of generating complex 3D structures, with the potential to reshape how objects are designed and realized in the physical world. Yet, producing elegant geometry is fundamentally different from producing objects that can be built and perform their intended functions. Existing evaluations largely focus on geometric quality while overlooking physical realizability. We introduce LMBuild, a benchmark for evaluating LLM agents on generating buildable and functional structures. LMBuild represents generated objects as assembled structures comprising part decompositions, joints, materials, and sequences. To support reproducible evaluation, we provide a unified framework consisting of: (1) an interactive environment in which agents can use tools to retrieve, create, and place components to construct objects; (2) a curated benchmark that repurposes established CAD datasets and augments them with knowledge from Wikipedia; and (3) a evaluation framework covering structural soundness, functional affordance, design quality, and physical realization. Evaluations across 30 systems reveal several intriguing findings: (a) Soundness and alignment are no longer the primary bottlenecks for frontier closed-source models, while functional affordance and physical operability remain substantially more challenging; (b) stronger models more effectively create new components, whereas weaker models tend to rely on retrieval; and (c) providing functional specifications substantially improves part completeness, kinematics, and physical operability. These results show that generating real-world structures requires deeper reasoning about functional affordances, mechanics, and designing and creating novel components. We expect LMBuild to provide a foundation for measuring progress and incentivizing research toward agents that generate buildable and functional structures.
