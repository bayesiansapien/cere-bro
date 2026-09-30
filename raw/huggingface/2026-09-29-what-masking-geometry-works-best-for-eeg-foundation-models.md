---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.936449+00:00
arxiv_id: 2609.33487
url: https://huggingface.co/papers/2609.33487
arxiv_url: https://arxiv.org/abs/2609.33487
date: 2026-09-29
---

# What masking geometry works best for EEG foundation models?

EEG foundation models hold promise for scalable brain-signal decoding across clinical and cognitive neuroscience applications, yet their pre-training pipelines remain poorly understood. Among design choices, the masking strategy is particularly critical: it determines what the network must predict and from which context. Yet it has never been ablated in isolation, as each new model bundles a new masking strategy with a new backbone and objective. In this paper, we formalize the design choices for spatio-temporal masking strategies and train various models with a single pipeline under varying masking configurations across two SSL frameworks (MAE and JEPA). We then systematically evaluate the resulting 58 pre-trained models on the 12 datasets of OpenEEGBench under a linear probe. Both frameworks agree on an optimal masking configuration and on shared failure modes. Outside these, performance is robust: 11 MAE and 9 JEPA configurations are statistically indistinguishable from the best. We further identify a novel JEPA-specific failure mode, tagged bias-inflation collapse, invisible to standard detectors. With a well-chosen mask, our pipeline reaches REVE-level downstream performance at a fraction of REVE's pre-training compute.
