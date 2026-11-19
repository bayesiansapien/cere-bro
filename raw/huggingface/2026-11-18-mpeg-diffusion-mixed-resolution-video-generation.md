---
source: farmer/huggingface
farmed: 2026-11-19T11:13:13+05:30
arxiv_id: 2611.12069
url: https://huggingface.co/papers/2611.12069
arxiv_url: https://arxiv.org/abs/2611.12069
date: 2026-11-18
---

# MPEG-Diffusion: Mixed-Resolution Video Generation

Video diffusion transformers (DiTs) generate realistic videos, but their heavy computational cost limits broader real-world applications. Mixed-resolution generation reduces this cost by generating the visually important region at high resolution (HR) and the rest at low resolution (LR), yet existing methods suffer a severe quality drop on videos and require knowing the HR region in advance. We show that these failures are not inherent to mixed resolution, and propose MPEG-Diffusion to address their three root causes: (1) dual-resolution attention to mitigate the curse of mixed resolution, where each query reads the K/V of its own resolution, (2) a mixed-resolution decoder to blend the HR and LR latents before decoding and resolve distortion, and (3) a self-selected HR region using the DiT's knowledge to find the visually important region without requiring it in advance. Processing only 30% of full-resolution tokens, MPEG-Diffusion speeds up denoising by 4.8times on Wan2.1 14B (3.8times on 1.3B), outperforming prior methods on nearly every metric. In the user study, we demonstrate the high quality of MPEG-Diffusion, with raters preferring it over prior mixed-resolution methods in over 90% of pairs and rating it close to full resolution.
