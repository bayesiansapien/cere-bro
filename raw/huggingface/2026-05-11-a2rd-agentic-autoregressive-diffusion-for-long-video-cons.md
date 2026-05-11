---
source: farmer/huggingface
farmed: 2026-05-11T00:00:00
arxiv_id: 2605.06924
url: https://huggingface.co/papers/2605.06924
arxiv_url: https://arxiv.org/abs/2605.06924
date: 2026-05-11
---

# A^2RD: Agentic Autoregressive Diffusion for Long Video Consistency

Synthesizing consistent and coherent long video remains a fundamental challenge. Existing methods suffer from semantic drift and narrative collapse over long horizons. We present A2RD, an Agentic Auto-Regressive Diffusion architecture that decouples creative synthesis from consistency enforcement. A2RD formulates long video synthesis as a closed-loop process that synthesizes and self-improves video segment-by-segment through a Retrieve-Synthesize-Refine-Update cycle. It comprises three core components: (i) Multimodal Video Memory that tracks video progression across modalities; (ii) Adaptive Segment Generation that switches among generation modes for natural progression and visual consistency; and (iii) Hierarchical Test-Time Self-Improvement that self-improves each segment at frame and video levels to prevent error propagation. We further introduce LVbench-C, a challenging benchmark with non-linear entity and environment transitions to stress-test long-horizon consistency. Across public and LVbench-C benchmarks spanning one- to ten-minute videos, A2RD outperforms state-of-the-art baselines by up to 30% in consistency and 20% in narrative coherence. Human evaluations corroborate these gains while also highlighting notable improvements in motion and transition smoothness.
