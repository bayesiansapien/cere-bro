---
source: farmer/huggingface
farmed: 2026-05-04T00:00:00Z
arxiv_id: 2605.00658
url: https://huggingface.co/papers/2605.00658
arxiv_url: https://arxiv.org/abs/2605.00658
date: 2026-05-04
---

# UniVidX: A Unified Multimodal Framework for Versatile Video Generation via Diffusion Priors

Recent progress has shown that video diffusion models (VDMs) can be repurposed to solve various multimodal graphics tasks. However, existing approaches predominantly train separate models for each specific problem setting. This practice locks models into fixed input-output mappings, and typically ignores the joint correlations across modalities. In this paper, we present UniVidX, a unified multimodal framework designed to leverage VDM priors to enable versatile video generation. Our goal is to (i) master diverse pixel-aligned tasks by formulating them as conditional generation problems within multimodal space, (ii) adapt to modality-specific distributions without compromising the backbone's native priors, and (iii) ensure cross-modal consistency during synthesis. Concretely, we propose three key designs: 1) Stochastic Condition Masking (SCM): by randomly partitioning modalities into clean conditions and noisy targets during training, we enable the model to learn omni-directional conditional generation rather than fixed mappings. 2) Decoupled Gated LoRA (DGL): we attach per-modality LoRAs and activate them when a modality serves as a generation target, thereby preserving the VDM's strong priors. 3) Cross-Modal Self-Attention (CMSA): we explicitly share keys/values across modalities while maintaining modality-specific queries, facilitating information exchange and inter-modal alignment. We validate our framework by instantiating it in two domains: 1) UniVid-Intrinsic for RGB videos and their intrinsic maps (albedo, irradiance, normal), and 2) UniVid-Alpha for blended RGB videos and their constituent RGBA layers. Experimental results demonstrate that both models achieve performance competitive with state-of-the-art methods across distinct tasks. Notably, they exhibit robust generalization capabilities in in-the-wild scenarios, even when trained on limited datasets of fewer than 1k videos. Our project page: https://houyuanchen111.github.io/UniVidX.github.io/
