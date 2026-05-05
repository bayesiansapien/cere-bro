---
source: farmer/huggingface
farmed: 2026-05-05T00:00:00
arxiv_id: 2604.27660
url: https://huggingface.co/papers/2604.27660
arxiv_url: https://arxiv.org/abs/2604.27660
date: 2026-05-05
---

# From Context to Skills: Can Language Models Learn from Context Skillfully?

Many real-world tasks require language models (LMs) to reason over complex contexts that exceed their parametric knowledge. This calls for context learning, where LMs directly learn relevant knowledge from the given context. An intuitive solution is inference-time skill augmentation: extracting the rules and procedures from context into natural-language skills. However, constructing such skills for context learning scenarios faces two challenges: the prohibitive cost of manual skill annotation for long, technically dense contexts, and the lack of external feedback for automated skill construction. In this paper, we propose Ctx2Skill, a self-evolving framework that autonomously discovers, refines, and selects context-specific skills without human supervision or external feedback. At its core, a multi-agent self-play loop has a Challenger that generates probing tasks and rubrics, a Reasoner that attempts to solve them guided by an evolving skill set, and a neutral Judge that provides binary feedback. Crucially, both the Challenger and the Reasoner evolve through accumulated skills: dedicated Proposer and Generator agents analyze failure cases and synthesize them into targeted skill updates for both sides, enabling automated skill discovery and refinement. To prevent adversarial collapse caused by increasingly extreme task generation and over-specialized skill accumulation, we further introduce a Cross-time Replay mechanism that identifies the skill set achieving the best balance across representative cases for the Reasoner side, ensuring robust and generalizable skill evolution. The resulting skills can be plugged into any language model to obtain better context learning capability. Evaluated on four context learning tasks from CL-bench, Ctx2Skill consistently improves solving rates across backbone models.
