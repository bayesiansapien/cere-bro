---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.05912
url: https://huggingface.co/papers/2610.05912
arxiv_url: https://arxiv.org/abs/2610.05912
date: 2026-10-07
---

# MiniCorp: The Last Mile of the AI Agent Firm

The last mile toward enterprise AGI is a company that runs itself. Training and adapting such agents require longitudinal enterprise data, which remain scarce, costly to acquire, and often restricted by privacy constraints. Historical archives are also frequently incomplete and record only what actually happened. They cannot show the outcomes of alternative decisions. We introduce MiniCorp, an office simulator for studying how agents can collectively run a company while generating enterprise data at scale. Using an e-commerce company as a demonstration, MiniCorp connects two interacting worlds. The external world models customers, dynamic competitors, and market mechanisms. The internal world consists of agents that observe events, discuss their options, and make strategic decisions. These decisions have lasting effects on the market, and the resulting feedback informs the firm's later decisions. As the firm and market interact, MiniCorp continuously records the agents' communications and decisions. These records preserve the information available at the time and the business results that followed. Checkpointing allows the same situation to be replayed under different decisions, providing comparisons unavailable in static archives. We evaluate end-to-end fidelity against patterns reported in empirical studies of real markets. These evaluations provide agents with realistic market feedback and reduce the risk that they learn to exploit flaws in the simulator. Our experiments show agents coordinating across roles and adapting their decisions to market feedback. With explicit long-term strategic guidance, they also sustain advertising exploration despite weak early returns. MiniCorp thus provides an environment for studying AI-run companies and a scalable source of longitudinal and counterfactual enterprise data for agent training and evaluation.
