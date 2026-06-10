---
source: farmer/huggingface
farmed: 2026-06-10T06:28:48Z
arxiv_id: 2606.09032
url: https://huggingface.co/papers/2606.09032
arxiv_url: https://arxiv.org/abs/2606.09032
date: 2026-06-10
---

# Bridging the Agent-World Gap: Text World Models for LLM-based Agents

Large language model (LLM)-based agents are increasingly used in interactive textual environments, from web navigation and code editing to tool use and long-horizon dialogue. Yet many remain largely reactive, mapping observations to actions without an explicit model of how these environments are structured and evolve. This motivates text world models (TWMs): transition models over textual states that, given a state and a candidate action, predict the resulting webpage, terminal output, API response, or user reply, thereby supporting planning, efficient learning, and principled evaluation. We systematically review text world models for LLM-based agents, organized around a formal framework and the agent lifecycle: (1) Foundations, defining text world models and characterizing them by state representation and grounding domain; (2) Construction, taxonomizing LLM-as-WM and code-as-WM paradigms and reviewing methods for building them; (3) Application, examining how world models support agents at training time through experience synthesis and at inference time through planning, verification, and adaptation; and (4) Evaluation, covering both evaluation of the world model itself and its use as an evaluation environment for agents. We aim to consolidate this rapidly developing area, clarify its design space, and highlight open challenges for future research.
