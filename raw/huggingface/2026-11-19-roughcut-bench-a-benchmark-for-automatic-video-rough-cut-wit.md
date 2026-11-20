---
source: farmer/huggingface
farmed: 2026-11-20T05:04:58.143109+00:00
arxiv_id: 2611.24098
url: https://huggingface.co/papers/2611.24098
arxiv_url: https://arxiv.org/abs/2611.24098
date: 2026-11-19
---

# RoughCut-Bench: A Benchmark for Automatic Video Rough-Cut with Large Vision-Language Models

Video rough-cut is a core stage in media production workflows, organizing raw media materials into an initial video cut. Despite recent advances in large vision-language models (LVLMs) for video-related tasks, automatic rough-cut remains underexplored, without a comprehensive benchmark for evaluation or mature workflows for producing executable cut plans. To address the evaluation gap, we introduce RoughCut-Bench, which covers two practical settings: (1) a visually driven setting over video cases, covering highlight detection and selection, source-video ordering, and adherence to user requirements when provided; and (2) a speech-driven setting over automatic speech recognition (ASR) transcripts, covering filler removal, expression deduplication, and low-value content trimming. Across these settings, the benchmark contains 101 visually driven cases, including 831 raw videos with 1,476 highlight annotations. It also includes 84 speech-driven cases, each consisting of an ASR transcript with annotated cleanup spans. The evaluation compares cut plans with these annotations in both settings and additionally uses a human-aligned agentic evaluator to assess rendered-cut quality in the visual setting. To apply LVLMs to automatic rough-cut, we further propose agentic workflows that guide them to produce structured cut plans from input materials. Experiments show that current LVLMs remain limited in producing expert-aligned cut plans. Our benchmark, code, and prompts are released at https://whalesong-zrs.github.io/RoughCut-Bench-Project-Page.
