---
source: farmer/huggingface
farmed: 2026-11-10T05:05:44.206158+00:00
arxiv_id: 2610.36896
url: https://huggingface.co/papers/2610.36896
arxiv_url: https://arxiv.org/abs/2610.36896
date: 2026-11-09
---

# PREEN: Exemplar-Based Color Style Transfer with Smartphone Editor Presets

We present PREEN (Preset Regression via an Exemplar-based Editor Network), which casts color style transfer as regression onto the 29 parameters of a deterministic image editor. Given a content image and a style reference, PREEN predicts a preset, a vector of editor slider values that is interpretable and editor-consumable, not a raster image. The key obstacle is supervision, since an arbitrary real reference lacks a preset ground truth. We therefore supervise with a style-transfer teacher, whose target looks we invert into the editor's parameter space as pseudo-presets, then pretrain a CLIP-conditioned regressor and refine it with LoRA under an image-level CIELAB loss. On the human-curated PST50 benchmark, PREEN applies the reference's color while preserving structural fidelity, leading the baselines on pixel- and perceptual-fidelity metrics. The preset is compact and predicted at sub-second on-device latency. The low-dimensional subspace also exposes a single inference-time strength knob that traces a continuous default-to-vivid trajectory in one forward pass, with every intermediate state a valid editor preset. A two-axis human study shows that raters prefer the vivid end for matching the reference but the default as a standalone photo, a trade-off the knob spans without retraining.
