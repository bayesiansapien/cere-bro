---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.352213+05:30
arxiv_id: 2609.18587
url: https://huggingface.co/papers/2609.18587
arxiv_url: https://arxiv.org/abs/2609.18587
date: 2026-10-01
---

# Label-free steering: Compressing test-time reinforcement learning into bias-only subspaces

Test-time reinforcement learning (TTRL) enables models to improve their reasoning without relying on labeled training data, but existing approaches typically optimize a large fraction of the model parameters. This raises a natural question: can effective test-time adaptation emerge when both the reward signal and the optimization space are severely restricted? We answer this question with label-free bias-only TTRL, which uses majority-vote pseudolabels as rewards and optimizes only ~100K bias parameters while keeping the pretrained backbone frozen. On MATH-500, our approach reaches 76.67% accuracy with Qwen2.5-7B, slightly exceeding our own labeled bias-steering reproduction while optimizing 76,000x fewer parameters than full-parameter TTRL. The same training procedure improves performance across vision-language and audio reasoning tasks, including MathVista, AI2D, LogicVista, and MMAU. We further show that the learned steering vectors transfer to 4,500 held-out MATH problems, indicating that the adaptation is not limited to the problems used during test-time optimization. Finally, we analyze why this highly restricted adaptation can work, showing that majority-vote reliability improves with rollout consensus and that bias subspaces with greater accessible gradient energy exhibit stronger downstream trainability. These results demonstrate that substantial test-time adaptation can emerge from optimizing a tiny bias-only subspace using entirely label-free rewards.
