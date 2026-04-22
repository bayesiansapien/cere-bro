---
source: farmer/huggingface
farmed: 2026-04-22T00:00:00
arxiv_id: 2604.19636
url: https://huggingface.co/papers/2604.19636
arxiv_url: https://arxiv.org/abs/2604.19636
date: 2026-04-22
---

# CoInteract: Physically-Consistent Human-Object Interaction Video Synthesis via Spatially-Structured Co-Generation

Synthesizing human-object interaction (HOI) videos has broad practical value in e-commerce, digital advertising, and virtual marketing. However, current diffusion models, despite their photorealistic rendering capability, still frequently fail on (i) the structural stability of sensitive regions such as hands and faces and (ii) physically plausible contact (e.g., avoiding hand-object interpenetration). We present CoInteract, an end-to-end framework for HOI video synthesis conditioned on a person reference image, a product reference image, text prompts, and speech audio. CoInteract introduces two complementary designs embedded into a Diffusion Transformer (DiT) backbone. First, we propose a Human-Aware Mixture-of-Experts (MoE) that routes tokens to lightweight, region-specialized experts via spatially supervised routing, improving fine-grained structural fidelity with minimal parameter overhead. Second, we propose Spatially-Structured Co-Generation, a dual-stream training paradigm that jointly models an RGB appearance stream and an auxiliary HOI structure stream to inject interaction geometry priors. During training, the HOI stream attends to RGB tokens and its supervision regularizes shared backbone weights; at inference, the HOI branch is removed for zero-overhead RGB generation. Experimental results demonstrate that CoInteract significantly outperforms existing methods in structural stability, logical consistency, and interaction realism.
