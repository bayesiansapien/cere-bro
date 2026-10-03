---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.821239+00:00
arxiv_id: 2610.00686
url: https://huggingface.co/papers/2610.00686
arxiv_url: https://arxiv.org/abs/2610.00686
date: 2026-10-02
---

# SemanTok: Predictable Semantic Tokens for Efficient Autoregressive Video Generation

Recent video-based world models pair the scalability of autoregressive (AR) prediction with the visual quality of diffusion models. The choice of scene tokenizer is paramount for the optimal performance of each of these, both in terms of fidelity and semantics. Flexible-length, coarse-to-fine tokenizers yield exactly that: the first coarse tokens carry the clip's global semantics while later tokens further specify details. Existing flexible tokenizers only apply a representation-alignment (REPA) loss on early decoder hidden states, a target the decoder can partly meet from its noised input instead. We introduce SemanTok, a flexible video tokenizer that feeds frozen DINO features into its encoder and adds lightweight heads that reconstruct them from each retained token prefix alone. SemanTok achieves high semantic alignment and video fidelity at every AR model size: a 201M SemanTok AR model matches or beats a VideoFlexTok AR model 3.4times its size, and larger SemanTok AR models further improve fidelity. It keeps semantic alignment on out-of-distribution classes and gives the decoder higher semantic alignment at every noise level, including pure noise. It performs well in both reconstruction and generation, and its short token prefixes are cheaper to predict and give better generation fidelity, with pixel detail deferred to later tokens.
