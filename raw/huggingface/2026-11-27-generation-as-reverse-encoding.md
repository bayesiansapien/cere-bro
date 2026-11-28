---
source: farmer/huggingface
farmed: 2026-11-28T10:45:04+05:30
arxiv_id: 2611.34782
url: https://huggingface.co/papers/2611.34782
arxiv_url: https://arxiv.org/abs/2611.34782
date: 2026-11-27
---

# Generation as Reverse Encoding

Pretrained visual representations accelerate generative learning by abstracting away appearance and spatial detail. Yet the same abstraction makes the return to pixels far harder, shifting much of the burden onto a larger decoder. We ask why the representation-to-pixel path should be learned independently when the encoder already provides a learned pixel-to-semantics path (the semantic encoding path). We introduce RevFlow, based on the principle of generation as reverse encoding. RevFlow uses intermediate representations of a frozen encoder as successive generative targets, first generating deep semantic representations, then shallow representations that retain appearance and spatial detail, before decoding to pixels. To learn these transitions without training a separate generator for each stage, we develop HyC-DiT, a unified generative model with a standard DiT backbone shared across stages and stage-specific condition injection. We further show that native matching in semantic representation space enables few-step generation. RevFlow accelerates both learning and sampling. On ImageNet 256 times 256, RevFlow reaches 1.96 FID at 690M and 1.74 FID at 1.55B after only 5 training epochs. It also achieves 30.25 dB reconstruction PSNR with an 89M decoder. After a short native-matching adaptation phase, RevFlow-XL achieves 2.85 FID using a single sampling step in each stage. Our code repository is at https://github.com/ChengShiest/RevFlow
