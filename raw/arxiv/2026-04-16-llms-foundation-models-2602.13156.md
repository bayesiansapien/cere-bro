---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2602.13156
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2602.13156
published: 2026-04-16
authors: Yiran Gao, Kim Hammar, Tao Li
---

# In-Context Autonomous Network Incident Response: An End-to-End Large Language Model Agent Approach

**arXiv:** https://arxiv.org/abs/2602.13156
**Authors:** Yiran Gao, Kim Hammar, Tao Li

## Abstract

arXiv:2602.13156v2 Announce Type: replace-cross  Abstract: Rapidly evolving cyberattacks demand incident response systems that can autonomously learn and adapt to changing threats. Prior work has extensively explored the reinforcement learning approach, which involves learning response strategies through extensive simulation of the incident. While this approach can be effective, it requires handcrafted modeling of the simulator and suppresses useful semantics from raw system logs and alerts. To address these limitations, we propose to leverage large language models' (LLM) pre-trained security knowledge and in-context learning to create an end-to-end agentic solution for incident response planning. Specifically, our agent integrates four functionalities, perception, reasoning, planning, and action, into one lightweight LLM (14b model). Through fine-tuning and chain-of-thought reasoning, our LLM agent is capable of processing system logs and inferring the underlying network state (perception), updating its conjecture of attack models (reasoning), simulating consequences under different response strategies (planning), and generating an effective response (action). By comparing LLM-simulated outcomes with actual observations, the LLM agent repeatedly refines its attack conjecture and corresponding response, thereby demonstrating in-context adaptation. Our agentic approach is free of modeling and can run on commodity hardware. When evaluated on incident logs reported in the literature, our agent achieves recovery up to 23% faster than those of frontier LLMs.
