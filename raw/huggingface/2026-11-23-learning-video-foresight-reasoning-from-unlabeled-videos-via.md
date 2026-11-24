---
source: farmer/huggingface
farmed: 2026-11-24T05:05:48.246771+00:00
arxiv_id: 2611.26954
url: https://huggingface.co/papers/2611.26954
arxiv_url: https://arxiv.org/abs/2611.26954
date: 2026-11-23
---

# Learning Video Foresight Reasoning from Unlabeled Videos via On-Policy Self-Distillation

Video foresight reasoning requires vision-language models to anticipate future events or next actions from currently observed videos. Existing methods fit future captions, rationales, or full visual states, but face two limitations. First, they rely on annotations or external large models for supervision, limiting scalability. We address this with an on-policy self-distillation framework that turns past-future video pairs into a natural self-supervised signal without extra annotations or LLM supervision. Second, they treat the whole future clip as equally valuable, although most of it is irrelevant context information. We address this by defining a foresight score, from which we obtain a contrastive privilege advantage that drives the model to learn the most valuable future information. Since the score is intractable, we optimize a tractable lower-bound surrogate that interpolates this advantage, computed between the true and a random reference future, with a teacher-student distillation advantage; together, they amplify decision-relevant content information and suppress irrelevant context information. We call the resulting framework Future-OPSD. On open-ended prediction and closed-ended planning, Future-OPSD improves base models by up to 14.2 and 15.9 points without compromising general video understanding. Code will be available at https://jingchensun.github.io/future-opsd/
