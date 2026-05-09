---
source: farmer/huggingface
farmed: 2026-05-09T03:37:34Z
arxiv_id: 2605.04647
url: https://huggingface.co/papers/2605.04647
arxiv_url: https://arxiv.org/abs/2605.04647
date: 2026-05-09
---

# ReflectDrive-2: Reinforcement-Learning-Aligned Self-Editing for Discrete Diffusion Driving

We introduce ReflectDrive-2, a masked discrete diffusion planner with a separate action expert for autonomous driving that represents plans as discrete trajectory tokens and generates them through parallel masked decoding. This discrete token space enables in-place trajectory revision: AutoEdit rewrites selected tokens using the same model, without requiring an auxiliary refinement network. We use a two-stage procedure: structure-aware perturbations supervised for expert trajectory recovery, then fine-tuning the full decision-draft-reflect rollout with reinforcement learning. On NAVSIM, ReflectDrive-2 achieves 91.0 PDMS with camera-only input and 94.8 PDMS in a best-of-6 oracle setting, while running at 31.8 ms average latency on NVIDIA Thor.
