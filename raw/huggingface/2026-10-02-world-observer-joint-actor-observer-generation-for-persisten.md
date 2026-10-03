---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.817879+00:00
arxiv_id: 2610.02162
url: https://huggingface.co/papers/2610.02162
arxiv_url: https://arxiv.org/abs/2610.02162
date: 2026-10-02
---

# World Observer: Joint Actor-Observer Generation for Persistent World Modeling

How can a world model continuously observe regions beyond the actor's current view? Video world models simulate how an environment evolves from an agent's actions, yet remain actor-centric. Once an object leaves the actor's view, they lose direct evidence of its evolution, often failing to preserve its state and dynamics upon re-entry. To address this, we introduce World Observer, which decouples observing from acting by jointly generating a perspective actor for the agent-centric view with one or more panoramic observers that watch selected world regions. This allows objects that leave the actor's view to remain visually evolving in an observer, so their updated states are reflected when they re-enter. We ground the actor and observers by warping from a shared panoramic source for explicit geometric correspondence, and introduce an Observer Sink of high-resolution perspective references to restore fine appearance upon re-entry. Since the observers are decoupled from the actor, they can be placed freely across the scene, extended to multiple locations for broader coverage, and driven by control signals to steer out-of-view evolution. To evaluate out-of-view evolution, we further introduce world-space metrics and a benchmark spanning real and synthetic scenes. World Observer substantially improves out-of-view dynamics while remaining competitive in visual fidelity, camera control, and 3D adherence.
