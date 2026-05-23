---
source: farmer/huggingface
farmed: 2026-05-23T00:00:00Z
arxiv_id: 2605.21803
url: https://huggingface.co/papers/2605.21803
arxiv_url: https://arxiv.org/abs/2605.21803
date: 2026-05-23
---

# Same Architecture, Different Capacity: Optimizer-Induced Spectral Scaling Laws

Scaling laws have made language-model performance predictable from model size, data, and compute, but they typically treat the optimizer as a fixed training detail. We show that this assumption misses a fundamental axis of representation scaling: how effectively the optimizer converts added FFN width into utilized spectral capacity. Using eigenspectra of feed-forward network representations, measured through soft and hard spectral-ranks, we find that the same Transformer architecture realizes markedly different spectral scaling laws when trained with different optimizers. Holding architecture and width schedule fixed, AdamW exhibits weak hard-rank scaling (β=0.44) on rare-token (TAIL) representations where learning is known to be hardest, whereas Muon achieves linear scaling (β=1.02) in the same regimes, a 2.3times increase in the scaling exponent. This difference is not reducible to validation loss: AdamW configurations can match low-rank Dion variants in perplexity, under extended training, while exhibiting sharply different spectral geometry, demonstrating that matched loss does not imply matched representation structure. Hard--soft rank asymmetry further reveals that optimizers differ not only in how much capacity is realized, but also in how that capacity is structured across eigenmodes. To disentangle optimizer effects from architectural ones, we compare against architectural interventions (e.g., attention rank and positional encoding), and find that optimizer-induced spectral shifts often exceed the architectural effects. These results suggest optimization as a first-class axis of representation scaling, motivating optimizer--architecture co-design.
