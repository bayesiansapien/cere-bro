---
source: farmer/huggingface
farmed: 2026-09-03T17:01:45.591071
arxiv_id: 2609.00591
url: https://huggingface.co/papers/2609.00591
arxiv_url: https://arxiv.org/abs/2609.00591
date: 2026-09-03
---

# A Glance Is All You Need: Single-Pass Fine-Grained Image Captioning with SimLoss

An image may be worth a thousand words, but most captioning models describe it in only a few. Modern vision-language models produce fluent high-level captions, yet routinely miss the attributes, counts, textures, materials, and spatial relations that make an image visually specific. Recent multi-stage systems recover some of these details through generation, decomposition, verification, and rewriting, but they do so at the expense of substantially higher inference latency.
  We propose SimLoss, a reference-free embedding-space objective for single-pass fine-grained image captioning. SimLoss trains a vision-language model to align its projected hidden-state representation with a frozen image embedding through an InfoNCE contrastive loss, supplying a dense visual supervision signal before any text is decoded, and requiring neither human-written fine-grained captions nor pseudo-captions from a multi-stage pipeline. We instantiate it as SimLoss FFT, which backpropagates through a locally available embedding model, and SimLoss GRPO, which treats that model as a black-box reward.
  Compared with single-pass, multi-stage verification, reward-optimized, and perception-aware baselines, the fully differentiable fine-tuning variant, SimLoss FFT, achieves the highest precision while nearly matching the F1 score of the multi-stage method, all while retaining single-pass inference and running roughly 20 times faster than the multi-stage pipeline.
  The reward-based variant SimLoss GRPO attains the strongest recall. Together, these results show that embedding-space supervision can recover the quality of multi-stage verification at the latency of a single-pass captioner.
