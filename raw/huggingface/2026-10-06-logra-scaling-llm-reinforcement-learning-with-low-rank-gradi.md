---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.06647
url: https://huggingface.co/papers/2610.06647
arxiv_url: https://arxiv.org/abs/2610.06647
date: 2026-10-06
---

# LoGRA: Scaling LLM Reinforcement Learning with Low-Rank Gradient Sketches

Reinforcement learning (RL) has greatly advanced the capabilities of large language models (LLMs), but its memory demands remain a barrier to broader adoption. We introduce LoGRA, an approach to RL post-training that reduces memory by retaining useful learning signals in low-rank gradient sketches. These compact representations support both model updates and efficient policy synchronization. To prevent overly large updates from disrupting learning, we complement gradient compression with predicted-KL step control, which estimates policy changes before applying each update and adjusts its magnitude accordingly. Across reasoning tasks, LoGRA reduces average training memory by up to 45.7\% without sacrificing performance. It also enables stable training of a 27B-parameter model for over 1,100 steps on a single eight-GPU node, where dense Adam runs out of memory, making previously memory-infeasible RL training practical. Code is available in the https://github.com/skzhang1/labs-molt/tree/logra/examples/scripts/logra{Molt library}.
