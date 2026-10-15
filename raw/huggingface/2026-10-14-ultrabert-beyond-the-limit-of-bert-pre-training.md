---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.502715+00:00
arxiv_id: 2610.15028
url: https://huggingface.co/papers/2610.15028
arxiv_url: https://arxiv.org/abs/2610.15028
date: 2026-10-14
---

# UltraBERT: Beyond the Limit of BERT Pre-Training

Recent bidirectional encoders have been modernized with innovations from causal large language models (LLMs). However, the pretraining recipe itself remains inherited from small-scale conventions, leaving encoders underoptimized, with no single model performing competitively across both classification and retrieval tasks. In this work, we investigate how far encoder performance can be pushed by revisiting core design choices in training, revealing three key findings: (1) Encoders saturate on downstream tasks beyond a few trillion tokens, indicating that additional compute past this point does not help. (2) Across model sizes, lower masking ratios benefit classification while higher ones benefit retrieval, contradicting prior work suggesting larger ratios for larger models. (3) Distillation with pruning improves classification at low masking ratios but degrades retrieval at high ones. Guided by these findings, we present UltraBERT, a single encoder that assigns separate LM heads to low and high masking ratios within a batch and restricts the distillation objective to the low ratio. To our knowledge, UltraBERT is the first encoder to achieve state of the art on both classification and retrieval tasks, reaching 91.0 on GLUE and 47.7 on BEIR. Together, these results show how far encoder performance can be pushed and provide a principled basis for compute allocation, masking ratio design, and knowledge transfer in bidirectional models.
