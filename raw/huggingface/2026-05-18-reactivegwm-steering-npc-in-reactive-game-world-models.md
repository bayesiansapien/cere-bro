---
source: farmer/huggingface
farmed: 2026-05-18T04:19:52Z
arxiv_id: 2605.15256
url: https://huggingface.co/papers/2605.15256
arxiv_url: https://arxiv.org/abs/2605.15256
date: 2026-05-18
---

# ReactiveGWM: Steering NPC in Reactive Game World Models

Current game world models simulate environments from a subjective, player-centric perspective. However, by treating the Non-Player Character (NPC) merely as background pixels, these models cannot capture interactions between the player and NPC. In that sense, they act as passive video renderers rather than real simulation engines, lacking the physical understanding needed to model action-induced NPC reactivities. We introduce ReactiveGWM, a reactive game world model that synthesizes dynamic interactions between the player and NPC. Instead of entangling all interaction dynamics, ReactiveGWM explicitly decouples player controls from NPC behaviors. Player actions are injected into the diffusion backbone via a lightweight additive bias, while high-level NPC responses (e.g., Offense, Control, Defense) are grounded through cross-attention modules. Crucially, these modules learn a game-agnostic representation of interactive logic. This enables zero-shot strategy transfer: our learned modules can be plugged directly into off-the-shelf, unannotated world models of different games. This instantly unlocks steerable NPC interactions without any domain-specific retraining. Evaluated on two Street Fighter games, ReactiveGWM maintains fine-grain player controllability while achieving robust, prompt-aligned NPC strategy adherence, paving the way for scalable, strategy-rich interaction with the NPC.
