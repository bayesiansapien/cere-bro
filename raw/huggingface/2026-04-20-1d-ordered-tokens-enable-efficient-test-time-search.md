---
source: farmer/huggingface
farmed: 2026-04-20T00:00:00
arxiv_id: 2604.15453
url: https://huggingface.co/papers/2604.15453
arxiv_url: https://arxiv.org/abs/2604.15453
date: 2026-04-20
---

# (1D) Ordered Tokens Enable Efficient Test-Time Search

Tokenization is a key component of autoregressive (AR) generative models, converting raw data into more manageable units for modeling. Commonly, tokens describe local information, such as regions of pixels in images or word pieces in text, and AR generation predicts these tokens in a fixed order. A worthwhile question is whether token structures affect the ability to steer the generation through test-time search, where multiple candidate generations are explored and evaluated by a verifier. Using image generation as our testbed, we hypothesize that recent 1D ordered tokenizers with coarse-to-fine structure can be more amenable to search than classical 2D grid structures. This is rooted in the fact that the intermediate states in coarse-to-fine sequences carry semantic meaning that verifiers can reliably evaluate, enabling effective steering during generation. Through controlled experiments, we find that AR models trained on coarse-to-fine ordered tokens exhibit improved test-time scaling behavior compared to grid-based counterparts. Moreover, we demonstrate that, thanks to the ordered structure, pure test-time search over token sequences (i.e., without training an AR model) can perform training-free text-to-image generation when guided by an image-text verifier. Beyond this, we systematically study how classical search algorithms (best-of-N, beam search, lookahead search) interact with different token structures, as well as the role of different verifiers and AR priors. Our results highlight the impact of token structure on inference-time scalability and provide practical guidance for test-time scaling in AR models.
