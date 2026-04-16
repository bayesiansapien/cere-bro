---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13793
category: cs.CV
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13793
published: 2026-04-16
authors: Mohammad Mahdi, Nedko Savov, Danda Pani Paudel
---

# From Synchrony to Sequence: Exo-to-Ego Generation via Interpolation

**arXiv:** https://arxiv.org/abs/2604.13793
**Authors:** Mohammad Mahdi, Nedko Savov, Danda Pani Paudel

## Abstract

arXiv:2604.13793v1 Announce Type: new  Abstract: Exo-to-Ego video generation aims to synthesize a first-person video from a synchronized third-person view and corresponding camera poses. While paired supervision is available, synchronized exo-ego data inherently introduces substantial spatio-temporal and geometric discontinuities, violating the smooth-motion assumptions of standard video generation benchmarks. We identify this synchronization-induced jump as the central challenge and propose Syn2Seq-Forcing, a sequential formulation that interpolates between the source and target videos to form a single continuous signal. By reframing Exo2Ego as sequential signal modeling rather than a conventional condition-output task, our approach enables diffusion-based sequence models, e.g. Diffusion Forcing Transformers (DFoT), to capture coherent transitions across frames more effectively. Empirically, we show that interpolating only the videos, without performing pose interpolation already produces significant improvements, emphasizing that the dominant difficulty arises from spatio-temporal discontinuities. Beyond immediate performance gains, this formulation establishes a general and flexible framework capable of unifying both Exo2Ego and Ego2Exo generation within a single continuous sequence model, providing a principled foundation for future research in cross-view video synthesis.
