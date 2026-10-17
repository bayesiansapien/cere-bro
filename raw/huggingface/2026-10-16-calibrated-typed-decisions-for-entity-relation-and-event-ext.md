---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.17113
url: https://huggingface.co/papers/2610.17113
arxiv_url: https://arxiv.org/abs/2610.17113
date: 2026-10-16
---

# Calibrated Typed Decisions for Entity, Relation, and Event Extraction

Information extraction models often perform well on the datasets they are trained on, but transferring to new domains and annotation guidelines remains challenging. Supporting user-specified types alone does not resolve this problem. We present CalOn, a unified 0.6B-parameter encoder for entity, relation, and event extraction across datasets and schemas. The model jointly encodes text and type definitions, then directly identifies entity spans, relations between spans, and event triggers and arguments. Its extraction decisions consider the requested types together, using their combined evidence to identify relevant candidates before assigning a type. This gives all three tasks a common probabilistic formulation while keeping every extracted mention anchored to the input text. We train on diverse sources, and supplement supervised learning with a reward that encourages correct extractions and penalises incorrect ones. Across 40 benchmarks, CalOn outperforms the evaluated baselines on most benchmarks. It leads all reported relation extraction benchmarks and achieves the highest average F1 for event triggers and arguments with gold triggers. The same model also performs strongly on aspect sentiment triplet extraction and pronoun resolution through its span-pair formulation. A correction for the probability bias introduced during training improves confidence estimates for entities, relations, and event arguments after calibration, with little change in F1.
