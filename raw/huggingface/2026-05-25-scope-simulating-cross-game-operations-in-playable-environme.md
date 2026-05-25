---
source: farmer/huggingface
farmed: 2026-05-25T08:23:16Z
arxiv_id: 2605.23345
url: https://huggingface.co/papers/2605.23345
arxiv_url: https://arxiv.org/abs/2605.23345
date: 2026-05-25
---

# SCOPE: Simulating Cross-game Operations in Playable Environments for FPS World Models

Interactive world models for first-person shooter (FPS) games must resolve high-frequency overlapping control signals at every frame without disrupting unaffected regions. Existing methods inject actions globally and train on single titles, failing under dense FPS inputs. We observe that FPS actions are spatially selective: discrete events such as firing or reloading affect only a localized region around the weapon (the scope), while continuous camera and movement signals govern stable surroundings. We propose SCOPE, which inserts a conditioning module into each transformer block of a pretrained video diffusion model. It reshapes features into per-pixel temporal sequences so that each position computes its action response from local visual content. This separates in-scope effects from out-of-scope generation without segmentation labels. We also introduce CrossFPS, the first multi-game FPS dataset with frame-aligned action telemetry. It comprises 69K clips from 7 titles with 10-DoF controller signals, curated to remove gameplay bias. The model learns general visual-to-action mappings rather than game-specific patterns, enabling zero-shot transfer to unseen scenes. Experiments confirm strong action responsiveness, precise scope separation, and effective cross-game generalization.
