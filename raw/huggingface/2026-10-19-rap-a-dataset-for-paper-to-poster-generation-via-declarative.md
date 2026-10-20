---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.23230
url: https://huggingface.co/papers/2610.23230
arxiv_url: https://arxiv.org/abs/2610.23230
date: 2026-10-19
---

# RAP: A Dataset for Paper-to-Poster Generation via Declarative Markup from Human-Crafted Exemplars

Making a conference poster is visual coding in miniature: an entire paper must be compressed onto a single page, which exercises summarization, visual design, and code implementation at once, using nothing beyond the paper itself. Yet benchmarks for this task in the context of visual coding remain scarce: existing resources are small and annotated only with layout boxes, so evaluation must fall back on VLM-as-judge or human checklists rather than objective render-and-compare, and the generation methods they support design layouts from scratch, leaving human-crafted posters unusable as either a retrievable design library or as verified supervision. We introduce RAP (Reconstruct A Poster), a dataset and benchmark for paper-to-poster generation as a visual coding task. RAP contains 25K+ verified paper-poster pairs from various machine learning conferences held between 2022 and 2026, annotated with a three-level content taxonomy, plus a held-out benchmark of 150 test papers each paired with its human poster. A fully automated derendering pipeline turns each poster into styled HTML/CSS of typed, refillable slots, so every sample is a paper-poster-markup triplet verifiable by rendering against the source poster. The corpus serves both inference and training: PosterRAG, a training-free multi-agent pipeline, retrieves an exemplar and refills its slots without touching layout or styling, while an SFT+RL recipe trains a dedicated model from the same triplets. An online demo is available at https://reconstruct-a-poster.github.io/.
