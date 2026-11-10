---
source: farmer/huggingface
farmed: 2026-11-10T05:05:44.206361+00:00
arxiv_id: 2611.09055
url: https://huggingface.co/papers/2611.09055
arxiv_url: https://arxiv.org/abs/2611.09055
date: 2026-11-09
---

# OmniLatent: Unified Latent for 3D Part Modeling

3D part decomposition is a central capability for editable asset creation, yet existing workflows typically segment a completed mesh as a post-processing step, making the result sensitive to geometric artifacts, texture ambiguity, and limited part-level annotations. We present OmniLatent, a unified latent modeling framework for 3D part decomposition. Instead of predicting part labels in isolation, OmniLatent learns a shared latent space that jointly encodes geometry, deformation, appearance, and binary part IDs, allowing data-rich geometric and visual priors to support data-scarce part learning. Given a single input image, the base model generates geometry, deformation, texture, and surface part IDs in one pass, producing a part-aware 3D asset without a separate segmentation stage. We further tune the pretrained model for two extensions: a point-prompt adapter that maps arbitrary 3D point prompts with binary part IDs into latent tokens for full segmentation, refinement, and part subdivision, and an amodal part completion model that completes partial surface masks into a coherent full-object decomposition through dynamic per-part token allocation, cross-attention to the given geometry latent, and alternating part-local and global attention. Extensive experiments show that OmniLatent produces semantically meaningful part segmentations with precise boundaries, supports interactive part editing, and completes partial part observations while preserving global object consistency.
