---
source: farmer/huggingface
farmed: 2026-09-01T08:46:18.970698+00:00
arxiv_id: 2608.29252
url: https://huggingface.co/papers/2608.29252
arxiv_url: https://arxiv.org/abs/2608.29252
date: 2026-09-01
---

# Dynamic Important Example Mining for Reinforcement Finetuning

Reinforcement fine-tuning (RFT) is increasingly used to strengthen the reasoning abilities of large models, yet its effectiveness is bound by how training data are selected and used. Most data-centric RFT methods rely on static or heuristic sample selection, implicitly assuming a sample's value is fixed over training. This overlooks the non-stationary dynamics of policy learning and can lead to suboptimal updates. We propose Dynamic Important Example Mining (DIEM), a principled and fully automated framework that makes data utilization adaptive throughout RFT. DIEM integrates two components into each optimization step: (i) a gradient-alignment importance estimator that efficiently approximates each sample's marginal contribution to policy improvement; and (ii) a constrained batch reweighting scheme that maximizes aggregate utility while preserving the update's gradient magnitude to stabilize optimization. Across several reasoning benchmarks, DIEM consistently outperforms strong static and dynamic baselines. The code will be released via https://github.com/hrtan/DIEM.
