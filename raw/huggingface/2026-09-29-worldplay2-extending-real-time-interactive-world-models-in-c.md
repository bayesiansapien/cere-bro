---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.929842+00:00
arxiv_id: 2609.35560
url: https://huggingface.co/papers/2609.35560
arxiv_url: https://arxiv.org/abs/2609.35560
date: 2026-09-29
---

# WorldPlay2: Extending Real-Time Interactive World Models in Control and Horizon

Interactive world models require responding in real time to versatile controls and maintaining long-horizon consistency. However, modeling heterogeneous controls remains difficult, while explosive contexts and unstable distillation impede achieving both long-horizon consistency and real-time responsiveness. In this paper, we present WorldPlay2, an interactive world model that couples a factorized hybrid control interface with a co-design of compressed memory and stable distillation. 1) Our factorized hybrid control interface integrates frame-aligned action control with structured semantic control that explicitly disentangles scene appearance, character identity, and dynamic semantic events, thereby facilitating effective control learning. 2) To achieve efficient long-horizon modeling, we compress historical contexts into compact memory tokens shared by the autoregressive student and the bidirectional teacher. This design enables clip-wise, memory-conditioned score evaluation instead of jointly processing an entire long rollout, substantially reducing distillation overhead. 3) We further propose Stable Forcing, which initializes the autoregressive student via a few-step strategy and leverages full-rollout replay to preserve the quality of long-horizon rollouts, ensuring robust and stable distillation. Extensive experiments demonstrate the strong generalizability of our model and its superior performance compared to existing methods.
