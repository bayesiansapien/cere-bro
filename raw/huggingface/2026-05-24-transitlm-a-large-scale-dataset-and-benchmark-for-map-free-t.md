---
source: farmer/huggingface
farmed: 2026-05-24T05:07:38.368292+00:00
arxiv_id: 2605.22355
url: https://huggingface.co/papers/2605.22355
arxiv_url: https://arxiv.org/abs/2605.22355
date: 2026-05-24
---

# TransitLM: A Large-Scale Dataset and Benchmark for Map-Free Transit Route Generation

Public transit route planning traditionally depends on structured map infrastructure and complex routing engines, and no existing dataset supports training models to bypass this dependency. We present TransitLM, a large-scale dataset of over 13 million transit route planning records from four Chinese cities covering 120,845 stations and 13,666 lines, released as a continual pre-training corpus and benchmark data for three evaluation tasks with complementary metrics. Experiments show that an LLM trained on TransitLM produces structurally valid routes at high accuracy and implicitly grounds arbitrary GPS coordinates to appropriate stations without any explicit mapping. These results demonstrate that transit route planning can be learned entirely from data, enabling end-to-end, map-free route generation directly from origin-destination information. The dataset and benchmark are available at https://huggingface.co/datasets/GD-ML/TransitLM, with evaluation code at https://github.com/HotTricker/TransitLM.
