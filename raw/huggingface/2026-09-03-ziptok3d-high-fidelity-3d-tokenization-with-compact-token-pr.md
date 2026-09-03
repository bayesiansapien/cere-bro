---
source: farmer/huggingface
farmed: 2026-09-03T17:01:45.591071
arxiv_id: 2609.01740
url: https://huggingface.co/papers/2609.01740
arxiv_url: https://arxiv.org/abs/2609.01740
date: 2026-09-03
---

# ZipTok3D: High-Fidelity 3D Tokenization with Compact Token Prefixes

Compact token sequences are essential for efficient 3D generation. However, existing 3D tokenizers typically organize latent representations either over spatial regions or as fixed-size sets of global tokens, both suffering sharp reconstruction degradation when compressed to extremely low token budgets. In this paper, we present ZipTok3D, a 3D tokenizer designed for high-fidelity reconstruction from extremely short token sequences. Its key idea is to organize object geometry into progressively informative global-token prefixes and unfold these compact representations through iterative decoding. Specifically, nested dropout randomly truncates the latent sequence after encoding during training and requires each retained prefix to reconstruct the complete object, thereby prioritizing essential geometric information in the leading tokens. The decoder then repeatedly applies a parameter-shared Transformer block to recover fine-grained geometry from each prefix without a separate generative sampling stage. With the same token dimension, ZipTok3D achieves reconstruction quality comparable to the 32-token COD-VAE baseline using only one token on ShapeNet and four on TRELLIS, yielding 32times and 8times shorter token sequences, respectively.
