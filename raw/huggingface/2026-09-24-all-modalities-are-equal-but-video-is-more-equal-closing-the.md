---
source: farmer/huggingface
farmed: 2026-09-25T17:06:04.306887+00:00
arxiv_id: 2609.27901
url: https://huggingface.co/papers/2609.27901
arxiv_url: https://arxiv.org/abs/2609.27901
date: 2026-09-24
upvotes: 7
authors: ["Ohad Rahamim", "Dvir Samuel", "Idan Schwartz", "Gal Chechik"]
---

# All modalities are equal, but video is more equal: Closing the Cross-Attention Gap in Joint Video Generation

**Authors:** Ohad Rahamim, Dvir Samuel, Idan Schwartz, Gal Chechik

**Upvotes:** 7

**Links:** [HuggingFace](https://huggingface.co/papers/2609.27901) · [arXiv](https://arxiv.org/abs/2609.27901)

Video is a rich representation of a physical event, capturing appearance, geometry, motion, and temporal evolution. Other modalities, such as 3D body motion or audio, encode narrower aspects of the same event. We find that joint multimodal diffusion transformers exhibit a corresponding asymmetry in cross-modal correspondence: companion modalities develop strong correspondences to video, but the reciprocal correspondences through which they constrain video remain substantially weaker. We express both directions as comparable correspondence distributions over video tokens and define their disagreement as the reciprocal correspondence gap. We introduce RecCAR, standing for Reciprocal Cross-modal Attention Regularization, a KL regularizer that uses the well-established video-to-modality correspondence as a fixed reference and aligns the weaker modality-to-video correspondence toward it. Across joint video-motion and video-audio generation, RecCAR improves the Human Anatomy score from 0.69 to 0.75 and reduces audio-video desynchronization from 0.804 to 0.752, while improving overall generation
