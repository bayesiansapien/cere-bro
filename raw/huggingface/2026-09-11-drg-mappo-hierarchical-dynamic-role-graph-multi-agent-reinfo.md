---
source: farmer/huggingface
farmed: 2026-09-11T21:57:41.002444
arxiv_id: 2609.11155
url: https://huggingface.co/papers/2609.11155
arxiv_url: https://arxiv.org/abs/2609.11155
date: 2026-09-11
---

# DRG-MAPPO: Hierarchical Dynamic Role-Graph Multi-Agent Reinforcement Learning for Cooperative Air Combat

Multi-Agent Reinforcement Learning (MARL) has emerged as a pivotal paradigm for complex decision-making in autonomous systems and air combat. While MARL has demonstrated significant potential in air combat, achieving sophisticated tactical coordination remains a non-trivial challenge. This difficulty is largely attributed to two primary limitations: (1) the absence of structured relational modeling hinders agents from capturing complex, time-varying interactions among battlefield entities; and (2) conventional flat architectures often lack the capability to explicitly model tactical roles, leading to ambiguous task allocation in highly dynamic environments. To address these challenges, we propose Hierarchical Dynamic Role-Graph Multi-Agent Proximal Policy Optimization (DRG-MAPPO), a novel MARL framework that integrates graph-based relational modeling with dynamic role assignment. Specifically, DRG-MAPPO constructs a graph-based representation of battlefield interactions and leverages graph attention mechanisms to extract critical relational features among allies, enemies, and threats. Subsequently, a high-level policy employs a dynamic role assignment mechanism to determine tactical responsibilities (e.g., ``leader'' and ``supporter''). Conditioned on these roles and encoded graph-relational features, a low-level policy executes discrete maneuver actions, facilitating the joint optimization of tactical strategy and collaborative execution. Furthermore, a target-priority auxiliary task is designed to foster the emergence of behaviors such as focus-fire. Experimental results demonstrate that DRG-MAPPO achieves a state-of-the-art win rate of 87%, suggesting that our framework effectively balances relational modeling, interpretability, and optimization stability for cooperative air combat.
