---
source: farmer/huggingface
farmed: 2026-05-17T00:00:00Z
arxiv_id: "2605.14386"
url: "https://huggingface.co/papers/2605.14386"
arxiv_url: "https://arxiv.org/abs/2605.14386"
date: 2026-05-17
---

# Darwin Family: MRI-Trust-Weighted Evolutionary Merging for Training-Free Scaling of Language-Model Reasoning

We present Darwin Family, a framework for training-free evolutionary merging of large language models via gradient-free weight-space recombination. We ask whether frontier-level reasoning performance can be improved without additional training, by reorganizing latent capabilities already encoded in existing checkpoints. Darwin introduces three key ideas: (i) a 14-dimensional adaptive merge genome enabling fine-grained component- and block-level recombination; (ii) MRI-Trust Fusion, which adaptively balances diagnostic layer-importance signals with evolutionary search through a learnable trust parameter; and (iii) an Architecture Mapper that enables cross-architecture breeding between heterogeneous model families. Empirically, the flagship Darwin-27B-Opus achieves 86.9% on GPQA Diamond, ranking #6 among 1,252 evaluated models, and outperforming its fully trained foundation model without any gradient-based training. Across scales from 4B to 35B parameters, Darwin models consistently improve over their parents, support recursive multi-generation evolution, and enable a training-free evolutionary merge that combines Transformer- and Mamba-based components.
