---
source: farmer/huggingface
farmed: 2026-11-20T05:04:58.140872+00:00
arxiv_id: 2611.17600
url: https://huggingface.co/papers/2611.17600
arxiv_url: https://arxiv.org/abs/2611.17600
date: 2026-11-19
---

# LightTAR: Light and Fast Target-Aware Representations for Multimodal Tabular Learning

Multimodal tabular learning involves classification and regression on tables combining structured numerical and categorical features with unstructured text and images. These unstructured fields are commonly represented by pretrained encoder embeddings reduced with principal component analysis (PCA). This reduction prioritizes input variance but may overlook information relevant to predicting the target. We introduce LightTAR, a simple, inexpensive method that adapts dimensionality reduction to the prediction task. LightTAR augments the standard PCA representation with a few target-aware features extracted jointly from the final and an intermediate encoder layer using regularized partial least squares (PLS). We evaluate LightTAR with 21 tabular models, including tree ensembles, neural networks, and tabular foundation models. LightTAR improves average predictive performance for all models and, averaged across models, improves prediction on almost every MulTaBench dataset. These gains come with a small increase in total runtime relative to PCA representations. LightTAR integrates directly into existing encoding pipelines, improving tabular learners' predictive performance without modifying the encoder or the learner.
