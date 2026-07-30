---
source: farmer/huggingface
farmed: 2026-07-30T12:41:02.128718+05:30
arxiv_id: 2607.26115
url: https://huggingface.co/papers/2607.26115
arxiv_url: https://arxiv.org/abs/2607.26115
date: 2026-07-30
---

# GPT-Red: Automated Red Teaming via Self-Play at Scale

We introduce GPT-Red, an automated red-teaming agent that is trained to discover novel prompt injection attacks against frontier LLMs. The goal of this model is to evaluate and improve the robustness of our production systems. To this end, we use it to adversarially train GPT-5.6, our most robust model to prompt injections to date. To create GPT-Red, we design a scalable self-play algorithm where the model is tasked with attacking a diverse population of simultaneously-trained defender agents. We train the model on realistic red-teaming environments using compute on the same scale as some of our largest RL post-training runs, making it the single-largest LLM safety training run ever documented. GPT-Red excels at red-teaming: it reliably breaks our past models up to GPT-5.5, it finds more successful attacks than human red-teamers, and it generalizes to held-out environments, defender models, and harnesses. In the future, we expect that as we improve the robustness of each new GPT model, it will in turn will provide better learning signal for even stronger red-teamer agents, thus unlocking a self-improvement flywheel.
