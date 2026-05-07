# RLDX-1: VLA Robotic Policy for Dexterous Humanoid Manipulation

**Source:** HuggingFace Daily Papers (2026-05-07)
**Paper:** [arXiv 2605.03269](https://arxiv.org/abs/2605.03269) · [HF](https://huggingface.co/papers/2605.03269)
**Raw:** [raw](../../raw/huggingface/2026-05-07-rldx-1-technical-report.md)

## TL;DR

RLDX-1 is a general-purpose Vision-Language-Action robotic policy for dexterous manipulation, built on a Multi-Stream Action Transformer (MSAT) that integrates heterogeneous modalities through modality-specific streams with cross-modal joint self-attention. Combined with synthetic training data for rare manipulation scenarios, human-like manipulation procedures, and inference optimisations, RLDX-1 achieves 86.8% success on ALLEX humanoid tasks where pi0.5 and GR00T N1.6 land around 40%.

## Why it matters

The 86.8% vs 40% gap is unusually large for a VLA paper. The architectural claim is that prior VLAs collapse modalities into a single fused representation, which loses the modality-specific structure that contact-rich manipulation requires. MSAT preserves the modality-specific streams and lets cross-modal attention discover the relationships explicitly.

## Tier note

Tier 4 by the wiki's reader profile (robotics hardware), but the cross-modal joint self-attention pattern is structurally adjacent to the heterogeneous-modality routing patterns the wiki tracks for unified language/vision foundation models.

## Related

- [2026-04-30-x-wam-4d-world-model-robotics.md](2026-04-30-x-wam-4d-world-model-robotics.md)
