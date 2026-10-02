---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.352643+05:30
arxiv_id: 2609.35928
url: https://huggingface.co/papers/2609.35928
arxiv_url: https://arxiv.org/abs/2609.35928
date: 2026-10-01
---

# Prompted Identity Degrades Cooperation in Multi-Agent LLM Systems

Multi-agent LLM systems increasingly mix models from several providers, yet exposing each agent's underlying model identity to its peers significantly impairs cooperation. We show that when agents are aware of each other's model family, the group splits into clusters, where agents prefer interacting with others carrying their same label, although nothing in the task rewards or asks for such a split. We argue that the label itself causes this split, which we define as factionalism. We show and measure this phenomenon in two cooperative games and on a reasoning benchmark, with nine to twenty-five agents drawn from up to five open-weight model families. We further show that when the announced families are shuffled, or replaced by arbitrary labels, the factions still follow this information; when the label is removed, this behavior disappears. In strictly cooperative tasks, labeled groups spend on average 30% more rounds and 55% more tokens to reach a decision, and their success rate drops from 96% to 81%. The effect replicates across tasks, group sizes and model families. Withholding identity labels from the agents is simple and effective mitigation.
