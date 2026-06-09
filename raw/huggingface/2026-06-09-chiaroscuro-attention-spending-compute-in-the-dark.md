---
source: farmer/huggingface
farmed: 2026-06-09T16:28:21
arxiv_id: 2606.08327
url: https://huggingface.co/papers/2606.08327
arxiv_url: https://arxiv.org/abs/2606.08327
date: 2026-06-09
---

# Chiaroscuro Attention: Spending Compute in the Dark

Standard transformers apply self-attention uniformly at every layer and token, regardless of whether the input requires dynamic cross-token interaction. We propose CHIAR-Former (Chiaroscuro Attention), a 4-layer hybrid transformer that routes each token to one of three operators - DCT spectral mixing, RBF kernel mixing, or full self-attention - based on per-token spectral entropy, a theoretically justified complexity signal. Through systematic ablation on WikiText-103, we discover routing collapse: the router consistently rejects RBF in favour of DCT and attention, revealing that spectral mixing and dynamic attention are complementary and sufficient. A purpose-designed DCT+Attention-only variant achieves Val PPL 36.54 on WikiText-103 - a 45% improvement over a full-attention baseline (PPL 66.62) at 62.5% fewer attention FLOPs. We extend evaluation to WikiText-2, IMDB sentiment classification, and synthetic ListOps operations, establishing a clear operating regime: CHIAR-Former excels on large-scale naturalistic text where token diversity supports spectral specialisation, while full attention retains an edge on small datasets and synthetic pattern-matching tasks. These findings - both the wins and the losses - together define when and why spectral routing earns its keep.
