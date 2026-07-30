---
source: farmer/huggingface
farmed: 2026-07-30T12:41:02.128718+05:30
arxiv_id: 2607.25802
url: https://huggingface.co/papers/2607.25802
arxiv_url: https://arxiv.org/abs/2607.25802
date: 2026-07-30
---

# Explicit Layer Modeling for Video Object Insertion and Layer Decomposition

Most video editing systems still lack explicit layered video representations, limiting their ability to perform realistic compositing, object reuse, and consistent manipulation. This limitation is especially pronounced in video object insertion and video layer decomposition, where existing methods rely on implicit inference or per-scene optimization due to the absence of explicit foreground-layer supervision. We introduce TriLayer, a large-scale triplet video dataset containing aligned composite, background, and foreground videos, where the foreground layers include both object appearance and associated visual effects. This explicit supervision enables models to learn layered video representations directly rather than inferring them implicitly. Building on this dataset, we propose DBL-Diffusion, a dual-branch diffusion framework that jointly models RGB composites and RGBA foreground layers through shared denoising and cross-branch interaction. We instantiate the framework in two tasks: DBL-Insert for layered object insertion, which generates explicit RGBA layers for realistic compositing and flexible post-editing, and DBL-Decompose for video layer decomposition, which recovers foreground and background layers using triplet supervision. Experiments demonstrate that explicit layer modeling substantially improves both insertion fidelity and decomposition quality.
