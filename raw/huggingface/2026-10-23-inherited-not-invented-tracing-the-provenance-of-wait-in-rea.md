---
source: farmer/huggingface
farmed: 2026-10-24T12:49:20.885488+00:00
arxiv_id: 2610.30882
url: https://huggingface.co/papers/2610.30882
arxiv_url: https://arxiv.org/abs/2610.30882
date: 2026-10-23
---

# Inherited, Not Invented: Tracing the Provenance of Wait in Reasoning Models

Reinforcement learning (RL) is credited with teaching reasoning models to write {wait} before reconsidering a step, yet large RL accuracy gains do not require the word. This view can confuse what RL discovers with what a model inherits from its training data. We trace the word through open models' training histories, reading it with label-free indices of frequency, position, form and usage and an injected-error test, all computed from sampled outputs. We find that zero-RL almost never coins the marker: on bases that lack the word, RL raises MATH-500 accuracy substantially while {wait} stays near absent. It arrives with training data: mid-training in OLMo-3, and fine-tuning on reasoning traces installs it in most models whose base lacks it. Where the base already uses it, both released RL-Zero recipes (OLMo-3, MiMo) multiply it, whereas KL-free GRPO from the same base does not; OLMo-3's recipe wears down its form and makes it a more sensitive but more liberal alarm; RL after supervised fine-tuning barely changes it, and our GRPO recipe erases a marker seeded by fine-tuning. Finally, we show that marker frequency alone does not indicate RL-induced reasoning and caution against LLM-as-a-judge revision metrics, as automated judges can reverse human-labelled trends.
