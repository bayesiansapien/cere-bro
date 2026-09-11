---
source: farmer/huggingface
farmed: 2026-09-11T21:57:41.002444
arxiv_id: 2609.11317
url: https://huggingface.co/papers/2609.11317
arxiv_url: https://arxiv.org/abs/2609.11317
date: 2026-09-11
---

# Mi-Ripple: Restoring Images Degraded by Iterative AI Editing

Iterative reference-conditioned image editing can introduce grid-like and granular textures, commonly described as digital ripple. We present Mi-Ripple, a diagnosis-guided restoration workflow that suppresses this digital ripple while protecting image structure. Mi-Ripple separates periodic lattice artifacts from content-entangled granular texture, then combines selective spectral notching, structure-aware smoothing, and cleaned-reference regeneration. This separation enables low-distortion filtering when artifacts are spectrally isolated and visual reconstruction when filtering would erase legitimate detail. Across fourteen notch-only executions, whole-image residual standard deviation is 0.08--0.44 in CIELAB lightness units. In a paired regeneration example, reference cleaning reduces output debris density by 45\%. Mi-Ripple links measurable artifact reduction to visibly cleaner generated images, rather than optimizing a spectral score alone.
