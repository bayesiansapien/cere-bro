---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2609.36691
url: https://huggingface.co/papers/2609.36691
arxiv_url: https://arxiv.org/abs/2609.36691
date: 2026-10-06
---

# Video2Skill: From Streaming Experience to Reusable Embodied Skills

Manipulation behaviors vary widely across objects and scenes, but they share a small set of reusable skills, and planning with these skills helps embodied agents generalize to new tasks. Yet an agent can only plan with skills it knows. Recovering skills from observed experience, the inverse of planning, builds this knowledge over time and yields skill data for training future agents. Vision-Language Models (VLMs) describe individual manipulation events well, but can they organize a stream of events into reusable skills? We formulate this problem as Streaming Embodied Skill Discovery (SESD): a model watches videos in sequence and maintains a persistent skill library that shapes its later decisions. To systematically measure this ability, we introduce Video2Skill, a benchmark that covers robot tabletop manipulation and human kitchen activity and tests three core capabilities: (i) locating manipulation events in time, (ii) grouping events of the same transformation, and (iii) deciding when to reuse an existing skill or create a new one. Across 19 open-source VLMs, many models group events at near-chance level, and scale does not consistently help. Their errors depend on how perception and library updates are coupled: joint models merge distinct transformations into one skill, while models that update the library from text descriptions duplicate recurring ones. Supervised fine-tuning, including our counterfactual library-state rebalancing (CLaRe), improves grouping but exposes a deeper bottleneck: trained models consolidate familiar skills yet rarely expand the library. Their libraries stall below half the reference size, and transformations unseen in training are located in time but almost never given a new skill. Recognizing when existing skills are insufficient thus emerges as the central challenge.
