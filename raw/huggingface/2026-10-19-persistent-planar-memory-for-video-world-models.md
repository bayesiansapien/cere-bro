---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.23795
url: https://huggingface.co/papers/2610.23795
arxiv_url: https://arxiv.org/abs/2610.23795
date: 2026-10-19
---

# Persistent Planar Memory for Video World Models

Video world models that generate and explore environments at scale need a persistent 3D memory of what they have produced. Plane primitives offer a natural candidate: a compact set of oriented planes captures the dominant structural elements (e.g., walls, floors, facades) of indoor and outdoor scenes, while requiring only 7 parameters per primitive. We present PPMem, a video world model that adopts plane primitives as its persistent 3D memory. PPMem augments a video diffusion transformer with a planar prediction head and a Depth Token Fusion (DTF) module: each autoregressive chunk jointly produces RGB video and planar geometry, which merges into a persistent plane memory that conditions subsequent chunks via rendered depth. The resulting memory is three orders of magnitude more compact than per-pixel point clouds (~100K primitives, 5MB for a full scene), geometrically explicit (metric depth, normals, exportable surfaces), cross-view consistent (jointly predicted by the shared backbone), and adaptive (refined by the merging procedure as generation proceeds). On DL3DV and RealEstate10K, PPMem outperforms prior 3D-grounded world models in video quality while jointly producing metric-scale depth, surface normals, and exportable planar geometry, sustaining coherence across hundreds of frames under large viewpoint changes. Project page: https://hyzcluster.github.io/ppmem.
