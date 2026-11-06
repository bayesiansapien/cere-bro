---
source: farmer/huggingface
farmed: 2026-11-06T05:50:41.305254+00:00
arxiv_id: 2610.40516
url: https://huggingface.co/papers/2610.40516
arxiv_url: https://arxiv.org/abs/2610.40516
date: 2026-11-05
---

# How I Aligned Your Model: Scaling Up Multilingual Safety Training with Templates

Safety alignment for Large Language Models is heavily focused on English with limited multilingual representation, particularly damaging low-resource language performance. Related open training datasets are often limited in size or do not follow region-localized harmful topics to broaden the scope of alignment beyond cultures. We propose a scalable template-based augmentation pipeline to produce massive multilingual refusal and benign corpora, extracting safe templates from harmful prompts, translating them and then filling in the slots with culturally authentic entities, both harmful and benign. As a result, we release MSafeTemp, a validated corpus spanning 60 languages useful for multilingual safety alignment and evaluation. Using the dataset, we show that English-only evaluation misjudges multilingual safety: for several models, attacks that fail in English succeed once translated, while culturally localized variants expose further failures that translation alone misses. We also confirm that augmenting safety training data through templates allows for higher diversity and quality of alignment, resulting in improved safety performance beyond English. MSafeTemp and the respective pipeline are aimed at facilitating research and development of safer and more responsible models for less-represented cultures.
