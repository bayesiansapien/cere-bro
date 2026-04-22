# Weight Disentanglement and Task Arithmetic: OrthoReg

**Date:** 2026-04-22  
**Source:** [HuggingFace](https://huggingface.co/papers/2604.17078) | [Paper](https://arxiv.org/abs/2604.17078)  
**Raw:** [raw/huggingface/2026-04-22-understanding-and-enforcing-weight-disentanglement-in-task-a.md](../../raw/huggingface/2026-04-22-understanding-and-enforcing-weight-disentanglement-in-task-a.md)

## TL;DR

Task arithmetic (merging models by adding their fine-tuned weight vectors) works well when tasks don't interfere — but the mechanism behind this was not well understood. This paper introduces Task-Feature Specialization (TFS) as the underlying principle: models that allocate distinct internal features to different tasks are more composable. TFS produces an observable geometric consequence — weight vector orthogonality. OrthoReg regularizes for this orthogonality during fine-tuning, consistently improving task arithmetic performance across methods.

## Key Findings

- **Task-Feature Specialization (TFS)** = model allocates distinct internal features to different tasks → sufficient condition for weight disentanglement
- TFS produces **weight vector orthogonality** as a geometric signature — observable and measurable
- **OrthoReg**: regularization method that enforces orthogonal structure on weight update vectors during fine-tuning
- Consistently and significantly enhances task arithmetic performance across multiple methods
- Provides a theoretical explanation for why task arithmetic works at all (previously empirical observation)

## Relation to Prior Wiki Knowledge

Task arithmetic is a model merging technique, related to the broader landscape of parameter-efficient methods. **ShadowPEFT (04-22)** and the distillation papers all work with weight perturbations; this paper addresses what makes those perturbations composable.

The orthogonality result connects to **Geometric Canary (04-21)**: that paper found that geometric structure of representations predicts steerability and drift. OrthoReg shows that enforcing specific geometric structure (orthogonality) at training time improves task composability. The common thread: geometry of model weights/representations is not just a diagnostic tool — it's a design target.

## Related Pages

- [Geometric Canary](2026-04-21-geometric-canary.md)
- [ShadowPEFT](../inference-efficiency/2026-04-22-shadowpeft-centralized-layer-space.md)
