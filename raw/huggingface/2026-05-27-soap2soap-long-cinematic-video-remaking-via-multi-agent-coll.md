---
source: farmer/huggingface
farmed: 2026-05-27T07:52:03Z
arxiv_id: 2605.17423
url: https://huggingface.co/papers/2605.17423
arxiv_url: https://arxiv.org/abs/2605.17423
date: 2026-05-27
upvotes: 12
---

# Soap2Soap: Long Cinematic Video Remaking via Multi-Agent Collaboration

We study series-level cinematic remaking, a long-horizon video-to-video generation problem that localizes full episodes or films via stylization or actor replacement while strictly preserving narrative structure, motion choreography, and character identity across hundreds of shots. Existing video generation and editing pipelines often break down in this regime due to compounding identity drift, background mutation, and semantic erosion under large camera motions and viewpoint changes. We propose Soap2Soap, a multi-agent framework that enforces long-term language-visual consistency through a Dual-Bridge Consistency mechanism: a scene-aware JSON screenplay serving as a persistent semantic backbone, and dynamically allocated visual reference anchors at both scene and shot levels. To suppress drift before video synthesis, we introduce batch keyframe consistency, jointly generating multiple keyframes in a shared latent context via a grid-based formulation. A closed-loop verification agent further audits identity, stability, and alignment to trigger selective regeneration. Experiments on SoapBench demonstrate strong improvements over commercial video generation APIs in long-term consistency and narrative fidelity.
