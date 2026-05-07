# PhysForge: Physics-Grounded 3D Asset Generation

**Source:** HuggingFace Daily Papers (2026-05-07)
**Paper:** [arXiv 2605.05163](https://arxiv.org/abs/2605.05163) · [HF](https://huggingface.co/papers/2605.05163)
**Raw:** [raw](../../raw/huggingface/2026-05-07-physforge-generating-physics-grounded-3d-assets-interactive.md)

## TL;DR

PhysForge is a two-stage framework for generating interactive, physics-grounded 3D assets, supported by PhysDB (150,000 assets with four-tier physical annotations). Stage 1: a VLM acts as a "physical architect" producing a Hierarchical Physical Blueprint with material, functional, and kinematic constraints. Stage 2: a physics-grounded diffusion model realises the blueprint, synthesising geometry alongside kinematic parameters via a KineVoxel Injection (KVI) mechanism. Output is simulation-ready assets for interactive 3D content and embodied agents.

## Tier note

Tier 4. Listed for completeness. The two-stage VLM-plans-then-diffusion-realises pattern is a clean factoring of high-level constraints from low-level synthesis.
