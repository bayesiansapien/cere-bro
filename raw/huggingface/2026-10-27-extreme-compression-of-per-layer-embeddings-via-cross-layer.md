---
source: farmer/huggingface
farmed: 2026-10-28T10:37:11+05:30
arxiv_id: 2610.31309
url: https://huggingface.co/papers/2610.31309
arxiv_url: https://arxiv.org/abs/2610.31309
date: 2026-10-27
---

# Extreme Compression of Per-Layer Embeddings via Cross-Layer Latent Vector Quantization

Scaling embedding capacity alongside Transformer computation is an emerging trend in language models. This trend makes high compression rates increasingly useful. Hence, we study extreme compression of Per-Layer Embeddings (PLE), which follow this trend and account for 35.2% of the parameters of Gemma 4 E4B. At such rates, conventional quantizers give each token-layer vector its own code of only a few bytes. We instead develop OPTIC (Output-Path-fitted, Token-shared Indexed Codes), which stores one quantized code tuple per token and decodes it at every layer with a layer-specific affine decoder. Codes and decoders are fitted to the PLE output path rather than to the stored vectors. At about 100times PLE compression of bfloat16 (BF16) E4B, OPTIC retains an aggregate 97.8% of the uncompressed model's performance across seven benchmarks, whereas product quantization, the strongest of six conventional baselines, retains 66.3%. At 594times and 1,002times PLE compression of BF16 E4B, OPTIC retains 90.5% and 84.1%. On the official E4B release with 4-bit linear weights and 16-bit activations (W4A16), OPTIC retains 96.9% at about 100times PLE compression. During inference at about 100times PLE compression, BF16 E4B uses 29.7% less GPU memory than with uncompressed PLE at the same key-value cache size, while running at most 0.40% slower.
