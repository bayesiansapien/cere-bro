---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2509.21823
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2509.21823
published: 2026-04-16
authors: Gaole Dai, Shiqi Jiang, Ting Cao
---

# ProRe: A Proactive Reward System for GUI Agents via Reasoner-Actor Collaboration

**arXiv:** https://arxiv.org/abs/2509.21823
**Authors:** Gaole Dai, Shiqi Jiang, Ting Cao

## Abstract

arXiv:2509.21823v2 Announce Type: replace  Abstract: Reward is critical to the evaluation and training of large language models (LLMs). However, existing rule-based or model-based reward methods struggle to generalize to GUI agents, where access to ground-truth trajectories or application databases is often unavailable, and static trajectory-based LLM-as-a-Judge approaches suffer from limited accuracy. To address these challenges, we propose ProRe, a proactive reward system that leverages a general-purpose reasoner and domain-specific evaluator agents (actors). The reasoner schedules targeted state probing tasks, which the evaluator agents then execute by actively interacting with the environment to collect additional observations. This enables the reasoner to assign more accurate and verifiable rewards to GUI agents. Empirical results on over 3K trajectories demonstrate that ProRe improves reward accuracy and F1 score by up to 5.3\% and 19.4\%, respectively. Furthermore, integrating ProRe with state-of-the-art policy agents yields a success rate improvement of up to 22.4\%. The source code is available at https://github.com/V-Droid-Agent/ProRe.
