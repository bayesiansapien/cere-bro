# End-to-End Autoregressive Image Generation with 1D Semantic Tokenizer

**Source:** HuggingFace Daily Papers
**Raw:** [raw/huggingface/2026-05-04-end-to-end-autoregressive-image-generation-1d-semantic-tokenizer.md](../../raw/huggingface/2026-05-04-end-to-end-autoregressive-image-generation-1d-semantic-tokenizer.md)
**arXiv:** https://arxiv.org/abs/2605.00503
**Date:** 2026-05-04
**Tier:** 3 — image generation, tokenizer design

## TL;DR

Joint end-to-end training of visual tokenizer + autoregressive generative model, contrasting with the standard two-stage pipeline (train tokenizer, then train generator). Direct generation-result supervision flows back to the tokenizer. Vision foundation models are leveraged to improve the 1D tokenizer for AR modeling. Reports SOTA FID 1.48 *without classifier-free guidance* on ImageNet 256×256.

## Why this matters

Mostly Tier 3, but the joint-training pattern echoes a thread in cere-bro: "co-training the substrate and the generator improves both." CoPD (05-01) was the language-model version (co-evolving policy + distillation); this is the visual version. Compare also with the 1D-Ordered Tokens for Test-Time Search paper (04-20).

## Connections to prior wiki pages

- **CoPD Co-Evolving Policy Distillation (05-01)** — same end-to-end-substrate-with-generator philosophy in language.
- **1D Ordered Tokens for Test-Time Search (04-20)** — same 1D token paradigm.
- **Edit-R1 (05-01)** — verifier-based RL for image editing; pairs naturally with end-to-end tokenizers.
