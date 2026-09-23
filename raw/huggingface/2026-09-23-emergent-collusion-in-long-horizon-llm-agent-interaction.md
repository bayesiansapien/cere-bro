---
source: farmer/huggingface
farmed: 2026-09-23T14:55:25.993402
arxiv_id: 2609.24967
url: https://huggingface.co/papers/2609.24967
arxiv_url: https://arxiv.org/abs/2609.24967
date: 2026-09-23
---

# Emergent Collusion in Long-Horizon LLM Agent Interaction

LLM agents are increasingly deployed in collaborative settings, yet long-term interaction may give rise to undesirable coordination. We study the emergence of collusion in a long-horizon multi-agent environment: two agents repeatedly complete individual tasks, share task logs, verify each other's work, and receive rewards. We introduce realistic constraints that make compliance with the verification protocol incompatible with reward maximization, and find that agents increasingly deviate from the protocol over repeated interactions. Collusion emerges in 94% of trajectories across 10 models, and more capable models within the same family reach it earlier. Controlled peer interventions show that collusion is shaped by peer behavior, while ablations reveal additional effects of reward structure, the verification feedback agents receive, and their interaction history. In particular, restricting the amount and scope of interaction history available to agents reduces collusion. Overall, our findings show that long-horizon interaction can reshape how agents coordinate in ways that create safety risks.
