---
source: farmer/huggingface
farmed: 2026-09-03T17:01:45.591071
arxiv_id: 2609.01657
url: https://huggingface.co/papers/2609.01657
arxiv_url: https://arxiv.org/abs/2609.01657
date: 2026-09-03
---

# NeoMME: A Single-Tower Multimodal-Native Multilingual Foundation Encoder for Efficient Fine-Tuning and Inference

Multimodal models often build on architectures designed for generative vision-language modeling, typically combining separately pretrained vision encoders with causal language models. Visual document retrievers such as ColPali repurpose these models as encoders, carrying over the parameter and compute overhead of a VLM for a non-generative task.
  We introduce NeoMME, a family of 260M and 800M-parameter Multimodal and Multilingual bidirectional Encoders that process multilingual text and raw image patches in a single bidirectional Transformer encoder. Both models are pretrained from scratch with a masked discrete-diffusion text objective, conditioned on visible image patches for multimodal examples. Both support a 16,384-token context, enough to encode up to two standard 4K UHD images.
  To demonstrate its downstream capabilities, we fine-tune NeoMME with jointly trained dense and late-interaction heads. On the ViDoRe v3 benchmark, the resulting NeoMME-Retriever 260M outperforms all evaluated models strictly below 800M parameters with 0.523 nDCG@10, while NeoMME-Retriever 800M reaches 0.556. At a matched 2048x2048 image input size on an NVIDIA L40S, NeoMME-260M encodes pages with about 2x the throughput of ColModernVBERT. Hierarchical token pooling and asymmetric quantization compress late-interaction multimodal document embeddings by 255x while preserving over 95% of baseline nDCG@10. We contribute NeoMME to Hugging Face Transformers and release the pretrained backbone and retrieval-compatible checkpoints under Apache 2.0 at https://hf.co/collections/Hcompany/neomme.
