---
source: farmer/huggingface
farmed: 2026-06-07T04:51:04Z
arxiv_id: 2605.31058
url: https://huggingface.co/papers/2605.31058
arxiv_url: https://arxiv.org/abs/2605.31058
date: 2026-06-07
---

# Combinatorial Synthesis: Scaling Code RLVR via Atomic Decomposition and Recombination

Reinforcement Learning with Verifiable Rewards (RLVR) has recently emerged as the cornerstone for shaping the remarkable coding abilities of Large Language Models (LLMs). However, the scalability of RLVR is severely constrained by the scarcity of sufficiently challenging verifiable code tasks that target near the model's edge of competence. Prior studies often rely on heuristic seed expansions for data synthesis, which severely limits both novelty and difficulty. Consequently, the training value of such data fails to scale proportionally with the size of its synthesis. To this end, we propose Atomic Decomposition and Recombination (ADR), a novel framework that generates verifiable code tasks via decomposition into atomic elements and controlled recombination, thereby enabling the generation of genuinely novel and challenging verifiable code tasks. Experiments and analysis demonstrate that ADR achieves superior originality, difficulty, diversity, and test quality over existing baselines, and consistently delivers greater improvements in code ability across RLVR in diverse downstream domains, including algorithmic programming, tool usage, and data science. Our work sheds light on a new paradigm for novel code task synthesis and scalable RLVR training.
