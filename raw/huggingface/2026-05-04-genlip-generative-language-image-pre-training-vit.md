---
source: farmer/huggingface
farmed: 2026-05-04T00:00:00Z
arxiv_id: 2605.00809
url: https://huggingface.co/papers/2605.00809
arxiv_url: https://arxiv.org/abs/2605.00809
date: 2026-05-04
---

# Let ViT Speak: Generative Language-Image Pre-training

In this paper, we present Generative Language-Image Pre-training (GenLIP), a minimalist generative pretraining framework for Vision Transformers (ViTs) designed for multimodal large language models (MLLMs). To better align vision encoders with the autoregressive nature of LLMs, GenLIP trains a ViT to predict language tokens directly from visual tokens using a standard language modeling objective, without contrastive batch construction or an additional text decoder. This design offers three key advantages: (1) Simplicity: a single transformer jointly models visual and textual tokens; (2) Scalability: it scales effectively with both data and model size; and (3) Performance: it achieves competitive or superior results across diverse multimodal benchmarks. Trained on 8B samples from Recap-DataComp-1B, GenLIP matches or surpasses strong baselines despite using substantially less pretraining data. After continued pretraining on multi-resolution images at native aspect ratios, GenLIP further improves on detail-sensitive tasks such as OCR and chart understanding, making it a strong foundation for vision encoders in MLLMs.
