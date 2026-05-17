---
source: farmer/huggingface
farmed: 2026-05-17T00:00:00Z
arxiv_id: "2605.14984"
url: "https://huggingface.co/papers/2605.14984"
arxiv_url: "https://arxiv.org/abs/2605.14984"
date: 2026-05-17
---

# Sat3DGen: Comprehensive Street-Level 3D Scene Generation from Single Satellite Image

Generating a street-level 3D scene from a single satellite image is a crucial yet challenging task. Current methods present a stark trade-off: geometry-colorization models achieve high geometric fidelity but are typically building-focused and lack semantic diversity. In contrast, proxy-based models use feed-forward image-to-3D frameworks to generate holistic scenes by jointly learning geometry and texture, a process that yields rich content but coarse and unstable geometry. We introduce Sat3DGen to address these fundamental challenges, which embodies a geometry-first methodology. This methodology enhances the feed-forward paradigm by integrating novel geometric constraints with a perspective-view training strategy, explicitly countering the primary sources of geometric error. On our benchmark, our method improves geometric RMSE from 6.76m to 5.20m and reduces the Frechet Inception Distance (FID) from ~40 to 19 against the leading method.
