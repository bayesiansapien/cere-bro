---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.308018+05:30
arxiv_id: 2610.10497
url: https://huggingface.co/papers/2610.10497
arxiv_url: https://arxiv.org/abs/2610.10497
date: 2026-10-08
---

# QuadTok: Quadtree Visual Tokenizer for Autoregressive Image Generation

We introduce QuadTok, a novel framework for visual tokenization and autoregressive image generation. Compared to traditional approaches using 2D grids or 1D token sequences, we propose a hierarchical quadtree structure, bridging the gap between 2D spatial binding and 1D sequence-level flexibility. The QuadTok tokenizer dynamically allocates representational capacity to visually intricate areas while leaving homogeneous regions at a coarse resolution. Compared with a fixed 256-token grid, our ImageNet-trained tokenizer saves approximately 10% of tokens on ImageNet and 9% when transferred zero-shot to the COCO dataset, while maintaining comparable reconstruction fidelity. Furthermore, the natural causality introduced by the tree structure seamlessly enables autoregressive image generation. Conditioned on a quadtree topology supplied before generation, our 947M GPT-style generative model achieves a 2.08 gFID on the ImageNet 256 times 256 benchmark. Additionally, leveraging the strong spatial correlation preserved by the quadtree structure, the QuadTok generator enables zero-shot spatially controlled image generation capabilities. Code: https://github.com/myc634/QuadTok.
