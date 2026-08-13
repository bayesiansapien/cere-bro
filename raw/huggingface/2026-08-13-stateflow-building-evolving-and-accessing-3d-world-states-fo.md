---
source: farmer/huggingface
farmed: 2026-08-13T03:36:17.258300+00:00
arxiv_id: 2608.12314
url: https://huggingface.co/papers/2608.12314
arxiv_url: https://arxiv.org/abs/2608.12314
date: 2026-08-13
---

# StateFlow: Building, Evolving, and Accessing 3D World States for Previsualization

Previsualization is an intermediate layer between ideas and production in film, games, architecture, and urban design. It lets creators iteratively refine scenes, actions, cameras, and spatial-temporal dynamics. Yet existing generative methods rely on simple prompts to jointly control all of these factors through one-shot image or video synthesis, offering weak controllability and limited support for iterative editing. Fundamentally, a world comprises multiple elements with geometry, appearance, and other attributes, together with cameras. Different frames are produced through local modifications or recombinations of this shared state, which is otherwise largely reused. Therefore, we argue that the missing component is an explicit and persistent working state. To address this, we present StateFlow, a state-centric framework for generative previsualization. Rather than generating videos in one shot, StateFlow uses an editable 3D world to organize scene structure, evolution, and cameras, while off-the-shelf video models enhance visual quality when higher fidelity is desired. This world is maintained as a persistent structured 3D state of scene elements and camera configurations, serving as the core working representation for previsualization. Built on this insight, StateFlow has three stages to construct, evolve, and access the world state. State construction lifts generated 2D content into a coherent 3D world through prior-guided, conflict-aware dual-view initialization, while State evolution translates user intent into structured state transitions while preserving world memory, avoiding full-scene regeneration for each edit. State access uses render-feedback reflection to refine camera plans into visually feasible trajectories, avoiding reliance on VLM semantics alone. Experiments show that StateFlow produces high-quality 3D worlds for video creation and game-like prototyping.
