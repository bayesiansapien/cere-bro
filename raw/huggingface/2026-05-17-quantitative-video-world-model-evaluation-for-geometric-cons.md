---
source: farmer/huggingface
farmed: 2026-05-17T00:00:00Z
arxiv_id: "2605.15185"
url: "https://huggingface.co/papers/2605.15185"
arxiv_url: "https://arxiv.org/abs/2605.15185"
date: 2026-05-17
---

# Quantitative Video World Model Evaluation for Geometric-Consistency

Generative video models are increasingly studied as implicit world models, yet evaluating whether they produce physically plausible 3D structure and motion remains challenging. Most existing video evaluation pipelines rely heavily on human judgment or learned graders, which can be subjective and weakly diagnostic for geometric failures. We introduce PDI-Bench (Perspective Distortion Index), a quantitative framework for auditing geometric coherence in generated videos. Given a generated clip, we obtain object-centric observations via segmentation and point tracking, lift them to 3D world-space coordinates via monocular reconstruction, and compute a set of projective-geometry residuals capturing three failure dimensions: scale-depth alignment, 3D motion consistency, and 3D structural rigidity. To support systematic evaluation, we build PDI-Dataset, covering diverse scenarios designed to stress these geometric constraints. Across state-of-the-art video generators, PDI reveals consistent geometry-specific failure modes that are not captured by common perceptual metrics.
