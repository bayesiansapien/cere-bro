---
source: farmer/huggingface
farmed: 2026-10-28T10:37:11+05:30
arxiv_id: 2610.31566
url: https://huggingface.co/papers/2610.31566
arxiv_url: https://arxiv.org/abs/2610.31566
date: 2026-10-27
---

# CellTrack-Bench: Microscopic Cell Tracking Benchmark for Vision-Language Models

Large language models have shown outstanding performance on text-first tasks such as coding, math, and writing. Recent efforts are shifting models' training to include scientific problems that often live in highly specialized domains beyond text, such as protein structure and biological images. However, in these scenarios, their general-purpose accuracy compared with specialized algorithms remains in question. One such domain is cell tracking, which requires spatiotemporal awareness of cell dynamics. To evaluate this, we created a new benchmark, CellTrack-Bench, which assesses Vision-Language Models' (VLMs) cell-tracking-related performance against specialized trackers. The full benchmark draws from 15 standard cell-tracking datasets across four imaging modalities and comprises 1,537 problems corresponding to 9,041 cell-linking decisions. We selected a hard subset requiring greater reasoning effort by identifying failures shared across distinct algorithmic trackers. With this proposed dataset, we: (i) evaluated different environment harnesses for VLMs; (ii) benchmarked 9 frontier closed-source models and 13 open-weight models; and (iii) provided a detailed analysis of their failure modes. Code, the stored model outputs, and a pipeline that regenerates the benchmark from the source datasets are available at https://github.com/royerlab/celltrack-bench.
