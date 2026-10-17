---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.22240
url: https://huggingface.co/papers/2610.22240
arxiv_url: https://arxiv.org/abs/2610.22240
date: 2026-10-16
---

# MMSearch-OPD: Easy Made Hard, Hard Made Learnable for Long-Horizon Multimodal Search Agents

Multimodal deep search is moving from short queries to long-horizon investigations that continually acquire evidence. However, training such agents remains constrained by limited challenging training questions and insufficient process feedback.
  We introduce MMSearch-OPD, combining controllable data refinement with joint reinforcement learning (RL) and on-policy distillation (OPD). Our Refine pipeline performs targeted expansion of reasoning chains derived from existing simple multimodal questions. Parameterized transformations control search depth and cross-modal evidence requirements while reusing existing image--question pairs. For training, answer rewards and lightweight behavior penalties guide RL, while the reward gap modulates token-level teacher guidance on imperfect student trajectories. An exponentially decaying distillation coefficient reduces teacher dependence as training proceeds.
  Experiments show gains from data refinement and further improvements from joint training after SFT, indicating stronger long-horizon multimodal deep search capabilities.
