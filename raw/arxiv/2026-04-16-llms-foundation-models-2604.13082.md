---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13082
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13082
published: 2026-04-16
authors: Laura Gomezjurado Gonzalez
---

# The Long Delay to Arithmetic Generalization: When Learned Representations Outrun Behavior

**arXiv:** https://arxiv.org/abs/2604.13082
**Authors:** Laura Gomezjurado Gonzalez

## Abstract

arXiv:2604.13082v1 Announce Type: cross  Abstract: Grokking in transformers trained on algorithmic tasks is characterized by a long delay between training-set fit and abrupt generalization, but the source of that delay remains poorly understood. In encoder-decoder arithmetic models, we argue that this delay reflects limited access to already learned structure rather than failure to acquire that structure in the first place. We study one-step Collatz prediction and find that the encoder organizes parity and residue structure within the first few thousand training steps, while output accuracy remains near chance for tens of thousands more. Causal interventions support the decoder bottleneck hypothesis. Transplanting a trained encoder into a fresh model accelerates grokking by 2.75 times, while transplanting a trained decoder actively hurts. Freezing a converged encoder and retraining only the decoder eliminates the plateau entirely and yields 97.6% accuracy, compared to 86.1% for joint training. What makes the decoder's job harder or easier depends on numeral representation. Across 15 bases, those whose factorization aligns with the Collatz map's arithmetic (e.g., base 24) reach 99.8% accuracy, while binary fails completely because its representations collapse and never recover. The choice of base acts as an inductive bias that controls how much local digit structure the decoder can exploit, producing large differences in learnability from the same underlying task.
