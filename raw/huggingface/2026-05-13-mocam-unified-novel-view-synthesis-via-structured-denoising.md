---
source: farmer/huggingface
farmed: 2026-05-14T10:39:11Z
arxiv_id: 2605.12119
url: https://huggingface.co/papers/2605.12119
arxiv_url: https://arxiv.org/abs/2605.12119
date: 2026-05-13
---

# MoCam: Unified Novel View Synthesis via Structured Denoising Dynamics

Generative novel view synthesis faces a fundamental dilemma: geometric priors provide spatial alignment but become sparse and inaccurate under view changes, while appearance priors offer visual fidelity but lack geometric correspondence. Existing methods either propagate geometric errors throughout generation or suffer from signal conflicts when fusing both statically. We introduce MoCam, which employs structured denoising dynamics to orchestrate a coordinated progression from geometry to appearance within the diffusion process.MoCam first leverages geometric priors in early stages to anchor coarse structures and tolerate their incompleteness, then switches to appearance priors in later stages to actively correct geometric errors and refine details. This design naturally unifies static and dynamic view synthesis by temporally decoupling geometric alignment and appearance refinement within the diffusion process.Experiments demonstrate that MoCam significantly outperforms prior methods, particularly when point clouds contain severe holes or distortions, achieving robust geometry-appearance disentanglement.
