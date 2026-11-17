---
source: farmer/huggingface
farmed: 2026-11-17T08:29:02.002349+00:00
arxiv_id: 2611.02822
url: https://huggingface.co/papers/2611.02822
arxiv_url: https://arxiv.org/abs/2611.02822
date: 2026-11-16
---

# Disen-Forcing: Disentangling Semantic Anchoring from Motion for Autoregressive Video Diffusion

Autoregressive video diffusion models (AR-VDMs) enable real-time, long-horizon video generation but degrade rapidly once the inference horizon outruns the training horizon, due to compounding exposure bias. To stabilize long rollouts, recent methods heuristically adopt frame sink, keeping initial frames as a persistent model context, inspired by attention sinks in LLMs. We revisit this design and find that the mechanism by which initial frames stabilize long-range consistency in AR-VDMs is not an LLM-style attention sink; instead, long-range consistency is anchored through a sparse subset of attention heads, while the majority of heads predominantly capture local temporal dynamics. This observation reveals an over-conditioning pathology in existing frame-sink strategies: by universally exposing every head to the pinned initial-frame context, the model becomes prone to collapsing motion toward the low-dynamic modes of the teacher during model distillation. We propose Disen-Forcing, a distillation-time plug-in for AR-VDMs that disentangles and reinforces this head specialization through disentangled context routing and motion-disentangling regularization. On long-horizon video generation benchmarks, Disen-Forcing simultaneously improves long-range consistency and motion dynamics of base AR-VDMs, a trade-off that sink-based methods fail to balance.
