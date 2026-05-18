---
source: farmer/huggingface
farmed: 2026-05-18T04:19:52Z
arxiv_id: 2605.14333
url: https://huggingface.co/papers/2605.14333
arxiv_url: https://arxiv.org/abs/2605.14333
date: 2026-05-18
---

# InsightTok: Improving Text and Face Fidelity in Discrete Tokenization for Autoregressive Image Generation

Text and faces are among the most perceptually salient and practically important patterns in visual generation, yet they remain challenging for autoregressive generators built on discrete tokenization. A central bottleneck is the tokenizer: aggressive downsampling and quantization often discard the fine-grained structures needed to preserve readable glyphs and distinctive facial features. We attribute this gap to standard discrete-tokenizer objectives being weakly aligned with text legibility and facial fidelity, as these objectives typically optimize generic reconstruction while compressing diverse content uniformly. To address this, we propose InsightTok, a simple yet effective discrete visual tokenization framework that enhances text and face fidelity through localized, content-aware perceptual losses. With a compact 16k codebook and a 16x downsampling rate, InsightTok significantly outperforms prior tokenizers in text and face reconstruction without compromising general reconstruction quality. These gains consistently transfer to autoregressive image generation in InsightAR, producing images with clearer text and more faithful facial details. Overall, our results highlight the potential of specialized supervision in tokenizer training for advancing discrete image generation.
