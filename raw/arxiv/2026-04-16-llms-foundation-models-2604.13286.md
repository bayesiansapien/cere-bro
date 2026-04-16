---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13286
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13286
published: 2026-04-16
authors: Mehak Dhaliwal, Shashwat Chaurasia, Yao Qin
---

# English is Not All You Need: Systematically Exploring the Role of Multilinguality in LLM Post-Training

**arXiv:** https://arxiv.org/abs/2604.13286
**Authors:** Mehak Dhaliwal, Shashwat Chaurasia, Yao Qin

## Abstract

arXiv:2604.13286v1 Announce Type: cross  Abstract: Despite the widespread multilingual deployment of large language models, post-training pipelines remain predominantly English-centric, contributing to performance disparities across languages. We present a systematic, controlled study of the interplay between training language coverage, model scale, and task domain, based on 220 supervised fine-tuning runs on parallel translated multilingual data mixtures spanning mathematical reasoning and API calling tasks, with models up to 8B parameters. We find that increasing language coverage during post-training is largely beneficial across tasks and model scales, with low-resource languages benefiting the most and high-resource languages plateauing rather than degrading. Even minimal multilinguality helps: incorporating a single non-English language improves both English performance and cross-lingual generalization, making English-only post-training largely suboptimal. Moreover, at sufficient language diversity, zero-shot cross-lingual transfer can match or exceed the effects of direct language inclusion in a low-diversity setting, although gains remain limited for typologically distant, low-resource languages.
