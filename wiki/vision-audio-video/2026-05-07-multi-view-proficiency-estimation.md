# Parameter-Efficient Multi-View Proficiency Estimation

**Source:** HuggingFace Daily Papers (2026-05-07)
**Paper:** [arXiv 2605.03848](https://arxiv.org/abs/2605.03848) · [HF](https://huggingface.co/papers/2605.03848)
**Raw:** [raw](../../raw/huggingface/2026-05-07-parameter-efficient-multi-view-proficiency-estimation.md)

## TL;DR

A short survey-style contribution covering three recent multi-view proficiency estimation methods on Ego-Exo4D: SkillFormer (parameter-efficient discriminative architecture for selective multi-view fusion), PATS (temporal sampling that preserves locally dense excerpts of fundamental movements), and ProfVLM (proficiency estimation as conditional language generation, producing a label and expert-style feedback through a gated cross-view projector). Up to 20x fewer trainable parameters and 3x fewer training epochs than video-transformer baselines.

## Tier note

Tier 4. The shift from closed-set classification to interpretable feedback generation matches the broader trend of rubric-with-rationale evaluation (parallel to MedSkillAudit, also 05-07) but applied to motor skills.
