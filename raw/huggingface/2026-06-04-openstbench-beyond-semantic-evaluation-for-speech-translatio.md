---
source: farmer/huggingface
farmed: 2026-06-04T06:39:44Z
arxiv_id: 2605.30792
url: https://huggingface.co/papers/2605.30792
arxiv_url: https://arxiv.org/abs/2605.30792
date: 2026-06-04
---

# OpenSTBench: Beyond Semantic Evaluation for Speech Translation

Speech translation systems increasingly span speech-to-text translation (S2TT), speech-to-speech translation (S2ST), offline translation, and streaming generation, producing outputs that differ in modality, speech realization, and timing behavior. Existing evaluation practices assess important aspects such as translation quality, speech quality, and temporal quality, but these aspects are often evaluated under separate protocols, making it difficult to compare heterogeneous systems comprehensively. To address this gap, we present OpenSTBench, a unified multidimensional evaluation framework that organizes heterogeneous speech translation outputs into a shared evaluation format. OpenSTBench supports both S2TT and S2ST systems in offline and streaming settings, and jointly evaluates translation quality, speech quality, speaker preservation, emotion and paralinguistic fidelity, temporal consistency, and latency. Through experiments on representative speech translation systems, we show that systems with strong translation quality can still differ substantially in speech quality, as well as in temporal quality. OpenSTBench provides a reproducible protocol for analyzing these cross-dimensional differences and supporting application-oriented comparison of speech translation systems. The code and datasets are available at https://github.com/sjtuayj/OpenSTBench.
