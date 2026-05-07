# HERMES++: Unified Driving World Model for 3D Scene Understanding and Generation

**Source:** HuggingFace Daily Papers (2026-05-07)
**Paper:** [arXiv 2604.28196](https://arxiv.org/abs/2604.28196) · [HF](https://huggingface.co/papers/2604.28196)
**Raw:** [raw](../../raw/huggingface/2026-05-07-hermes-plus-plus-unified-driving-world-model-3d-scene.md)

## TL;DR

HERMES++ unifies 3D scene understanding and future geometry prediction in a single driving world model. A BEV (bird's-eye-view) representation feeds the LLM-compatible spatial structure, LLM-enhanced world queries transfer knowledge from the understanding branch, a Current-to-Future Link conditions geometric evolution on semantic context, and Joint Geometric Optimisation enforces structural integrity through explicit constraints plus implicit latent regularisation. Outperforms specialist baselines on both future point cloud prediction and 3D scene understanding.

## Tier note

Tier 4 (3D mapping / driving). Listed for completeness. The interesting structural claim, that semantic-understanding queries can guide geometric prediction within a unified world model, generalises beyond driving but is not tested outside it.

## Related

- [2026-04-30-x-wam-4d-world-model-robotics.md](2026-04-30-x-wam-4d-world-model-robotics.md)
- [2026-05-07-physforge-physics-grounded-3d-assets.md](2026-05-07-physforge-physics-grounded-3d-assets.md)
