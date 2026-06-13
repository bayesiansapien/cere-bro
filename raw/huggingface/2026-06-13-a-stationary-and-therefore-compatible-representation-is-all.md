---
source: farmer/huggingface
farmed: 2026-06-13T03:34:05Z
arxiv_id: 2606.12488
url: https://huggingface.co/papers/2606.12488
arxiv_url: https://arxiv.org/abs/2606.12488
date: 2026-06-13
---

# A Stationary (and Therefore Compatible) Representation is All You Need

Learning compatible representations aims to learn feature representations that can be used interchangeably over time whenever a model undergoes updates. In this paper, we demonstrate that stationary representations learned by d-Simplex fixed classifiers imply compatibility as in its formal definition. This result establishes a foundation for future works and can be directly exploited in practical learning scenarios. We address the challenge of learning compatibility using d-Simplex fixed classifiers when the model is sequentially fine-tuned. Learning according to a d-Simplex fixed classifier with the cross-entropy loss aligns feature distributions at the first-order statistics. Consequently, it may not fully capture higher-order dependencies in the representation between model updates. To address this issue, we demonstrate that training the model using a d-Simplex fixed classifier through a convex combination of the cross-entropy loss and a contrastive loss not only captures higher-order dependencies, but is also equivalent to learning with the cross-entropy under the compatibility constraints. We confirm our findings with extensive experiments also considering a new scenario where a pre-trained model is sequentially fine-tuned and occasionally replaced with an improved model. We show that stationary representations enable uninterrupted retrieval services (without reprocessing gallery images) while improving performance during model updates and replacements, achieving state-of-the-art. Code at https://github.com/miccunifi/iamcl2r.
