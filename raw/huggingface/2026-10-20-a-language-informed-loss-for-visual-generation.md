---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.23653
url: https://huggingface.co/papers/2610.23653
arxiv_url: https://arxiv.org/abs/2610.23653
date: 2026-10-20
---

# A Language-Informed Loss for Visual Generation

End-to-end visual generation with pixel-space loss has recently achieved competitive performance without the need for learned image tokenizers. In this work, we study whether language-informed supervision can provide a richer training signal than pixel loss for visual generation. We introduce LILIE (pronounced "lily"), a Language-Informed and Lossless Image Encoder. LILIE is an invertible image transform trained such that a vision-language model can recover captions from noised features. The encoder uses a normalizing flow transformer trained jointly with a vision-language model via next token prediction. We then use the encoder to extract a simple language-informed loss for text-to-image generation. We train JiT models with LILIE loss, reducing gFD by 14 points (66.84 to 53.01) against a pixel-only baseline on the GPIC dataset. Our code, encoders, and generative models are available at https://suchiragarwal.com/lilie.
