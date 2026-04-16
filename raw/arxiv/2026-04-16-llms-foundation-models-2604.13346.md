---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13346
category: cs.CL
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13346
published: 2026-04-16
authors: Pengcheng Wang, Jerry Huang, Jiarui Yao
---

# AgentSPEX: An Agent SPecification and EXecution Language

**arXiv:** https://arxiv.org/abs/2604.13346
**Authors:** Pengcheng Wang, Jerry Huang, Jiarui Yao

## Abstract

arXiv:2604.13346v1 Announce Type: new  Abstract: Language-model agent systems commonly rely on reactive prompting, in which a single instruction guides the model through an open-ended sequence of reasoning and tool-use steps, leaving control flow and intermediate state implicit and making agent behavior potentially difficult to control. Orchestration frameworks such as LangGraph, DSPy, and CrewAI impose greater structure through explicit workflow definitions, but tightly couple workflow logic with Python, making agents difficult to maintain and modify. In this paper, we introduce AgentSPEX, an Agent SPecification and EXecution Language for specifying LLM-agent workflows with explicit control flow and modular structure, along with a customizable agent harness. AgentSPEX supports typed steps, branching and loops, parallel execution, reusable submodules, and explicit state management, and these workflows execute within an agent harness that provides tool access, a sandboxed virtual environment, and support for checkpointing, verification, and logging. Furthermore, we provide a visual editor with synchronized graph and workflow views for authoring and inspection. We include ready-to-use agents for deep research and scientific research, and we evaluate AgentSPEX on 7 benchmarks. Finally, we show through a user study that AgentSPEX provides a more interpretable and accessible workflow-authoring paradigm than a popular existing agent framework.
