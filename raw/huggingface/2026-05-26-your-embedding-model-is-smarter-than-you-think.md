---
source: farmer/huggingface
farmed: 2026-05-26T06:42:03Z
arxiv_id: 2605.24938
url: https://huggingface.co/papers/2605.24938
arxiv_url: https://arxiv.org/abs/2605.24938
date: 2026-05-26
---

# Your Embedding Model is SMARTer Than You Think

Multimodal retrieval relies heavily on single-vector retrievers, which compress rich, sequential token sequences into one single global representation. While efficient, they discard fine-grained, local evidence critical for dense retrieval tasks. Multi-vector approaches were introduced as a solution, but they strictly require training and many ignore the necessity of a globally summarizing representation. To address this, we introduce SMART, a framework that unlocks the latent multi-vector capabilities of standard single-vector models. We first demonstrate that standard contrastive training on the pooled embedding implicitly shapes the retrieval geometry of preceding hidden states via gradient flow. By applying direct late-interaction over these frozen hidden states during inference, SMART acts as a plug-and-play upgrade that consistently improves performance across diverse modalities, improving even the state-of-the-art models further on MMEB-V2. We also reveal SMART's superior performance, as simple lightweight post-training not only saves time and compute, but also brings forth further improvement on Visual Document retrieval, allowing a single-vector model to outperform SoTA multi-vector counterparts. Ultimately, SMART offers both a highly efficient inference enhancement and a powerful finetuning technique for multimodal retrieval. We open source our code and weights at https://github.com/HanSolo9682/SMART.
