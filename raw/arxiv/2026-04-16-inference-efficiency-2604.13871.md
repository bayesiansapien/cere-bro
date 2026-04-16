---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13871
category: cs.LG
concept: inference-efficiency
url: https://arxiv.org/abs/2604.13871
published: 2026-04-16
authors: Eymen Ipek
---

# Hardware-Efficient Neuro-Symbolic Networks with the Exp-Minus-Log Operator

**arXiv:** https://arxiv.org/abs/2604.13871
**Authors:** Eymen Ipek

## Abstract

arXiv:2604.13871v1 Announce Type: new  Abstract: Deep neural networks (DNNs) deliver state-of-the-art accuracy on regression and classification tasks, yet two structural deficits persistently obstruct their deployment in safety-critical, resource-constrained settings: (i) opacity of the learned function, which precludes formal verification, and (ii) reliance on heterogeneous, library-bound activation functions that inflate latency and silicon area on edge hardware. The recently introduced Exp-Minus-Log (EML) Sheffer operator, eml(x, y) = exp(x) - ln(y), was shown by Odrzywolek (2026) to be sufficient - together with the constant 1 - to express every standard elementary function as a binary tree of identical nodes. We propose to embed EML primitives inside conventional DNN architectures, yielding a hybrid DNN-EML model in which the trunk learns distributed representations and the head is a depth-bounded, weight-sparse EML tree whose snapped weights collapse to closed-form symbolic sub-expressions. We derive the forward equations, prove computational-cost bounds, analyse inference and training acceleration relative to multilayer perceptrons (MLPs) and physics-informed neural networks (PINNs), and quantify the trade-offs for FPGA/analog deployment. We argue that the DNN-EML pairing closes a literature gap: prior neuro-symbolic and equation-learner approaches (EQL, KAN, AI-Feynman) work with heterogeneous primitive sets and do not exploit a single hardware-realisable Sheffer element. A balanced assessment shows that EML is unlikely to accelerate training, and on commodity CPU/GPU it is also unlikely to accelerate inference; however, on a custom EML cell (FPGA logic block or analog circuit) the asymptotic latency advantage can reach an order of magnitude with simultaneous gain in interpretability and formal-verification tractability.
