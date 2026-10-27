---
source: farmer/huggingface
farmed: 2026-10-27T05:06:31.801639+00:00
arxiv_id: 2610.32894
url: https://huggingface.co/papers/2610.32894
arxiv_url: https://arxiv.org/abs/2610.32894
date: 2026-10-26
---

# LoCA: Enabling Multi-Modality in Geospatial Location Encoders

Location encoders map geographic coordinates to high-dimensional descriptors through contrastive alignment with paired Earth Observation imagery. We prove that this construction is structurally limited: any Lipschitz location encoder produces an output of intrinsic dimension at most 2, regardless of architecture or bandwidth, which forces the contrastive loss to strictly exceed its asymptotic optimum. Empirically, joint training also collapses the encoder's embedding covariance to low rank. Although dimension-limited, current location encoders sidestep this spectral collapse by training against a frozen image encoder, which we reinterpret as a covariance regularizer that supplies a high-rank target for the location encoder to fold onto. However, extending this approach to multimodal inputs is challenging, as location encoders should simultaneously map a single location to multiple, potentially incompatible, descriptors. We identify two requirements a regularizer must satisfy for location encoding in multimodal regimes: co-alignment across modalities, since adapters alone cannot align independently pretrained encoders; and high effective rank, since the location encoder inherits its target's spectrum. We propose LoCA (Location Contrastive Alignment), a two-stage pipeline that satisfies both. Stage 1 jointly trains Sentinel-1 and Sentinel-2 encoders with contrastive learning, producing a co-aligned, high-rank multimodal target. Stage 2 freezes the image encoders and trains a location and a tabular metadata encoder as projection adapters with multi-view contrastive learning. Against five state-of-the-art encoders on 17 tasks ranging from land cover and wildfire forecasting to geophysical, socio-economic, biodiversity and climate applications, LoCA achieves the most task wins, is the only model to outperform every other on a majority of tasks, and wins 68.8% of all per-task comparisons.
