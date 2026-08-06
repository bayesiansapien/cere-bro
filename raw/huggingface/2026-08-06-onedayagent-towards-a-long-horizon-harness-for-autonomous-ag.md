---
source: farmer/huggingface
farmed: 2026-08-06T10:35:34.247620Z
arxiv_id: 2608.05013
url: https://huggingface.co/papers/2608.05013
arxiv_url: https://arxiv.org/abs/2608.05013
date: 2026-08-06
---

# OneDayAgent: Towards a Long-Horizon Harness for Autonomous Agents

LLM agents are increasingly applied to open-ended everyday requests that span work, study, and life. These tasks are long-horizon, cross-environment, and multimodal, forcing the agent to preserve goals and constraints across many steps while navigating heterogeneous tools and attachments. While prior work has addressed individual failure modes such as goals drift, states loss, and context overflow, whether a single harness can manage them jointly and remain effective across backends has received less study. We present OneDayAgent, a long-horizon harness for autonomous agents. OneDayAgent turns an open-ended request into a managed execution process that decomposes tasks into bounded subtasks, maintains execution memory under context pressure, and verifies and repairs the final deliverable. We evaluate OneDayAgent on AgentIF-OneDay across 104 tasks. With the GLM-5.2 backend, OneDayAgent sets a new state of the art with an overall score of 0.821. The same harness runs across five backend LLMs from three model families, indicating the harness generalizes across backends without tuning, even as different models induce distinct execution styles under the same workflow.
