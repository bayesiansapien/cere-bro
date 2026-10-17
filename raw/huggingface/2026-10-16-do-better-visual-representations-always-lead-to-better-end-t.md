---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.09695
url: https://huggingface.co/papers/2610.09695
arxiv_url: https://arxiv.org/abs/2610.09695
date: 2026-10-16
---

# Do Better Visual Representations Always Lead to Better End-to-End Autonomous Driving?

Visual foundation models (VFMs) are increasingly integrated into end-to-end autonomous driving for their powerful representations, yet it remains unclear when these representations improve driving performance. To investigate this question, we introduce ViRA, a planner-agnostic visual representation alignment framework that keeps the planner architecture and inference cost unchanged. Our study reveals three findings: (1) VFM-guided visual representations consistently improve driving performance across diverse end-to-end planners, with gains extending to zero-shot closed-loop evaluation. (2) The choice of VFM target matters for planning performance, and alignment to a different VFM can further benefit planners with pre-trained VFM encoders. (3) Auxiliary perception supervision reduces sensitivity to VFM target selection, narrowing the EPDMS spread across five targets from 2.7 to 0.5 points and potentially compensating for less effective VFM targets. Guided by these findings, we develop ViRA-Diffusion, a diffusion-based planner trained without auxiliary perception supervision, which achieves 92.3 EPDMS on NAVSIM v2 navtest, outperforming recent methods in our comparison by at least 1.9 points. The results motivate jointly considering target selection and planner supervision when integrating VFMs into end-to-end autonomous driving. The results and demo are available at https://github.com/OpenDriveLab/ViRA.
