---
source: farmer/huggingface
farmed: 2026-11-06T05:50:41.297024+00:00
arxiv_id: 2611.06728
url: https://huggingface.co/papers/2611.06728
arxiv_url: https://arxiv.org/abs/2611.06728
date: 2026-11-05
---

# Turns Matter: Advancing Streaming Video RL via Turn-Level Credit

Streaming video understanding requires models to repeatedly decide whether to respond or continue observing. Recently, Group Relative Policy Optimization (GRPO) has been applied to this setting, with existing approaches emphasizing reward design while retaining a single trajectory-level advantage across turns. Such shared credit can reinforce redundant replies after earlier successes and discourage useful follow-ups after earlier failures. We propose TurnWise, a turn-level GRPO framework that aligns learning with individual streaming decisions. TurnWise addresses the mismatch between trajectory-level feedback and turn-level interaction, promoting informative responses and reducing redundancy. Specifically, turn-level credit assignment uses silence-completed prefix scoring to construct group-relative advantages from each decision's remaining return, separating its learning signal from earlier rewards. Turn-mean policy optimization averages token losses within each turn and then across turns, giving response and waiting decisions equal weight regardless of output length. These complementary designs improve streaming policy learning without a learned critic or additional rollouts. Extensive experiments show our method outperforms prior RL approaches for streaming video understanding.
