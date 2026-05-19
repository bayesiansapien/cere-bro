---
source: farmer/huggingface
farmed: 2026-05-19T09:55:00.432604+00:00
arxiv_id: 2605.18601
url: https://huggingface.co/papers/2605.18601
arxiv_url: https://arxiv.org/abs/2605.18601
date: 2026-05-19
---

# Incantation: Natural Language as the Action Interface for Multi-Entity Video World Models

Modern interactive video world models have achieved impressive visual fidelity, yet lack fine-grained multi-entity control and cross-entity, cross-world generalization. We trace this gap to the action interface: standard control protocols (e.g. animation IDs, device inputs, scene-level captions) bind action semantics to specific entities or engines at design time. We propose natural language as the interface to unlock expressiveness that no prior interface can achieve, and we present Incantation, the first interactive video world model with per-latent-frame (0.25 s) natural-language conditioning that supports simultaneous multi-entity control and concept-level cross-entity transfer beyond any fixed rendering pipeline. We pair a pretrained bidirectional video backbone with frame-local text cross-attention, and enable real-time long-horizon streaming through ODE-initialized Self-Forcing distillation with a RoPE-decoupled sliding KV-cache. We surpass the Action-Index baseline on cross-entity transfer (89% vs. 43%) and out-of-vocabulary prompts (90% vs. 0%), and our 2-step student sustains 19.7 FPS at 480p with stable FVD over 2-hour rollouts. We further apply the same architecture and training recipe to The King of Fighters, changing only the per-entity action vocabulary slots. We have released a preview subset of the Incantation dataset at https://huggingface.co/datasets/zhush/incantation-elden-ring-scenes, containing manually collected Elden Ring player-boss combat clips with structured action-oriented metadata. Larger-scale Elden Ring and KOF data will be released with the full project.
