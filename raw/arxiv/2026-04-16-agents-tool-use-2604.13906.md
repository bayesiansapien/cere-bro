---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13906
category: cs.CV
concept: agents-tool-use
url: https://arxiv.org/abs/2604.13906
published: 2026-04-16
authors: Shuyun Wang, Hu Zhang, Xin Shen
---

# Blind Bitstream-corrupted Video Recovery via Metadata-guided Diffusion Model

**arXiv:** https://arxiv.org/abs/2604.13906
**Authors:** Shuyun Wang, Hu Zhang, Xin Shen

## Abstract

arXiv:2604.13906v1 Announce Type: new  Abstract: Bitstream-corrupted video recovery aims to restore realistic content degraded during video storage or transmission. Existing methods typically assume that predefined masks of corrupted regions are available, but manually annotating these masks is labor-intensive and impractical in real-world scenarios. To address this limitation, we introduce a new blind video recovery setting that removes the reliance on predefined masks. This setting presents two major challenges: accurately identifying corrupted regions and recovering content from extensive and irregular degradations. We propose a Metadata-Guided Diffusion Model (M-GDM) to tackle these challenges. Specifically, intrinsic video metadata are leveraged as corruption indicators through a dual-stream metadata encoder that separately embeds motion vectors and frame types before fusing them into a unified representation. This representation interacts with corrupted latent features via cross-attention at each diffusion step. To preserve intact regions, we design a prior-driven mask predictor that generates pseudo masks using both metadata and diffusion priors, enabling the separation and recombination of intact and recovered regions through hard masking. To mitigate boundary artifacts caused by imperfect masks, a post-refinement module enhances consistency between intact and recovered regions. Extensive experiments demonstrate the effectiveness of our method and its superiority in blind video recovery. Code is available at: https://github.com/Shuyun-Wang/M-GDM.
