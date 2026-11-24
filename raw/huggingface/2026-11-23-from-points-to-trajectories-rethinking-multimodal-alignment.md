---
source: farmer/huggingface
farmed: 2026-11-24T05:05:48.250134+00:00
arxiv_id: 2611.24249
url: https://huggingface.co/papers/2611.24249
arxiv_url: https://arxiv.org/abs/2611.24249
date: 2026-11-23
---

# From Points to Trajectories: Rethinking Multimodal Alignment for Physical Events

Advancing physical artificial intelligence (Physical AI) requires moving beyond static object recognition to ground how real-world mechanics (e.g., impact, friction, and force transfer) unfold over time. While multimodal aligners seek to capture these interactions by matching multi-sensor streams, prevailing architectures compress each temporal sequence into a single pooled embedding. We show that this paradigm fails on twin events: distinct physical executions recorded under identical task conditions. Collapsing the temporal dimension averages out transient cross-modal dynamics, effectively reducing physical event alignment to static scene recognition. Formally, we prove that as sequence length increases, any temporally pooled representation converges to the stationary recording condition. Consequently, as windows grow, no choice of loss function or embedding geometry can disambiguate twin events from pooled features alone. Instead, we show that physical events are uniquely identified by the event gap, namely the instantaneous, synchronous co-fluctuations across modalities that are erased by pooling and accumulate only along unpooled trajectories. To recover this signal, we introduce CounterPoint, a lightweight plug-in module that strips out each modality's temporal mean to score frame-level cross-modal agreement. Integrated across four state-of-the-art (SOTA) multimodal aligners, CounterPoint shifts representations from coarse condition matching to fine-grained physical event alignment, consistently outperforming existing temporal alignment methods.
