---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13627
category: cs.LG
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13627
published: 2026-04-16
authors: Mark Rofin, Aditya Varre, Nicolas Flammarion
---

# (How) Learning Rates Regulate Catastrophic Overtraining

**arXiv:** https://arxiv.org/abs/2604.13627
**Authors:** Mark Rofin, Aditya Varre, Nicolas Flammarion

## Abstract

arXiv:2604.13627v1 Announce Type: new  Abstract: Supervised fine-tuning (SFT) is a common first stage of LLM post-training, teaching the model to follow instructions and shaping its behavior as a helpful assistant. At the same time, SFT may harm the fundamental capabilities of an LLM, particularly after long pretraining: a phenomenon known as catastrophic overtraining (Springer et al., 2025). To understand overtraining, we first investigate catastrophic forgetting in finetuning through the lens of implicit regularization of the learning rate. For models trained to the same SFT loss, we identify how the learning rate mediates optimization: finetuning with large and small steps converges to qualitatively different models. Next, we link forgetting to overtraining: learning rate decay increases the sharpness of the pretrained model, which in turn exacerbates catastrophic forgetting during SFT, leading to overtraining. Our findings paint a picture of the overtraining mechanism in LLMs and broadly contribute to the understanding of the interplay between optimization dynamics during pretraining and finetuning.
