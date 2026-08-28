---
source: farmer/huggingface
farmed: 2026-08-28T14:50:07.734667+05:30
arxiv_id: 2608.27168
url: https://huggingface.co/papers/2608.27168
arxiv_url: https://arxiv.org/abs/2608.27168
date: 2026-08-28
---

# Magpie: Real-Time World Renderer for Interactive Games

Modern game development relies heavily on conventional graphics pipelines. High-quality visual content requires modeling, material authoring, animation, lighting, effects, and runtime optimization, making asset production expensive and extending the development cycle of game prototypes. Recently, video foundation models are beginning to change film and video production, but games differ from linear media, they require not only continuous and realistic imagery, but also stable and reproducible gameplay rules, object states, and interaction outcomes. We present Magpie, a real-time generative world-rendering system for interactive games. Magpie separates gameplay execution from visual generation. Designers define scenes and rules in a game engine. At runtime, the Game Engine resolves player actions and maintains world state, while an independent Render Server generates visual output from white-box frames produced by the engine. Magpie provides a system-level implementation path for applying generative models to real-time game rendering. It preserves gameplay designability and reproducibility, and reduces the dependence of early game prototypes on complete visual assets.
