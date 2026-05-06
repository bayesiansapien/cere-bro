# FASH-iCNN: Editorial Fashion Identity via Multimodal CNN Probing

**Date:** 2026-04-30
**Source:** [HuggingFace](https://huggingface.co/papers/2604.26186) | [Paper](https://arxiv.org/abs/2604.26186)
**Raw:** [raw/huggingface/2026-04-30-fash-icnn-editorial-fashion-identity-multimodal-cnn-probing.md](../../raw/huggingface/2026-04-30-fash-icnn-editorial-fashion-identity-multimodal-cnn-probing.md)

## TL;DR

Adobe Research trains a CNN on 87K Vogue runway images (15 fashion houses, 1991–2024) and probes which visual channels carry "house identity." Removing color costs only 10.6pp; removing texture costs 37.6pp. Texture and luminance — not color — are the primary carriers of editorial identity. Tier 4 for Amit's interests; recorded for completeness.

## Note for the wiki

The probing methodology (channel ablation to localize identity signal) is a lightweight, generalizable probe. Same approach could be used to localize *style* in language models (which channels carry register, persona, etc.). Worth noting if a future style-attribution paper crosses the digest.
