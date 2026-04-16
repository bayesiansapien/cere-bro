---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13409
category: cs.CV
concept: agents-tool-use
url: https://arxiv.org/abs/2604.13409
published: 2026-04-16
authors: Bo Liu, Yulong Zou, Jin Hong
---

# CausalDisenSeg: A Causality-Guided Disentanglement Framework with Counterfactual Reasoning for Robust Brain Tumor Segmentation Under Missing Modalities

**arXiv:** https://arxiv.org/abs/2604.13409
**Authors:** Bo Liu, Yulong Zou, Jin Hong

## Abstract

arXiv:2604.13409v1 Announce Type: new  Abstract: In clinical practice, the robustness of deep learning models for multimodal brain tumor segmentation is severely compromised by incomplete MRI data. This vulnerability stems primarily from modality bias, where models exploit spurious correlations as shortcuts rather than learning true anatomical structures. Existing feature fusion methods fail to fundamentally eliminate this dependency. To address this, we propose CausalDisenSeg, a novel Structural Causal Model (SCM)-grounded framework that achieves robust segmentation via causality-guided disentanglement and counterfactual reasoning. We reframe the problem as isolating the anatomical Causal Factor from the stylistic Bias Factor. Our framework implements a three-stage causal intervention: (1) Explicit Causal Disentanglement: A Conditional Variational Autoencoder (CVAE) coupled with an HSIC constraint mathematically enforces statistical orthogonality between anatomical and style features. (2) Causal Representation Reinforcement: A Region Causality Module (RCM) explicitly grounds causal features in physical tumor regions. (3) Counterfactual Reasoning: A dual-adversarial strategy actively suppresses the residual Natural Direct Effect (NDE) of the bias, forcing its spatial attention to be mutually exclusive from the causal path. Extensive experiments on the BraTS 2020 dataset demonstrate that CausalDisenSeg significantly outperforms state-of-the-art methods in accuracy and consistency across severe missing-modality scenarios. Furthermore, cross-dataset evaluation on BraTS 2023 under the same protocol yields a state-of-the-art macro-average DSC of 84.49.
