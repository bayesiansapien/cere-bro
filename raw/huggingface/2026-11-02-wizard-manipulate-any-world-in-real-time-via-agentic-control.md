---
source: farmer/huggingface
farmed: 2026-11-03T14:58:56.497265+05:30
arxiv_id: 2610.40339
url: https://huggingface.co/papers/2610.40339
arxiv_url: https://arxiv.org/abs/2610.40339
date: 2026-11-02
---

# Wizard: Manipulate Any World in Real Time via Agentic Control

Recent advances in video world models have enabled the generation of increasingly realistic and interactive virtual environments, opening new possibilities for player-customizable gameplay. Agentic frameworks further advance this direction by decoupling explicit game logic and controllable world representations from visual generation. However, existing approaches support only simple game settings and predefined motion patterns, generalize poorly to unseen environments and characters, and offer limited real-time interactivity. In this paper, we introduce Wizard, an agentic game world model that enables real-time, precise control over character motions while generalizing zero-shot across novel scenes, characters, and actions. To achieve this, we construct a diverse dataset spanning 750 scenes and 178 characters, incorporating skeleton and geometry information as structured representations. We leverage these representations as intermediate proxies to condition a video generation model, together with an adaptive masking mechanism that improves alignment between the conditioning signals and generated video rollouts. Furthermore, we introduce an agentic framework that explicitly maintains and updates game states, allowing players to freely configure their virtual worlds and exercise fine-grained control over character motions while preserving visual quality and gameplay consistency. By combining agentic control with structured proxy-based generation, our framework unlocks new possibilities for player-driven game creation with real-time, generalizable, and mechanically consistent world simulation.
