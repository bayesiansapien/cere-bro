---
source: farmer/huggingface
farmed: 2026-11-24T05:05:48.250610+00:00
arxiv_id: 2611.26809
url: https://huggingface.co/papers/2611.26809
arxiv_url: https://arxiv.org/abs/2611.26809
date: 2026-11-23
---

# Search From the Start: Search-Native Pretraining for Language Models

Modern language models (LMs) are increasingly deployed with access to search tools at inference. Yet pretraining remains predominantly focused on predicting static text, with search capabilities typically introduced during post-training. We propose Search-Native Pretraining as a practical route to teach search capability during pretraining from ordinary text corpora. Specifically, we augment pretraining corpus at scale with web-search queries and retrieve web response using a local index. Training on this augmented corpus teaches models to generate search calls and incorporate retrieved evidence during language modeling. Across Wikipedia and DCLM-Edu corpora and 360M to 3.3B parameter scales, search-pretrained models ("QueryLM") show improved performance on knowledge-intensive tasks and higher steerability toward the retrieved evidence. Crucially, their advantage persists after supervised fine-tuning of both search-pretrained and conventionally pretrained models, indicating that the tested post-training procedures do not fully recover the capabilities developed during pretraining. Throughout our experiments, we find that a 1.4B QueryLM consistently beats or matches the performance of a FLOP-matched 3.3B baseline model across all knowledge intensive tasks. These results establish search-pretraining as a practical way to develop foundational search capabilities during pretraining. We release the training artifacts, including model checkpoints and data.
