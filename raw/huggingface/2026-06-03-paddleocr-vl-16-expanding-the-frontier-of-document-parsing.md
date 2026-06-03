---
source: farmer/huggingface
farmed: 2026-06-03T00:00:00Z
arxiv_id: 2606.03264
url: https://huggingface.co/papers/2606.03264
arxiv_url: https://arxiv.org/abs/2606.03264
date: 2026-06-03
---

# PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training

We introduce PaddleOCR-VL-1.6, an upgraded compact document parsing model built upon PaddleOCR-VL-1.5. Although PaddleOCR-VL-1.5 establishes a strong 0.9B baseline, its remaining errors concentrate in under-optimized regions where model behavior is unstable, data coverage is sparse, or supervision is unreliable. Rather than expanding the training corpus indiscriminately, PaddleOCR-VL-1.6 introduces a region-aware data optimization framework that identifies weak regions from the previous model, applies targeted enhancement to these regions, and improves the reliability of supervision signals. It further adopts a progressive post-training recipe based on curated data selection and reinforcement learning, pushing model performance to a higher level through staged optimization. PaddleOCR-VL-1.6 achieves a new state-of-the-art score of 96.33% on OmniDocBench v1.6, demonstrates strong competitiveness against top-tier VLMs, and provides a practical post-training recipe for the PaddleOCR-VL series.
