---
source: farmer/huggingface
farmed: 2026-11-14T05:10:36.530846+00:00
arxiv_id: 2611.16009
url: https://huggingface.co/papers/2611.16009
arxiv_url: https://arxiv.org/abs/2611.16009
date: 2026-11-13
---

# JustRUA: A Controlled Study of GPT-6 Robot-Use Agents

GPT-6 Astra can drive a robot arm directly through a fixed harness, and scores of such robot-use agents on RoboDojo have risen quickly since. Reported systems differ in harness and test subset and often change several designs at once, so it is hard to tell which choices produce the gains. We take these designs apart and test them in one framework, along the harness around the model, the action interface, the reuse of experience and the scene geometry given to the model. A lean harness that keeps the full episode history and stops each motion early goes a long way. Reusing experience changes how the model acts but is not a free lunch, and scene geometry helps most, even when depth is predicted from RGB alone. JustRUA starts from the official L3 harness and keeps only what matters most. Even with no learned policy, self-improvement loop or task-specific tuning, this simple harness raises the score on the RoboDojo simulation benchmark substantially, from 29.7 to 50.3.
