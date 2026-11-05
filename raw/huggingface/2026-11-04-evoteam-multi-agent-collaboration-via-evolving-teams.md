---
source: farmer/huggingface
farmed: 2026-11-05T20:36:55.360997+05:30
arxiv_id: 2610.39813
url: https://huggingface.co/papers/2610.39813
arxiv_url: https://arxiv.org/abs/2610.39813
date: 2026-11-04
---

# EvoTeam: Multi-Agent Collaboration via Evolving Teams

LLM-based multi-agent systems (MAS) rely on collaboration among specialized agents to solve complex tasks. Existing methods improve MAS by refining the prompts, skills, and execution strategies of individual agents based on task feedback. However, improving individual agents does not necessarily lead to better team collaboration. Recent studies have therefore extended evolution to the collaboration level, using collective execution experience to adjust team organization, and inter-agent interactions. Nevertheless, evolving collaboration across heterogeneous tasks remains challenging, as existing approaches often constrain team reorganization within a shared structure and reuse interaction rules across incompatible team contexts. In this paper, we propose EvoTeam, a collaboration-centric evolution framework that jointly evolves team organization, interaction rules, and individual agent skills through execution experience. It maintains a library of reusable teams, selecting or creating agent teams and guiding collaboration through team-specific interaction rules. Collaboration experience accumulates within compatible team contexts, while individual skills remain reusable across teams. Experiments across four benchmarks demonstrate its effectiveness. Our code is available at https://github.com/DEEP-JLU/EvoTeam.
