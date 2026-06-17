---
source: farmer/huggingface
farmed: 2026-06-17T10:05:49Z
arxiv_id: 2606.17861
url: https://huggingface.co/papers/2606.17861
arxiv_url: https://arxiv.org/abs/2606.17861
date: 2026-06-17
---

# GameCraft-Bench: Can Agents Build Playable Games End-to-End in a Real Game Engine?

Game generation is an emerging application of coding agents, requiring models to transform natural-language specifications into playable interactive systems. Unlike traditional coding tasks, game generation takes place within a game engine, where scripts, scenes, assets, rendering, and runtime interactions must jointly produce coherent gameplay. We formalize end-to-end game generation as the problem of producing a complete game artifact that realizes a specification through observable player-game interaction in a target environment. We argue that evaluating this setting requires three desiderata: Engine Grounding, Artifact Completeness, and Interactive Verification. We propose an interaction-grounded evaluation framework that assesses executable gameplay through replayed demonstrations and rubric-guided multimodal judging. We instantiate this framework as GameCraft-Bench, a benchmark comprising 140 Godot tasks across 15 game families. Evaluations of frontier coding agents show that end-to-end game generation remains highly challenging: the strongest agent achieves only 41.46%, and most agents score below 40%. Further analysis reveals that while agents often implement recognizable mechanics, they struggle to deliver complete games with sufficient content, functional visual feedback, and coherent presentation. See https://tongxuluo.github.io/gamecraft-bench-website for demos, code, and data.
