---
source: farmer/huggingface
farmed: 2026-06-16T00:00:00Z
arxiv_id: 2606.15300
url: https://huggingface.co/papers/2606.15300
arxiv_url: https://arxiv.org/abs/2606.15300
date: 2026-06-16
---

# CODA-BENCH: Can Code Agents Handle Data-Intensive Tasks?

Advanced agents are increasingly demonstrating the potential to operate as autonomous engineers, creating a growing demand for evaluation benchmarks that capture the complexity of real-world development. Such environments typically involve both complex code and large-scale data (i.e., file system). However, existing benchmarks usually evaluate code-centric or data-centric capabilities in isolation, leaving a clear gap with real development scenarios. In this paper, we bridge this gap by introducing CODA-BENCH, the first benchmark to jointly evaluate code and data intelligence in a data-intensive environment. We construct a data-intensive Linux sandbox based on the Kaggle ecosystem (containing hundreds of datasets), where agents must actively explore complex file hierarchies to identify relevant resources and generate code for data-driven analytical tasks. CODA-BENCH comprises 1,009 tasks spanning 31 communities, with each task environment containing an average of 980 files, simulating realistic data scale and noise. Evaluations of advanced agents reveal that even top-performing systems struggle to effectively integrate data discovery with code execution, achieving a success rate of only 61.1%. These results highlight a substantial gap in current agentic capabilities for data-intensive tasks and point to promising directions for future research.
