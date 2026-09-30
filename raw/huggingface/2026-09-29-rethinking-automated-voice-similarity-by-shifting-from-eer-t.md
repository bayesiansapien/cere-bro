---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.932635+00:00
arxiv_id: 2609.33999
url: https://huggingface.co/papers/2609.33999
arxiv_url: https://arxiv.org/abs/2609.33999
date: 2026-09-29
---

# Rethinking Automated Voice Similarity by Shifting from EER to Embedding Geometry

Speaker verification (SV) models are commonly assumed to better capture nuances among speaker characteristics as verification accuracy improves, leading to their widespread use as automated proxies for human voice similarity in speech generation tasks. However, by establishing a human perceptual alignment metric and conducting systematic analysis, we demonstrate that perceptual alignment is governed far more by how a model is trained (its learning objective) than by how well it performs (EER). Notably, standard margin-based classification losses (e.g., AAM-Softmax) yield substantially lower perceptual alignment than prototypical metric losses, while EER itself fails to track human judgment, directly challenging the community's implicit assumption. We trace this divergence to embedding geometry, where a model's effective dimensionality (d_{eff}) tracks perceptual alignment with a -0.95 rank correlation, revealing that the dimensional spread favored by classification losses fundamentally clashes with the low-dimensional nature of human voice perception. Imposing a dimensionality bottleneck compresses d_{eff} and raises perceptual alignment (ρ_{align}) from 0.08 to 0.74, establishing a principled geometric criterion for evaluating voice similarity.
