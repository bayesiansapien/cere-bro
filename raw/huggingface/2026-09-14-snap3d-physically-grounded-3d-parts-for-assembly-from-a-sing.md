---
source: farmer/huggingface
farmed: 2026-09-14T06:17:21.172209+00:00
arxiv_id: 2609.13146
url: https://huggingface.co/papers/2609.13146
arxiv_url: https://arxiv.org/abs/2609.13146
date: 2026-09-14
---

# SNAP3D: Physically Grounded 3D Parts for Assembly from a Single Image

Part-aware 3D asset generation enables applications such as editing, articulation, simulation, and fabrication, yet existing methods can generate visually complete individual parts without ensuring that they form a valid physical assembly. Consequently, generated neighboring parts may interpenetrate, lack valid connections, or collapse under gravity. We propose a physics-guided framework for improving single-image part-aware 3D generation with physically compatible geometry and stable connections. Our method resolves inter-part penetration, recovers a contact graph between neighboring parts, and introduces parameterized connectors at their contact surfaces. Using feedback from physical simulation, we refine connector placement, orientation, and dimensions to improve assembly stability while preserving the generated geometry. We further introduce a physics-based evaluation protocol that complements conventional geometric metrics by directly testing assembly validity and stability under gravity. Experiments comparing against multiple part-aware 3D generators show substantial improvements in physical realizability and stability while maintaining geometric quality. We additionally validate the resulting parts through 3D printing and real-world assembly.
