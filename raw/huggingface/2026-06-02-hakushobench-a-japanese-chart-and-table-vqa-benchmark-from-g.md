---
source: farmer/huggingface
farmed: 2026-06-02T09:40:06Z
arxiv_id: 2606.01132
url: https://huggingface.co/papers/2606.01132
arxiv_url: https://arxiv.org/abs/2606.01132
date: 2026-06-02
---

# HakushoBench: A Japanese Chart and Table VQA Benchmark from Governmental White Papers

Understanding chart and table images is essential for applying vision-language models (VLMs) to real-world document understanding. While English benchmarks have advanced rapidly, non-English counterparts remain scarce, leaving it unclear whether this progress generalizes across languages. A key obstacle is the difficulty of collecting realistic and diverse non-English chart and table images at scale. To address this, we leverage governmental white papers as a scalable source for benchmark construction beyond English, as they contain naturally occurring charts and tables across diverse formats and domains and are freely accessible in many countries. As a first instantiation, we introduce HakushoBench, a challenging Japanese chart and table VQA benchmark built from 33 governmental white papers. HakushoBench contains 2,053 images spanning over 10 image types, with manually annotated QA pairs, designed to assess deep and holistic understanding of charts and tables, rather than local visual cues alone. Experiments across a broad range of VLMs demonstrate that HakushoBench remains challenging for open-weight models: the best open-weight model achieves only 58.6% accuracy, and a 34.9-point gap between open-weight and proprietary models highlights substantial room for improvement in complex chart and table understanding. We release our dataset and code.
