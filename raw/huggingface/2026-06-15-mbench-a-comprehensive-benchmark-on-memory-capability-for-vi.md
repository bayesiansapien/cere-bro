---
source: farmer/huggingface
farmed: 2026-06-15T06:21:28Z
arxiv_id: 2606.00793
url: https://huggingface.co/papers/2606.00793
arxiv_url: https://arxiv.org/abs/2606.00793
date: 2026-06-15
---

# MBench: A Comprehensive Benchmark on Memory Capability for Video World Models

Recent advancements in video-based world models have demonstrated an unprecedented ability to synthesize high-fidelity visual sequences. However, a fundamental gap persists between visually plausible video generation and the functional requirements of a world model, particularly in maintaining a stable and reasonable internal state over extended temporal horizons. While existing benchmarks primarily emphasize visual quality, motion coherence, and text-video alignment, they largely overlook memory, the core capability of a world model to preserve consistency across long-term horizons and complex interactions. To address this gap, we present MBench, a comprehensive benchmark dedicated to quantifying and evaluating the memory capability of video world models. We systematically decompose the memory capability of video world models into three hierarchical and complementary core dimensions: entity consistency, environment consistency, and causal consistency, which are further refined into 12 quantifiable sub-dimensions for comprehensive characterization of long-term memory. Our benchmark is built upon rigorously curated real-captured long videos, and evaluated by rule-based quantitative matrices and VLM to enable objective and comprehensive consistency assessment. Extensive evaluations of mainstream state-of-the-art video world models reveal critical systemic limitations of existing methods in long-term state retention, providing a standardized benchmark and clear research direction to advance the field.
