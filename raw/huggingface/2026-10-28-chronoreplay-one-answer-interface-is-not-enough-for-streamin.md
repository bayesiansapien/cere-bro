---
source: farmer/huggingface
farmed: 2026-10-29T10:37:09.993366+05:30
arxiv_id: 2610.34283
url: https://huggingface.co/papers/2610.34283
arxiv_url: https://arxiv.org/abs/2610.34283
date: 2026-10-28
---

# ChronoReplay: One Answer Interface Is Not Enough for Streaming Spatial Intelligence

Training a spatial VLM to answer which side an object lies on does not require it to preserve the metric displacement that determines that answer, while supervision for a distance estimate may leave categorical relations largely unconstrained. When post-training emphasizes one readout, improvements can therefore concentrate on that interface while transfer to others remains weak or even degrades; we call this observed specialization interface lock-in. ChronoReplay addresses it by replaying heterogeneous spatial supervision as chronologically ordered episodes, retaining source-native targets, and balancing supervision across families. Under the same observation access, a single ChronoReplay checkpoint improves OVO-S-Bench, OST-Bench, and UCS-Bench together, including a 13.41-point gain on OST-Bench, and achieves the highest three-benchmark mean among the supervision settings compared here. Same-data controls further separate the ingredients of this transfer: answer serialization redistributes gains across OST and UCS, family-balanced learning improves over ordinary joint SFT and natural turn weighting, and chronological replay exceeds a shifted-order control by about 2.41 OST points across two paired seeds. Adaptive frame selection then changes evidence access while keeping the trained model fixed, providing an additional inference-time gain at lower visual cost. Streaming spatial performance depends on what distinctions supervision preserves, how heterogeneous histories are organized during learning, and what causal evidence inference makes available at test time.
