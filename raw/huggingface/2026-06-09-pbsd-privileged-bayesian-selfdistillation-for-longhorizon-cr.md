---
source: farmer/huggingface
farmed: 2026-06-09T11:13:01Z
arxiv_id: 2606.09348
url: https://huggingface.co/papers/2606.09348
arxiv_url: https://arxiv.org/abs/2606.09348
date: 2026-06-09
---

# PBSD: Privileged Bayesian Self-Distillation for Long-Horizon Credit Assignment

Long-horizon agentic tasks pose a fundamental credit assignment challenge for outcome-base reinforcement learning: trajectory-level rewards verify final correctness but provide limited guidance on which intermediate reasoning steps or tool interactions contribute to the outcome. The difficulty is especially pronounced in multi-turn search agents, where successful trajectories may contain misleading actions and failed trajectories may contain valuable evidence-gathering steps. We propose PBSD (Privileged Bayesian Self-Distillation), a Bayes-calibrated self-distillation method for fine-grained credit assignment under sparse final rewards. PBSD measures trajectory quality through the posterior-to-prior probability ratio of the verified answer and applies Bayes' rule to convert this hard-to-estimate answer-side ratio into a tractable likelihood ratio between a standard student model and a privileged answer-conditioned teacher model. Autoregressive decomposition of this Bayesian evidence score yields turn-level signals that identify whether each intermediate turn supports or undermines the verified outcome. Consequently, PBSD provides a principled and elegant reweighting scheme that transforms sparse outcome supervision into Bayes-calibrated turn-level credit signals, while remaining fully compatible with standard policy optimization. Experiments demonstrate that PBSD consistently enhances performance across both in-domain and out-of-domain settings, and effectively transfers knowledge from short-context training to long-context inference, suggesting that its fine-grained credit assignment mechanism facilitates more effective policy learning and yields improved generalization.
