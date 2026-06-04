---
source: farmer/huggingface
farmed: 2026-06-04T06:39:44Z
arxiv_id: 2606.03577
url: https://huggingface.co/papers/2606.03577
arxiv_url: https://arxiv.org/abs/2606.03577
date: 2026-06-04
---

# Eliciting Complex Spatial Reasoning in MLLMs through Wide-Baseline Matching

Wide-baseline matching (WBM) requires integrating geometric understanding, viewpoint changes, fine-grained perception, and occlusion reasoning, making it a challenging testbed for spatial reasoning in multimodal large language models (MLLMs) deployed in physical environments. However, current MLLMs lack systematic evaluation and training frameworks for these capabilities. We introduce ReasonMatch-Bench, a benchmark stratified by viewpoint displacement and matching granularity across indoor, outdoor, and object-centric scenarios, and show that current MLLMs still struggle with fine-grained wide-baseline correspondence: on a difficult 90-sample subset, human annotators achieve 84.0 F1, while the best existing baseline reaches 37.2. To bridge this gap, we build a scalable data-generation pipeline that automatically extracts wide-baseline view pairs from large-scale video-3D corpora, including RGB-D videos and SfM reconstructions, yielding diverse and verifiable supervision. We further propose Dynamic Correspondence Reinforcement Learning (DCRL), which combines Image-Level Viewpoint Progression and Point-Level Correspondence Curriculum to improve WBM training through verifiable rewards without explicit CoT supervision. Extensive experiments show that DCRL substantially improves ReasonMatch-Bench and transfers to related spatial benchmarks, while maintaining general visual understanding performance with modest gains on several benchmarks.
