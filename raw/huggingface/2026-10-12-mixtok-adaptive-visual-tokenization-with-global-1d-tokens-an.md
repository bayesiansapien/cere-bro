---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.221001+05:30
arxiv_id: 2610.13181
url: https://huggingface.co/papers/2610.13181
arxiv_url: https://arxiv.org/abs/2610.13181
date: 2026-10-12
---

# MixTok: Adaptive Visual Tokenization with Global 1D Tokens and Sparse 2D Refinement

Efficient visual tokenization requires balancing representation compactness with the preservation of fine-grained image content. Conventional grid-based tokenizers allocate tokens uniformly across spatial locations despite non-uniform visual complexity, whereas compact 1D tokenizers aggregate global information but can struggle to preserve local details. We introduce MixTok, a hybrid visual tokenizer that combines a compact 1D global representation with sparse 2D tokens for local refinement. A content-adaptive router ranks candidate locations by refinement priority and determines the number of 2D tokens for each image under a target average token budget. At the highest-scoring locations, 2D token features replace the spatial features recovered from the 1D representation, and a shared decoder reconstructs the image from the resulting mixed features. On ImageNet 256 x 256, MixTok achieves highly competitive reconstruction and generation performance, with an rFID of 1.195 and a gFID of 1.95 at respective average budgets of approximately 128 and 131 content tokens per image.
