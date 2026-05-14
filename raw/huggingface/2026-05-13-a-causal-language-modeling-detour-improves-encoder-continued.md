---
source: farmer/huggingface
farmed: 2026-05-14T10:39:11Z
arxiv_id: 2605.12438
url: https://huggingface.co/papers/2605.12438
arxiv_url: https://arxiv.org/abs/2605.12438
date: 2026-05-13
---

# A Causal Language Modeling Detour Improves Encoder Continued Pretraining

When adapting an encoder to a new domain, the standard approach is to continue training with Masked Language Modeling (MLM). We show that temporarily switching to Causal Language Modeling (CLM) followed by a short MLM decay improves downstream performance. On biomedical texts with ModernBERT, this CLM detour outperforms MLM baselines trained on identical data and compute across 8 French and 11 English biomedical tasks, by +1.2-2.8pp and +0.3-0.8pp respectively, depending on model size. We investigate the reasons for these gains. We find that CLM's dense supervision impacts low transformer layers (0-7) far more than MLM does. Freezing low layers during CLM eliminates the downstream benefit; freezing mid layers preserves it. The representational changes persist through the MLM decay phase, even when it matches the CLM phase in length, and they scale with model capacity. We release ModernCamemBERT-bio and ModernBERT-bio as state-of-the-art biomedical encoders in Base and Large sizes.
