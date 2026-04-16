---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13151
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13151
published: 2026-04-16
authors: Jaden Park, Jungtaek Kim, Jongwon Jeong
---

# Exploration and Exploitation Errors Are Measurable for Language Model Agents

**arXiv:** https://arxiv.org/abs/2604.13151
**Authors:** Jaden Park, Jungtaek Kim, Jongwon Jeong

## Abstract

arXiv:2604.13151v1 Announce Type: new  Abstract: Language Model (LM) agents are increasingly used in complex open-ended decision-making tasks, from AI coding to physical AI. A core requirement in these settings is the ability to both explore the problem space and exploit acquired knowledge effectively. However, systematically distinguishing and quantifying exploration and exploitation from observed actions without access to the agent's internal policy remains challenging. To address this, we design controllable environments inspired by practical embodied AI scenarios. Each environment consists of a partially observable 2D grid map and an unknown task Directed Acyclic Graph (DAG). The map generation can be programmatically adjusted to emphasize exploration or exploitation difficulty. To enable policy-agnostic evaluation, we design a metric to quantify exploration and exploitation errors from agent's actions. We evaluate a variety of frontier LM agents and find that even state-of-the-art models struggle on our task, with different models exhibiting distinct failure modes. We further observe that reasoning models solve the task more effectively and show both exploration and exploitation can be significantly improved through minimal harness engineering. We release our code \href{https://github.com/jjj-madison/measurable-explore-exploit}{here}.
