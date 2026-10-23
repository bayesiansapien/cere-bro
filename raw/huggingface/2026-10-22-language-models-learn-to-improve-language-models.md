---
source: farmer/huggingface
farmed: 2026-10-23T08:19:34.196264+00:00
arxiv_id: 2610.23344
url: https://huggingface.co/papers/2610.23344
arxiv_url: https://arxiv.org/abs/2610.23344
date: 2026-10-22
---

# Language Models Learn to Improve Language Models

Large language models (LLMs) are increasingly used to automate AI research, including language-model (LM) development, offering a potential path toward recursive self-improvement. However, turning experimental feedback into a learned ability to propose effective improvements across models faces two challenges. First, training such an ability with real feedback is expensive: reinforcement learning (RL) requires evaluating tens of thousands of proposals, each potentially requiring a full model-training run. Even at ten GPU-hours per run, reward collection alone would consume hundreds of thousands of GPU-hours, motivating a cheaper surrogate. Second, surrogate feedback can become unreliable as policy optimization favors overestimated proposals when the proposal distribution shifts. To address these challenges, we propose LM2LM, which trains LLMs with RL to generate effective LM improvement proposals. To provide scalable feedback, we use a research world model (RWM), a frozen LLM that predicts proposal gains from real experimental records provided in context, as the reward model for RL. To maintain feedback reliability, we periodically execute current-policy proposals ranked highly by the RWM and add their measured outcomes to its context. Across eight autoregressive and diffusion LM development environments, real-execution evaluations on held-out tasks show that LM2LM enables Qwen3.8-27B to outperform GPT-6-sol, even when GPT-6-sol is given 300 real experimental records in context, while requiring 33% lower data-generation cost. LM2LM also generalizes to a model family unseen during training.
