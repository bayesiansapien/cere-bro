---
source: farmer/huggingface
farmed: 2026-07-28T09:26:01.339781
arxiv_id: 2607.24241
url: https://huggingface.co/papers/2607.24241
arxiv_url: https://arxiv.org/abs/2607.24241
date: 2026-07-28
---

# FilmBench: A Film-Grade Benchmark for Cinematic Video Generation

Progress in video generation keeps narrowing the visual gap between AI-generated and professionally produced footage, yet most benchmarks still draw prompts from web sources or LLM templates and score them with untrained, generic multimodal models. More fundamentally, their evaluation taxonomies remain rudimentary (overall visual quality, coarse text alignment and temporal smoothness) rather than the professional Cinematic Language criteria by which films are actually made and judged, so they assess basic video plausibility rather than film-grade craft. We introduce FilmBench, a text-to-video (T2V) and reference-to-video (R2V) benchmark grounded in the professional Cinematic Language of the film-academy tradition and co-developed with directors and faculty from the Beijing Film Academy and the Hujing Digital Media & Entertainment Group film studio. It rests on three choices. First, prompts are reverse-engineered from clips of award-winning films spanning 20 cinematic genres and chosen by professional directors, so every prompt is anchored to a verified live-action reference; the prompts follow real shot lists, and most script multiple shots (1,056 of the 1,169 prompts are multi-shot), unlike prior single-clip benchmarks. Second, evaluation follows a three-level Cinematic taxonomy of 3 axes, 12 components and 35 (T2V) +3 (R2V-only) sub-metrics. Third, we develop an in-house expert-grade automatic evaluation agent and open-source its core suite of Cinematic Language operators (FilmOps). Benchmarking leading video generation models (9 for T2V, 7 for R2V), the evaluator reproduces the human model ranking at model-level Spearman rho = 0.95 (T2V) and 0.96 (R2V). Scores fall well below prior web-style benchmarks, with two consistent gaps in dynamic aesthetics and a marked single- to multi-shot performance drop that widens for weaker models.
