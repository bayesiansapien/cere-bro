# APEX: Aesthetic-Informed Popularity Prediction for AI-Generated Music

**Source:** HuggingFace Daily Papers (2026-05-07)
**Paper:** [arXiv 2605.03395](https://arxiv.org/abs/2605.03395) · [HF](https://huggingface.co/papers/2605.03395)
**Raw:** [raw](../../raw/huggingface/2026-05-07-apex-large-scale-multi-task-aesthetic-popularity-ai-music.md)

## TL;DR

APEX is a multi-task framework for AI-generated music popularity, trained on 211k songs / 10k hours from Suno and Udio. It jointly predicts engagement-based popularity (streams, likes) and five perceptual aesthetic quality dimensions from frozen MERT audio embeddings. Aesthetic features improve preference prediction on Music Arena (out-of-distribution pairwise human-preference battles across eleven generative music systems), demonstrating that aesthetic and engagement signals capture complementary aspects of AI-generated music.

## Tier note

Tier 4. Listed for completeness. The interesting external signal is that **AI-generated music is now a measurable consumption surface large enough to support 211k-song training corpora.** That is a market-data point worth filing for the industry-pulse thread.
