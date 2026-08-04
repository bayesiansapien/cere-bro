---
source: farmer/huggingface
farmed: 2026-08-04T09:04:58.435121+05:30
arxiv_id: 2608.00440
url: https://huggingface.co/papers/2608.00440
arxiv_url: https://arxiv.org/abs/2608.00440
date: 2026-08-04
---

# Poplar: A Scalable Pipeline for Human-Centric Image Dataset Synthesis

Recent image generators can synthesize convincing human-centric images, yet producing a useful collection remains different from producing a single successful image. A human-centric dataset must cover varied people and contexts, avoid implausible attribute combinations, preserve an everyday photographic character, and expose quality-control decisions at scale. We present Poplar, a reproducible Specify--Render--Inspect pipeline for human-centric image dataset synthesis. Specify samples structured attributes under commonsense constraints and verbalizes them as photography-oriented prompts. Render uses a realism-adapted image generator across composition-aware aspect ratios and retries obvious technical failures. Inspect applies a single structured vision--language review to each candidate, preserving the original prompt while rejecting intrinsic image defects or material prompt mismatches. Using Poplar, we construct Poplar-9K: 9,401 curated human-centric image--text pairs retained from 11,765 reviewed candidates (79.9\% acceptance). We release the dataset together with the pipeline, configurations, immutable generation prompts, and auditable inspection records as a compact resource for building customizable human-centric collections.
