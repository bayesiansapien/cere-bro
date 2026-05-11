---
source: farmer/huggingface
farmed: 2026-05-11T00:00:00
arxiv_id: 2605.07510
url: https://huggingface.co/papers/2605.07510
arxiv_url: https://arxiv.org/abs/2605.07510
date: 2026-05-11
---

# InterLV-Search: Benchmarking Interleaved Multimodal Agentic Search

Existing benchmarks for multimodal agentic search evaluate multimodal search and visual browsing, but visual evidence is either confined to the input or treated as an answer endpoint rather than part of an interleaved search trajectory. We introduce InterLV-Search, a benchmark for Interleaved Language-Vision Agentic Search, in which textual and visual evidence is repeatedly used to condition later search. It contains 2,061 examples across three levels: active visual evidence seeking, controlled offline interleaved multimodal search, and open-web interleaved multimodal search. Beyond existing benchmarks, it also includes multimodal multi-branch samples that involve comparison between multiple entities during the evidence search. We construct Level 1 and Level 2 with automated pipelines and Level 3 with a machine-led, human-supervised open-web pipeline. We further provide InterLV-Agent for standardized tool use, trajectory logging, and evaluation. Experiments on proprietary and open-source multimodal agents show that current systems remain far from solving interleaved multimodal search, with the best model below 50% overall accuracy, highlighting challenges in visual evidence seeking, search control, and multimodal evidence integration.
