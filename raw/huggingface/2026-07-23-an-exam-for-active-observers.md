---
source: farmer/huggingface
farmed: 2026-07-24T23:47:01.610703+05:30
arxiv_id: 2607.16165
url: https://huggingface.co/papers/2607.16165
arxiv_url: https://arxiv.org/abs/2607.16165
date: 2026-07-23
---

# An Exam for Active Observers

Human vision is a closed loop: gaze is continuously redirected by intermediate hypotheses rather than a single snapshot. Decades of psychophysics and cognitive science have argued that this active observation is essential for a wide range of tasks. Whether today's multimodal large language models (MLLMs) exercise active observation is an empirical question that current vision-language benchmarks do not answer. We introduce ActiveVision, a benchmark that makes active observation measurable for MLLMs, comprising 17 tasks across 3 categories. Tasks are designed to force repeated visual perception rather than a single static description. Frontier MLLMs collapse on ActiveVision: the highest-scoring model we evaluate, GPT-5.5 at the highest exposed reasoning-effort tier, solves only 10.6% of items and scores zero on 11 of the 17 tasks, and even Claude Fable 5, despite topping most reasoning and coding leaderboards, solves just 3.5%, far behind three human participants who average 96.1%. Furthermore, much of the gap persists even when models write and run their own vision code: such code is unreliable on realistic imagery, and catching its failures itself requires the active perception the models lack. Together, these results indicate that current MLLMs lack robust active visual observation, motivating architectures and training objectives that close the perception-reasoning loop.
