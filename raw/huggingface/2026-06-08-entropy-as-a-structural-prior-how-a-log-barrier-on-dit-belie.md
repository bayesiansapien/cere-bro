---
source: farmer/huggingface
farmed: 2026-06-08T09:23:13Z
arxiv_id: 2606.07207
url: https://huggingface.co/papers/2606.07207
arxiv_url: https://arxiv.org/abs/2606.07207
date: 2026-06-08
---

# Entropy as a Structural Prior: How a Log-Barrier on DiT Belief Space Drives Musical Diversity and Development

Confidence-based loss weighting is usually avoided in generative models because it accelerates errors when the model is confidently wrong, but this intuition breaks down in supervised diffusion training. We introduce the Eisbach log-barrier, a parameter-free weight derived from the entropy of the DiT output's spatial energy distribution: high entropy damps the gradient, while low entropy preserves it. Applied to LoRA fine-tuning of Stable Audio 3 Medium on MusicCaps, it unexpectedly yields stronger thematic development, clearer acoustic differentiation, and higher textural diversity than unweighted training, the opposite of mode collapse. This works because in supervised diffusion the gradient direction is locked to ground truth, so confidence only scales the step size, and because temporal entropy downweights flat samples while preserving high-contrast ones. The result is an online, self-referential data curriculum that emerges purely from the forward pass, with analyzed noise-level dynamics and testable predictions.
