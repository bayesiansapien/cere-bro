---
source: farmer/huggingface
farmed: 2026-06-04T06:39:44Z
arxiv_id: 2606.04036
url: https://huggingface.co/papers/2606.04036
arxiv_url: https://arxiv.org/abs/2606.04036
date: 2026-06-04
---

# Self-Distilled Policy Gradient

On-policy self-distillation, where a language model conditions on privileged context to supervise its own generations, is a promising source of dense supervision for sparse-reward reinforcement learning. Actually, it can be instantiated as an auxiliary full-vocabulary student-to-teacher reverse Kullback-Leibler divergence loss. We therefore propose SDPG, a self-distilled policy-gradient framework that combines group-relative verifier advantages with normalized standard deviation, exact full-vocabulary on-policy self-distillation, as well as reference-policy KL regularization. Empirically, SDPG improves stability and performance over RLVR and self-distillation baselines. The code is available at https://github.com/lauyikfung/SDPG.
