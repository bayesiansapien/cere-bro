---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13546
category: cs.LG
concept: inference-efficiency
url: https://arxiv.org/abs/2604.13546
published: 2026-04-16
authors: Yongil Choi
---

# Learning Inference Concurrency in DynamicGate MLP Structural and Mathematical Justification

**arXiv:** https://arxiv.org/abs/2604.13546
**Authors:** Yongil Choi

## Abstract

arXiv:2604.13546v1 Announce Type: new  Abstract: Conventional neural networks strictly separate learning and inference because if parameters are updated during inference, outputs become unstable and even the inference function itself is not well defined [1, 2, 3]. This paper shows that DynamicGate MLP structurally permits learning inference concurrency [4, 5]. The key idea is to separate routing (gating) parameters from representation (prediction) parameters, so that the gate can be adapted online while inference stability is preserved, or weights can be selectively updated only within the inactive subspace [4, 5, 6, 7]. We mathematically formalize sufficient conditions for concurrency and show that even under asynchronous or partial updates, the inference output at each time step can always be interpreted as a forward computation of a valid model snapshot [8, 9, 10]. This suggests that DynamicGate MLP can serve as a practical foundation for online adaptive and on device learning systems [11, 12].
