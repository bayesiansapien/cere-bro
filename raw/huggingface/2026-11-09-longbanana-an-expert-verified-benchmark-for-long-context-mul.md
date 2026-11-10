---
source: farmer/huggingface
farmed: 2026-11-10T05:05:44.202660+00:00
arxiv_id: 2611.06856
url: https://huggingface.co/papers/2611.06856
arxiv_url: https://arxiv.org/abs/2611.06856
date: 2026-11-09
---

# LongBanana: An Expert-Verified Benchmark for Long-Context Multi-Reference Image Synthesis

We introduce LongBanana, to our knowledge the first expert-designed and expert-verified benchmark for long-context multi-reference image synthesis in the age of agent-driven image generation. The task requires retrieving dispersed visual evidence, rejecting distractors, binding entities and relations, and composing one coherent final image from multiple references. LongBanana contains 90 carefully designed tasks organized by a 3-by-3 taxonomy; each task includes about 32 reference images, 20 constraints, and 50 evaluation items, yielding 4,670 expert-specified atomic evaluation items in total. Its graph-grounded evaluation design instantiates each task with reference images and an entity-relation graph, then converts node, edge, and whole-graph obligations into checklist items for Content Fidelity, Relational Binding, and Global Constraint Satisfaction. Reviewed expert labels include a 15% double-labeled subset with 89.4% exact agreement and 0.83 quadratic weighted kappa. We further introduce LongBanana-Gen, an agent-harness framework for long-horizon image generation; experiments show that minimal agent harnesses improve over direct generation, while a ReAct-Plan-Exec-Reflect (RPR) workflow yields harness-dependent gains by strengthening evidence grounding and repair. Together, LongBanana provides an auditable testbed for measuring dense visual evidence use and a shared target for developing stronger agent-driven image-generation systems. Code and data are available at the project page: https://long-banana.com/.
