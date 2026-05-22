---
source: farmer/huggingface
farmed: 2026-05-22T10:21:55.060746+00:00
arxiv_id: 2605.16787
url: https://huggingface.co/papers/2605.16787
arxiv_url: https://arxiv.org/abs/2605.16787
date: 2026-05-21
---

# The Unlearnability Phenomenon in RLVR for Language Models

Reinforcement Learning with Verifiable Reward (RLVR) has proven effective in improving Large Language Model's (LLM) reasoning ability. However, the learning dynamics of RLVR remain underexplored. In this paper, we reveal a counterintuitive phenomenon: among hard examples that the model initially struggles with, a substantial subset remains unlearnable even when correct rollouts are present. To understand the phenomenon, we first demonstrate that existing optimization and sampling techniques fail to resolve unlearnability. With cross-example gradient analysis, we show that unlearnable examples have fundamental representation issue, characterized by low gradient similarity with the rest of the examples and ungeneralizable reasoning patterns. We further show that representation flaws are difficult to mitigate in RL, as data augmentation does not improve gradient similarity. Our study provides the first systematic characterization of unlearnable data in RLVR training and reveals fundamental limitations in current RL approaches for reasoning tasks. Code and data are available at https://github.com/yulinchen99/unlearnability-rlvr.
