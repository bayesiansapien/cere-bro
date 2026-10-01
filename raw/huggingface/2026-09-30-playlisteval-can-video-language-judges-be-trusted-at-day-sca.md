---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.34314
url: https://huggingface.co/papers/2609.34314
arxiv_url: https://arxiv.org/abs/2609.34314
date: 2026-09-30
---

# PlaylistEval: Can Video-Language Judges Be Trusted at Day Scale and Beyond?

Video-language models are increasingly used as judges of video understanding, both for evaluating model outputs and for training reward models. Whether their judgments remain reliable when the evidence is buried in day-long videos has yet to be established. Existing benchmarks cannot answer this. Their videos are typically only a few minutes long, many answer pairs can be separated from the transcript alone, and collecting human judgments does not scale to ultra-long videos. We introduce PlaylistEval, an agentic framework that builds video-language judge benchmarks over 100-hour playlist collection without human annotation. It automatically generates questions with paired answers whose differences are controlled by causal degradation, so that every pair demands retrieval across the collection. The resulting benchmark contains 630 pairs across seven domains spanning both static and dynamic knowledge, and on a stratified subset of 152 pairs it agrees with human judgments 93.0% of the time (IAA 0.781). Evaluating 17 omnimodal and multimodal models from eight families reveals that frontier judges reach only 75.4% pairwise accuracy, while open-source judge models perform far behind. We further show that both retrieval and final judgment depend on using multiple modalities, and that judge accuracy degrades as the playlist set grows. We release our pipeline, benchmark, and evaluation code at https://playlisteval.github.io.
