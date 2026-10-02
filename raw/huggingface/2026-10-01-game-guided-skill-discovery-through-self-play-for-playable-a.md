---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.351537+05:30
arxiv_id: 2609.40137
url: https://huggingface.co/papers/2609.40137
arxiv_url: https://arxiv.org/abs/2609.40137
date: 2026-10-01
---

# Game-Guided Skill Discovery through Self-Play for Playable Agent Control

We present Game-Guided Skill Discovery (GGSD), a framework that uses self-play in games to discover motor skills that are directly playable by humans. Playable skills provide a compact abstraction for controlling embodied agents through a small set of learned behaviors rather than low-level actions. To be effective, these skills should be semantically distinct, interpretable, and expressive; properties that existing unsupervised skill-discovery methods often fail to achieve simultaneously. GGSD achieves these desiderata by grounding skill discovery in competitive gameplay. A hierarchical agent competes against its past selves, with a high-level policy selecting from a small discrete skill set and a skill-conditioned low-level policy learning the corresponding behaviors. After training, a human can replace the high-level policy and directly control the agent through the same discrete skills. Despite the small number of high-level actions, skill transitions give rise to emergent combo behaviors, expanding expressivity beyond individual primitives. Across Ant, Franka-arm, and Unitree G1 environments, we show that GGSD produces human-playable skills that humans can compose to solve unseen tasks, such as Maze and CubePush, without additional training. An interactive demo is available at https://ggsd-demo.github.io.
