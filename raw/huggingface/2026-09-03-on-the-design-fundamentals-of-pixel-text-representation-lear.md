---
source: farmer/huggingface
farmed: 2026-09-03T17:01:45.591071
arxiv_id: 2609.01147
url: https://huggingface.co/papers/2609.01147
arxiv_url: https://arxiv.org/abs/2609.01147
date: 2026-09-03
---

# On the Design Fundamentals of Pixel Text Representation Learning

Text-rich visual inputs require models that can read, retrieve, and compress language directly in pixel space, yet existing pixel-text encoders struggle with fixed resolution pretraining, visual shortcut learning, weak visual grounding, and multilingual visual text understanding. In this work, we investigate the fundamental design principles required for robust visual text representation learning. Through systematic controlled ablations, we identify four critical components: variable image resolutions and rendered font sizes provide spatial proxies for high-resolution document generalization; natural image-text pairs are indispensable for grounding and prevent text-only collapse; layout-aware rendering helps prevent pixel-level shortcuts; and a two-stage multilingual curriculum enables effective cross-lingual alignment. By integrating these principles into a scalable training recipe, we train Pixel Linguist II, a native-resolution vision encoder trained with on-the-fly rendering, unified contrastive grounding, and a multilingual curriculum over 280M training examples. Pixel Linguist II sets new state-of-the-art results on English, cross-lingual, and multilingual Visual STS and ViDoRe, while also enabling better MLLM downstream evaluation. Notably, Pixel Linguist II remains robust under 80\% visual token compression, showing great promise for optical context compression. Our code and resources are available at https://github.com/Pixel-Linguist/Pixel-Linguist-II.
