---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.511271+00:00
arxiv_id: 2610.14158
url: https://huggingface.co/papers/2610.14158
arxiv_url: https://arxiv.org/abs/2610.14158
date: 2026-10-14
---

# Video-Arena: A Scalable Agentic Video Benchmark for Spatiotemporal Capability

Understanding and tracking a dynamic world are fundamental to visual intelligence. Existing video benchmarks provide limited insight into whether models can maintain a coherent understanding of evolving world state. Building such a benchmark from real-world videos is challenging because the underlying world state is partially observable, making annotations hard to obtain. To close this gap, we introduce Video-Arena, a benchmark that turns competitive games into scalable, verifiable tests of how well models understand evolving world states from videos. Specifically, inspired by how humans understand dynamic events, we evaluate spatiotemporal world state understanding and tracking through three task categories: perceiving critical events, interpreting state updates, and tracking the resulting states. Our pipeline can generate videos and aligned reference labels from game records at scale. To keep evaluation affordable and reproducible, we curate a golden set of 180 tasks across 9 games and run evaluations under two protocols: native visual understanding and tool-assisted agentic analysis. The best-performing systems achieve F1 scores of and under the two protocols, respectively. The result highlights that native models struggle to perceive events reliably, while tool-assisted systems improve event recovery but still struggle to interpret state updates and track the resulting states consistently over time. Our project page is in https://videoarena-bench.github.io
