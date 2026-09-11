---
source: farmer/huggingface
farmed: 2026-09-11T21:57:41.002444
arxiv_id: 2609.10715
url: https://huggingface.co/papers/2609.10715
arxiv_url: https://arxiv.org/abs/2609.10715
date: 2026-09-11
---

# NCP-ArchPreview Technical Report: Moving towards Latent Space Language Models through Next Concept Prediction

We introduce NCP-ArchPreview, a latent-space language model that pushes autoregressive pretraining beyond standard next-token prediction (NTP). Alongside NTP, the model learns through Next Concept Prediction (NCP) to predict discrete concepts that span multiple tokens, introducing an explicit and more challenging concept-level objective while preserving standard token-level autoregressive generation. NCP-ArchPreview builds a latent space by constructing a product-quantized concept vocabulary directly from its hidden states, and subsequently learns to predict future concepts via a dedicated Concept Module. These predicted concepts are then fed back to the token level to guide subsequent generation, with NTP and NCP trained jointly end-to-end. We scale this architecture to 8.9B parameters and train it on 5.73T tokens from the Dolma-3 dataset, marking the largest demonstration of a latent-space language model to date. Remarkably, by consuming only 51.3% of the total training tokens, NCP-ArchPreview achieves the final pretraining loss of OLMo-3-7B. Following full pretraining, it outperforms OLMo-3-7B by 2.45 points on the downstream macro-average, including a notable 5.99-point gain on GSM8K. Controlled experiments isolate a clear progression of performance gains stemming from both the latent architecture and the NCP objective. Furthermore, utilizing only 85% of the standard computation, NCP-ArchPreview approaches the training loss of a strictly parameter-aligned 8.9B baseline. The learned latent space remains highly valuable after the pretraining stage: updating just the 17M-parameter VQ module yields a novel, lightweight interface for domain adaptation, while a simple injection of concept representations into a DFlash2 drafter improves the mean accepted length by 4.17% with negligible overhead.
