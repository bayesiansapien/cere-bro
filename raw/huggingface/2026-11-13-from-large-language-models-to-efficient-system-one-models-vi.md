---
source: farmer/huggingface
farmed: 2026-11-14T05:10:36.533816+00:00
arxiv_id: 2611.16321
url: https://huggingface.co/papers/2611.16321
arxiv_url: https://arxiv.org/abs/2611.16321
date: 2026-11-13
---

# From Large Language Models to Efficient System One Models via Adaptive Computation

Transferring LLMs into System One decision models typically replaces the language modeling head with a decision head while retaining the full backbone, making every decision pay for all layers. Yet it remains unclear how much depth such decisions require. We find that decision information is concentrated in intermediate layers, with early layers building essential features and the final six layers removable without loss, while independently trained smaller models largely mimic the full model rather than developing specialized decision capabilities. These findings suggest that efficiency requires not simply smaller backbones, but shared computation across different depths. Building on this, we propose , which jointly trains a full model with prefix sub-models that share its final layers and decision head through self-distillation. A lightweight gate reads the hidden state at each exit to determine whether additional computation is needed, allowing one model to operate at multiple layers. Across seven decision benchmarks, our approach matches or outperforms independently trained models at every depth, while achieving better accuracy-efficiency trade-offs through adaptive computation.
