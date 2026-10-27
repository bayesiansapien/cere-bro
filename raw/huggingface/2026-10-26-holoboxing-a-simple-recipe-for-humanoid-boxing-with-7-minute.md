---
source: farmer/huggingface
farmed: 2026-10-27T05:06:31.800188+00:00
arxiv_id: 2610.32909
url: https://huggingface.co/papers/2610.32909
arxiv_url: https://arxiv.org/abs/2610.32909
date: 2026-10-26
---

# HoloBoxing: A Simple Recipe for Humanoid Boxing with 7 Minutes of Single-GPU Training

HoloBoxing presents a simple recipe for learning humanoid boxing by building on a pretrained whole-body controller. The recipe separates reusable motor skills from task decisions: a compact planner requests future body-point targets, while the frozen controller handles joint-level execution. A learned decoder maps 32-dimensional actions to structured target windows, and measured-state imitation initializes the planner before reinforcement learning. Task learning then refines interaction behavior while reusing the decoder and controller, avoiding the need to relearn whole-body control. This combination keeps task optimization focused on a compact upper policy and supplies an initial behavior before reward-driven exploration. Starting from that available controller, the recipe accounts for about seven minutes of additional training, including reused representation fitting and a single-GPU task run. This excludes controller pretraining, data preparation, evaluation, and search. Simulated boxing experiments and component controls evaluate the resulting behavior and the roles of imitation initialization and the target representation.
