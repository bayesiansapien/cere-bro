---
source: farmer/huggingface
farmed: 2026-10-10T05:09:51.411821+00:00
arxiv_id: 2610.12421
url: https://huggingface.co/papers/2610.12421
arxiv_url: https://arxiv.org/abs/2610.12421
date: 2026-10-09
---

# Beyond Spatio-Temporal Priors: A Generalizable Approach for Dense Correspondence Matching

Dense correspondence matching has historically been bounded by simplifying spatio-temporal priors, such as smooth motion and rigid geometry. While effective for classical tasks, these assumptions break down in image editing and reference-guided generation (IEG), where transformations can preserve visual identity while breaking physical continuity. To establish identity-preserving correspondence across such transformations, we introduce FreeMatching, a generalizable framework combining generative and semantic foundation representations with heterogeneous supervision from classical datasets, tracked videos, and synthetic scenes. Teacher-guided iterative refinement further improves correspondence in IEG without dense correspondence annotations. Experimentally, a single FreeMatching model substantially improves correspondence quality on challenging IEG image pairs while retaining competitive performance on classical benchmarks. Furthermore, we demonstrate its utility as a quantitative metric for evaluating identity preservation, with scores that correlate with human judgment. The code is available at https://github.com/luping-liu/FreeMatching.
