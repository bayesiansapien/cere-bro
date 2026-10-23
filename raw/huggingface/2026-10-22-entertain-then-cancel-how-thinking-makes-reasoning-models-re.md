---
source: farmer/huggingface
farmed: 2026-10-23T08:19:34.193279+00:00
arxiv_id: 2610.21204
url: https://huggingface.co/papers/2610.21204
arxiv_url: https://arxiv.org/abs/2610.21204
date: 2026-10-22
---

# Entertain, then Cancel: How Thinking Makes Reasoning Models Read Some and Or Literally

When a speaker says ``some students passed'', listeners infer that not all of them did. Reasoning models now let users decide how long a model thinks before it answers, but we do not know what extra thinking does to such everyday inferences. We study this directly: we keep a model's weights fixed, change only how much it thinks, and record which reading it chooses. A second tool cuts the model's own reasoning at successive points and asks for an answer, showing where the reading changes. Thinking makes models read logical words as logic: it cancels the implicatures of some (not all) and or (not both) in most tested open reasoning models and in GPT-5, while context-driven inferences such as indirect answers improve. The trace shows why: models first entertain the enriched reading and cancel it later. Answering from that early reading, an exploratory inference-time remedy, recovers these implicatures without losing literal accuracy. Evaluations of reasoning models should measure how they interpret, not only how accurate they are.
