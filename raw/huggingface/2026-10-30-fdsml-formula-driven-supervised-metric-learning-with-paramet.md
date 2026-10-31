---
source: farmer/huggingface
farmed: 2026-10-31T08:06:35.163737+00:00
arxiv_id: 2610.39423
url: https://huggingface.co/papers/2610.39423
arxiv_url: https://arxiv.org/abs/2610.39423
date: 2026-10-30
---

# FDSML: Formula-Driven Supervised Metric Learning with Parameter-Aware Triplet Loss

Formula-Driven Supervised Learning (FDSL) enables vision pre-training without real images, but existing methods cast pre-training as classification on discretized labels, discarding continuity in the generative process. We propose Formula-Driven Supervised Metric Learning (FDSML), which derives relational supervision from image-generation parameters beyond discrete class labels. FDSML combines FineFractalDB, our refined fractal dataset with higher intra-class variation and more stable structures, with a Parameter-Aware Triplet (PA-Triplet) Loss that assigns positives and negatives according to distances in the underlying Iterated Function System parameter space. This objective trains embeddings to respect parameter-derived relative similarity orderings. Experiments show that FDSML improves transferability to image retrieval while remaining competitive on downstream classification and improving robustness under several corruption settings. On ResNet-50, Recall@1 improves from 65.6% to 74.0% on Stanford Online Products and from 56.2% to 78.4% on Stanford Cars over FDSL pre-training. These results suggest that parameter-derived relational supervision provides a stronger synthetic pre-training signal than label-based classification for transfer beyond recognition.
