---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.218209+05:30
arxiv_id: 2610.12978
url: https://huggingface.co/papers/2610.12978
arxiv_url: https://arxiv.org/abs/2610.12978
date: 2026-10-12
---

# Learning Representations to Guide Pixel Diffusion Transformers

Visual representations are largely developed for understanding, yet what makes them useful for generation remains unclear. We study this question in pixel diffusion transformers and uncover two key insights. First, better representation quality does not necessarily translate into greater generative utility, as externally aligned semantics can be progressively lost during pixel synthesis. Second, architectural separation with specialized pixel decoders mainly redistributes semantic and spatial modeling, without necessarily yielding representations better suited to generation. These insights suggest that a useful generative representation must be both properly formed and actively exploited. Motivated by these insights, we introduce Representation Guidance (RG), which directly forms and exploits internal representations while retaining a plain Transformer architecture. A low-dimensional bottleneck forces generation-relevant information into a compact representation, which is then explicitly used to guide decoder generation by modifying the flow-matching target according to its induced prediction offset. RG learns clearer semantic and spatial structure while scaling efficiently in both parameters and computation. On ImageNet 256x256, RG-L/16 with only 459M parameters outperforms substantially larger pixel diffusion transformers, while RG-XL/16 achieves an FID of 1.55. RG further reaches an FID of 1.74 at 512x512 and extends to text-to-image generation, achieving 0.89 on GenEval and 87.1 on DPG-Bench.
