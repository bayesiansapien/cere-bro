---
source: farmer/huggingface
farmed: 2026-07-31T19:58:50.731985
arxiv_id: 2607.27958
url: https://huggingface.co/papers/2607.27958
arxiv_url: https://arxiv.org/abs/2607.27958
date: 2026-07-31
---

# Σ-Mem: An Online Reliability Memory for LLM-based Multi-Agent Systems

Memory is central to long-horizon LLM agents, yet existing memory systems primarily preserve interaction content rather than modeling which agents can be trusted and under what conditions. This limitation is particularly important in multi-agent systems, where a central model may be unable to directly verify plausible or correlated peer responses. We introduce Σ-Mem, an online reliability memory that records historical competence evidence for individual peers and peer relationship evidence across the peer set. Both forms of evidence are maintained as real symmetric states and updated from post-decision correctness feedback. By Weyl's inequality, the spectral change caused by each event-level update is bounded, enabling stable online adaptation without retraining the underlying models. Σ-Mem provides a general write-and-read interface: the same memory can be used for residual steering of a central model, response-free peer routing, or reliability-weighted voting. Across five Qwen-family models, Σ-Mem adapts to counterfactual reliability shifts and generalizes to unseen peers and task domains. Direct memory readouts also outperform majority voting and the best fixed peer over the full OOD evaluation set. Moreover, performance improves consistently as more correctness feedback becomes available, indicating that Σ-Mem progressively accumulates actionable reliability information. These results establish reliability memory as a reusable foundation for adaptive coordination in LLM-based multi-agent systems.
