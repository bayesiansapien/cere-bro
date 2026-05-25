---
source: farmer/huggingface
farmed: 2026-05-25T08:23:16Z
arxiv_id: 2605.17873
url: https://huggingface.co/papers/2605.17873
arxiv_url: https://arxiv.org/abs/2605.17873
date: 2026-05-25
---

# HINT-SD: Targeted Hindsight Self-Distillation for Long-Horizon Agents

Training long-horizon LLM agents with reinforcement learning is challenging because sparse outcome rewards reveal whether a task succeeds, but not which intermediate actions caused the outcome or how they should be corrected. Recent methods alleviate this issue by generating rewards or textual hints from turn-level action-output signals, or by using feedback-conditioned self-distillation. However, generating feedback at every turn is inefficient when many intermediate turns are already successful or neutral, and applying feedback at a fixed or misaligned turn often fails to supervise the actions that contributed to the failure. To bridge this gap, we propose HINT-SD, a targeted self-distillation framework that uses full-trajectory hindsight to select failure-relevant actions and applies feedback-conditioned distillation only on targeted action spans. Experiments on BFCL v3 and AppWorld show that our method improves over the dense per-turn feedback baseline by up to 18.80 percent while achieving 2.26times lower time per training step, suggesting that selecting where to distill is a key factor for both effective and efficient long-horizon agent training.
