---
source: farmer/huggingface
farmed: 2026-11-10T05:05:44.204624+00:00
arxiv_id: 2611.09017
url: https://huggingface.co/papers/2611.09017
arxiv_url: https://arxiv.org/abs/2611.09017
date: 2026-11-09
---

# Frontier3DBench: Benchmarking Coding Agents for 3D Creation across Objects, Scenes, and Interactive Open Worlds

Coding agents combine visual understanding with program execution, offering a new route to automated 3D creation. By translating images and instructions into editable programs, they bring reconstruction, generation, and editing into a shared workflow. Yet existing benchmarks fragment evaluation across task scopes and protocols, leaving their capabilities across construction levels unclear. We propose Frontier3DBench, a unified benchmark of 145 tasks across 9 categories spanning object, scene, and interactive open-world creation, with joint evaluation of appearance, structure, and behavior. Experiments with 11 model-harness configurations reveal strengths that vary by level: GPT-6.1-sol leads the object and scene levels and achieves the highest overall score of 66.02/100, whereas GPT-6-astra leads interactive world construction. However, all configurations score lower on reference reconstruction than on text-driven generation in object and scene tasks. Producing plausible content thus remains easier than reproducing specified geometry, layouts, and visual details. Moreover, generated worlds average 83.08/100 on local mechanisms but only 20.82 on motion clearance and 30.26 on stateful workflows: individual mechanisms often function, whereas complete activities that require coordinated actions and persistent state remain difficult. These results identify reference fidelity and coordinated activity completion as central bottlenecks for coding agents in 3D creation.
