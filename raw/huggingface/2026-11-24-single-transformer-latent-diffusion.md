---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.922791+00:00
arxiv_id: 2611.29064
url: https://huggingface.co/papers/2611.29064
arxiv_url: https://arxiv.org/abs/2611.29064
date: 2026-11-24
---

# Single-Transformer Latent Diffusion

Latent generative models typically rely on three separate networks: an encoder that tokenizes pixels, a generator that models the latent distribution, and a decoder that maps latents back to pixels. UNITE recently merged the first two into a single generative encoder trained in one stage, but its decoder remains a separate network. We ask whether this last network can be folded in too, so that one diffusion transformer encodes, generates, and decodes. Simply letting the shared backbone decode does not help. What makes it work is to cast all three modes as position-aligned sequence maps over one fully shared backbone, distinguished only by a mode token and the timestep. The resulting model, UNIFIED, is simple: one network trained from scratch in a single stage with only reconstruction and flow-matching losses, without adversarial losses or pretrained encoders (e.g., DINO). On ImageNet-1K 256x256 at matched parameters, UNIFIED improves gFID over UNITE at three sizes (~60M, ~115M, and ~215M) and reaches 2.08 with 215M parameters, the lowest among compared models under 250M parameters. On text-to-image generation, UNIFIED-B (218M) reaches a GenEval score of 0.87 at 512x512, exceeding single-stage pixel diffusion models with around one billion parameters. Full unification of latent diffusion is thus not merely feasible but beneficial.
