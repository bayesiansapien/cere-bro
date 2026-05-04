# UniVidX — Unified Multimodal Framework for Versatile Video Generation

**Source:** HuggingFace Daily Papers
**Raw:** [raw/huggingface/2026-05-04-unividx-unified-multimodal-framework-versatile-video-generation.md](../../raw/huggingface/2026-05-04-unividx-unified-multimodal-framework-versatile-video-generation.md)
**arXiv:** https://arxiv.org/abs/2605.00658
**Date:** 2026-05-04
**Tier:** 3 — video generation

## TL;DR

UniVidX leverages video-diffusion-model (VDM) priors for omni-directional conditional video generation across modalities (RGB, intrinsic maps, alpha layers). Three design choices: (1) Stochastic Condition Masking — randomly partitioning modalities into clean conditions vs noisy targets so the model learns omni-directional generation rather than fixed mappings; (2) Decoupled Gated LoRA — per-modality LoRAs activated only when a modality is the target, preserving native VDM priors; (3) Cross-Modal Self-Attention — shared keys/values across modalities with modality-specific queries. Two instantiations: UniVid-Intrinsic (RGB ↔ albedo/irradiance/normal), UniVid-Alpha (RGB ↔ RGBA layers). Robust generalization with <1k training videos.

## Why this matters

Tier 3 for cere-bro reading priorities, but the SCM "random masking → omni-directional generation" idea generalizes beyond video — it is the multimodal analog of denoising diffusion's training objective. Pairs with the world-model architecture survey (Ken Huang 05-03) on the diffusion-as-substrate thread.

## Connections to prior wiki pages

- **Ken Huang World Models (05-03)** — UniVidX is concrete evidence of the "autoregressive temporal + diffusion spatial" hybrid pattern Astra formalizes.
- **Seedance 2 Video Generation (04-16)** — earlier video-generation reference.
- **Diffusion Templates Plugin Framework (04-30)** — same per-modality-adapter pattern (DGL ↔ template plugins).
