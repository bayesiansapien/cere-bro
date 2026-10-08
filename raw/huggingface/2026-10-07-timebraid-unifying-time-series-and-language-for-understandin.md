---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2609.29792
url: https://huggingface.co/papers/2609.29792
arxiv_url: https://arxiv.org/abs/2609.29792
date: 2026-10-07
---

# TimeBraid: Unifying Time Series and Language for Understanding and Forecasting

We present TimeBraid, a series of unified time-series and language models that align pretrained language models and pretrained time-series foundation models through interleaved global residual attention layers. Each model inherits knowledge, instruction following, and reasoning from one side, continuous-signal perception and zero-shot forecasting from the other, and fuses the two in a shared representation space where both modalities are understood and generated. We study the design choices that make such unified modeling work: where to align the two representation spaces, how to ground language in temporal structure, how to balance understanding with generation, and how to keep joint optimization stable. The resulting recipe combines a unified prompting scheme for diverse time-series and text tasks, stabilized joint training, and supervision from 2.2M curated series--text pairs and 4.9M instruction-tuning samples. Across benchmarks spanning time-series perception, understanding, reasoning, and both context-aided and unimodal forecasting, TimeBraid remains competitive with far larger general-purpose models and task-specific counterparts.
