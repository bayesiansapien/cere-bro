---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.06960
url: https://huggingface.co/papers/2610.06960
arxiv_url: https://arxiv.org/abs/2610.06960
date: 2026-10-07
---

# DistScene: Object-to-Scene Distillation for 3D Scene Generation

We present DistScene, a framework for single-image compositional 3D scene generation by jointly modeling the environment and individual objects. Unlike existing methods that represent scenes primarily as collections of objects, we model the environment as an explicit scene component to provide geometric context for object placement. Specifically, we introduce Scene-Frame Generation, which jointly generates separate environment and object components in a shared coordinate frame, allowing their geometry and relative placement to be learned together. Then we introduce Object-Centric Refinement to refine each object in a local frame with scene context. Finally, we develop Object-to-Scene Distillation to transfer pretrained object-generation priors to scene generation through automatically composed and rendered synthetic scenes. Evaluations on indoor and outdoor benchmarks demonstrate improved scene-level spatial coherence over the evaluated baselines. Project page: https://coolbeam.github.io/DistScene/
