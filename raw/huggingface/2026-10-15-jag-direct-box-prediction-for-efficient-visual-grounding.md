---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.232841+05:30
arxiv_id: 2610.13239
url: https://huggingface.co/papers/2610.13239
arxiv_url: https://arxiv.org/abs/2610.13239
date: 2026-10-15
---

# Jag: Direct Box Prediction for Efficient Visual Grounding

Visual grounding combines image--language understanding with geometric prediction, yet autoregressive multimodal models often express a box as a coordinate sequence. Sequential decoding adds computation to the multimodal processing needed for localization. Adapting these representations to box geometry offers a route to direct prediction. We present Jag, which adapts a compact pretrained multimodal model for direct continuous box prediction. A lightweight regression head reads the last valid input-token state, conditioned on the image and referring expression, and predicts all four box coordinates together. Geometric supervision jointly adapts the language backbone, visual merger, and regression head, allowing localization losses to shape both the multimodal representations and the coordinate mapping. Inference retains image--language processing and returns the box in one forward pass, without coordinate generation or text parsing. Across benchmarks, Jag consistently improves grounding accuracy over its base model across the observed target sizes and expression groups. Component ablation show that jointly adapting the representations and head substantially improves accuracy over training the head alone. Against existing specialized grounding models, it achieves competitive accuracy with lower single-request latency and GPU memory use. These results show how supervision tailored to the geometric answer can specialize a compact pretrained multimodal model for accurate grounding and efficient direct prediction. Project page: https://xyzzzh.github.io/Jag/
