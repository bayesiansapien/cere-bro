---
source: farmer/huggingface
farmed: 2026-08-05T09:04:08.705882+00:00
arxiv_id: 2608.02713
url: https://huggingface.co/papers/2608.02713
arxiv_url: https://arxiv.org/abs/2608.02713
date: 2026-08-05
---

# Quo Vadis, World Modeling?

Continually improving agents require dynamic interaction feedback beyond static supervision, yet direct real-environment interaction is costly, slow, unsafe, and hard to parallelize. World modeling offers a natural intermediate proxy that allows agents to query lower-cost, more controllable feedback before committing to real actions. Classical world models instantiate this proxy primarily through future physical-state prediction, a formulation useful yet narrow for agents that require actionable feedback beyond raw state transitions. In this work, we conceptualize Agent-Centric Interactive World Proxies, shifting the fundamental paradigm from physical state transitions to agent-usable information transitions, such as execution outcomes, retrieved experiences or skills, and verification signals, broadening the scope of world modeling to provide versatile feedback for continually improving agents. To systematically map this design space, we organize world proxies into six functional forms based on their feedback modalities: dynamics, spatial, execution, memory/experience, skill, and reward/verification proxies, which together characterize the primary ways world modeling serves agent improvement. We further analyze how these proxies empower agents across three progressive levels: L.1 Inference-Time Guidance, where proxy outputs enrich in-context information for superior decisions; L.2 Training-Time Optimization, where proxy outputs yield rewards, critiques, or synthetic rollouts for policy learning; and L.3 Agent-Proxy Co-Evolution, where real-environment evidence continuously updates both the proxy and the agent for co-evolution. Ultimately, this work recasts world modeling into an agent-centric paradigm, establishing a roadmap for building world proxies that empower agents to plan better, learn faster, and evolve continually.
