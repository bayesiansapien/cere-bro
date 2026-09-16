---
source: farmer/huggingface
farmed: 2026-09-16T13:11:10.933414
arxiv_id: 2609.16679
url: https://huggingface.co/papers/2609.16679
arxiv_url: https://arxiv.org/abs/2609.16679
date: 2026-09-16
---

# AI for Games in the Foundation Model Era

Foundation models, alongside advances in learned game-world models, are reshaping AI across the game lifecycle. Beyond playing games, recent systems model players and game dynamics, support design and development, adapt player-facing experiences at runtime, and evaluate resulting artifacts. Yet these directions have evolved largely separately, obscuring which capabilities transfer across settings and which remain tied to particular games, engines, interfaces, or player populations. We organize the literature into six roles according to the immediate use of AI output: playing and acting; modeling players and games; designing games; building and maintaining games; generating and adapting at runtime; and testing and evaluating games. For each role, we examine what structure is supplied by the game or workflow, what AI learns or produces, which capabilities and artifacts transfer across settings and roles, and what evidence supports the claims. We identify cross-role connections: trajectories train world models, learned environments provide experience for agents, design specifications drive executable implementations, and play or testing feedback guides revision. However, control schemes, rules, engine interfaces, state representations, and player contexts often remain setting-specific, so downstream claims require validation in the target setting. Evaluation is most standardized for bounded game playing and selected learned environments, while persistent state in learned worlds, repeated software revision, validated player modeling, sustained runtime adaptation, and representative automated testing remain less established. The central challenge is to reuse or transfer outputs and capabilities across roles while re-establishing evidence for effectiveness in the game-specific contexts where they are used.
