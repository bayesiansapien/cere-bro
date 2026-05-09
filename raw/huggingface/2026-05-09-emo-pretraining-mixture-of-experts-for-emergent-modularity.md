---
source: farmer/huggingface
farmed: 2026-05-09T03:37:34Z
arxiv_id: 2605.06663
url: https://huggingface.co/papers/2605.06663
arxiv_url: https://arxiv.org/abs/2605.06663
date: 2026-05-09
---

# EMO: Pretraining Mixture of Experts for Emergent Modularity

Large language models are typically deployed as monolithic systems, requiring the full model even when applications need only a narrow subset of capabilities. We introduce Emo, an MoE designed for modularity, the independent use and composition of expert subsets, without requiring human-defined priors. Our key idea is to encourage tokens from similar domains to rely on similar experts. Since tokens within a document often share a domain, Emo restricts them to select experts from a shared pool, while allowing different documents to use different pools. We pretrain a 1B-active, 14B-total Emo on 1T tokens. Retaining only 25% (12.5%) of experts incurs just a 1% (3%) absolute drop, whereas standard MoEs break under the same setting.
