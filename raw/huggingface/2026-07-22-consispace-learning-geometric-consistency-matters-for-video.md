---
source: farmer/huggingface
farmed: 2026-07-22T05:46:30Z
arxiv_id: 2607.17599
url: https://huggingface.co/papers/2607.17599
arxiv_url: https://arxiv.org/abs/2607.17599
date: 2026-07-22
---

# ConsiSpace: Learning Geometric Consistency Matters for Video Spatial Reasoning

Video spatial reasoning is essential for navigation-oriented perception and long-video question answering, where models must infer spatial relations across long horizons under changing viewpoints. However, existing multimodal large language models (MLLMs) remain largely semantic-centric, and often fail to reliably aggregate consistent spatial evidence from redundant video observations, leading to inefficient or unstable reasoning. To address these issues, we propose ConsiSpace, a geometry-consistency-aware framework for geometry-sensitive video spatial reasoning that turns spatial consistency into both an evidence organization principle and an explicit post-SFT learning signal. We build a geometry-consistent memory (GCM) including implicit evidence tokens and explicit geometric cues, and leverage efficient organization strategies to compactly preserve task-related spatial evidence. Furthermore, we utilize unified consistency self-supervised reinforcement learning (UC-SSRL) after supervised fine-tuning to improve cross-view stability, with answer-, metric-, and topology-consistency rewards. Extensive experiments on three spatial-reasoning benchmarks, VSI-Bench, OSI-Bench, and MMSI-Video-Bench, show consistent gains, improving the average score by 12.6 points over the strongest baselines.
