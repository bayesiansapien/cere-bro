---
source: farmer/huggingface
farmed: 2026-04-16T00:00:00Z
arxiv_id: 2604.14084
url: https://huggingface.co/papers/2604.14084
arxiv_url: https://arxiv.org/abs/2604.14084
date: 2026-04-16
authors: Yuanda Xu, Hejian Sang, Zhengze Zhou
---

# TIP: Token Importance in On-Policy Distillation

**Authors:** Yuanda Xu, Hejian Sang, Zhengze Zhou
**arXiv:** [2604.14084](https://arxiv.org/abs/2604.14084)
**HuggingFace:** [hf.co/papers/2604.14084](https://huggingface.co/papers/2604.14084)

## Abstract

On-policy knowledge distillation (OPD) trains a student on its own rollouts under token-level supervision from a teacher. Not all token positions matter equally, but existing views of token importance are incomplete. We ask a direct question: which tokens carry the most useful learning signal in OPD? Our answer is that informative tokens come from two regions: positions with high student entropy, and positions with low student entropy plus high teacher-student divergence, where the student is overconfident and wrong.
