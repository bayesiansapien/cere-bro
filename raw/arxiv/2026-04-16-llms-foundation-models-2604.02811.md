---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.02811
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.02811
published: 2026-04-16
authors: Lik Tung Fu, Jie Zhou, Shaokai Ren
---

# ChatSVA: Bridging SVA Generation for Hardware Verification via Task-Specific LLMs

**arXiv:** https://arxiv.org/abs/2604.02811
**Authors:** Lik Tung Fu, Jie Zhou, Shaokai Ren

## Abstract

arXiv:2604.02811v2 Announce Type: replace-cross  Abstract: Functional verification consumes over 50% of the IC development lifecycle, where SystemVerilog Assertions (SVAs) are indispensable for formal property verification and enhanced simulation-based debugging. However, manual SVA authoring is labor-intensive and error-prone. While Large Language Models (LLMs) show promise, their direct deployment is hindered by low functional accuracy and a severe scarcity of domain-specific data. To address these challenges, we introduce ChatSVA, an end-to-end SVA generation system built upon a multi-agent framework. At its core, the AgentBridge platform enables this multi-agent approach by systematically generating high-purity datasets, overcoming the data scarcity inherent to few-shot scenarios. Evaluated on 24 RTL designs, ChatSVA achieves 98.66% syntax and 96.12% functional pass rates, generating 139.5 SVAs per design with 82.50% function coverage. This represents a 33.3 percentage point improvement in functional correctness and an over 11x enhancement in function coverage compared to the previous state-of-the-art (SOTA). ChatSVA not only sets a new SOTA in automated SVA generation but also establishes a robust framework for solving long-chain reasoning problems in few-shot, domain-specific scenarios. An online service has been publicly released at https://www.nctieda.com/CHATDV.html.
