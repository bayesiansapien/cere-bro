---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.310320+05:30
arxiv_id: 2610.03799
url: https://huggingface.co/papers/2610.03799
arxiv_url: https://arxiv.org/abs/2610.03799
date: 2026-10-08
---

# StepCAD: Mesh-to-CAD Code Generation via LLM Policy and Geometry-Guided Search

Recovering executable CAD programs from 3D meshes is challenging due to the compositional nature of CAD construction and the interaction between discrete modeling choices and continuous parameters. Many learning-based methods predict complete programs in a single pass and rely predominantly on sketch-extrude representations, limiting operation diversity and opportunities to correct geometric errors during reconstruction. We introduce StepCAD, a generative optimization approach that combines a state-conditioned CAD policy with geometry-guided search. Given an input mesh, the policy predicts construction actions conditioned on both target and intermediate geometry, and an IoU-guided tree search refines the resulting program through local edits. We also introduce ARCADE-1.5M, a large-scale dataset of 1.5M executable CAD programs spanning diverse operations, sequences with a maximum length of 150+ counted operations, and 12.5M intermediate state-action transitions. Experiments across multiple CAD reconstruction benchmarks show that StepCAD achieves state-of-the-art geometric reconstruction accuracy with consistently high validity, yielding up to 87.2% relative IoU improvement over the strongest evaluated baseline, with particularly large gains on complex shapes. Project page: https://ghadinehme.com/stepcad.github.io/
