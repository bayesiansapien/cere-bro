---
source: farmer/huggingface
farmed: 2026-07-27T13:15:36.767293
arxiv_id: 2607.12756
url: https://huggingface.co/papers/2607.12756
arxiv_url: https://arxiv.org/abs/2607.12756
date: 2026-07-27
---

# VisCo: Leveraging Large Language Models as Intrinsic Encoders for Visual Token Compression

Vision-language models (VLMs) process large numbers of visual tokens, resulting in substantial inference latency and memory overhead. This has motivated extensive research on visual token compression. While training-free strategies rely on heuristic metrics and suffer significant performance degradation under high compression ratios, many training-based methods introduce external compression modules that force the VLM backbone to adapt, incurring substantial retraining cost and compromising VLMs' priors. Effective visual token compression hinges on strong information encoding, a capability already present in pretrained VLMs but underutilized by existing approaches. Motivated by this, we propose VisCo, a training-efficient self-compression framework that reuses the pretrained VLM itself as an intrinsic compressor. VisCo is a parameter-sharing autoencoder that compresses visual information using a small set of memory tokens and transfers hierarchical information from encoding to decoding. Experiments show that VisCo surpasses prior methods across all evaluated compression ratios, with larger gains under more aggressive compression, and remains stable even in the extreme single-token setting. Moreover, when combined with the original visual tokens, the learned memory tokens can even improve the base model, suggesting that VisCo captures complementary representations beyond compression.
