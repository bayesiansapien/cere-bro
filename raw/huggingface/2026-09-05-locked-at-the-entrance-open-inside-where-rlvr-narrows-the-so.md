---
source: farmer/huggingface
farmed: 2026-09-05T10:14:12.541801+05:30
arxiv_id: 2608.29188
url: https://huggingface.co/papers/2608.29188
arxiv_url: https://arxiv.org/abs/2608.29188
date: 2026-09-05
---

# Locked at the Entrance, Open Inside: Where RLVR Narrows the Solution Space

Reinforcement learning with verifiable rewards (RLVR) substantially improves single-sample accuracy (pass@1) but causes the policy's solution space to contract, diminishing the returns of test-time scaling. In this work, we investigate where inside a reasoning trajectory this breadth is lost: does the policy fail to access a valid solution family, or does it fail to execute computation once initiated? To disentangle access from execution, we analyze the Countdown task, whose solution space can be exhaustively enumerated into discrete entrance families defined by the first operand and operator, across PPO on Qwen2.5-3B and GRPO on Qwen2.5-3B-Instruct. Across both training setups, solution coverage falls by up to 67%, halving even on problems solved across all checkpoints. We show that this contraction is heavily concentrated at the entrance: per-token likelihood shifts are 11x--16x larger prior to the first arithmetic operation than during downstream reasoning. Supplying only an unselected entrance prefix restores completion rates in low-access families by over an order of magnitude (0.018 -> 0.212 under PPO), demonstrating that alternative solutions remain executable but are no longer initiated. Guided by this localization, we find that while surface prompting fails to recover diversity, entrance-targeted interventions succeed: late-layer parameter interpolation with early checkpoints increases solution coverage by 37% at no loss in pass@1. Finally, we show that early-step entropy collapse recurs across six math benchmarks with 7B and 14B models, but is not an inevitable byproduct of reasoning optimization: an SFT baseline preserves more than double the coverage, and staged SFT--DPO--RLVR pipelines retain early-step entropy. In summary, reasoning breadth is lost at the door, not inside the room. Code: https://github.com/ershiyidian/early-branch-locking.
