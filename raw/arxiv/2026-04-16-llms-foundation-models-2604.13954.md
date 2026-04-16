---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13954
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13954
published: 2026-04-16
authors: Jiacheng Wang, Jinchang Hou, Fabian Wang
---

# HINTBench: Horizon-agent Intrinsic Non-attack Trajectory Benchmark

**arXiv:** https://arxiv.org/abs/2604.13954
**Authors:** Jiacheng Wang, Jinchang Hou, Fabian Wang

## Abstract

arXiv:2604.13954v1 Announce Type: cross  Abstract: Existing agent-safety evaluation has focused mainly on externally induced risks. Yet agents may still enter unsafe trajectories under benign conditions. We study this complementary but underexplored setting through the lens of \emph{intrinsic} risk, where intrinsic failures remain latent, propagate across long-horizon execution, and eventually lead to high-consequence outcomes. To evaluate this setting, we introduce \emph{non-attack intrinsic risk auditing} and present \textbf{HINTBench}, a benchmark of 629 agent trajectories (523 risky, 106 safe; 33 steps on average) supporting three tasks: risk detection, risk-step localization, and intrinsic failure-type identification. Its annotations are organized under a unified five-constraint taxonomy. Experiments reveal a substantial capability gap: strong LLMs perform well on trajectory-level risk detection, but their performance drops to below 35 Strict-F1 on risk-step localization, while fine-grained failure diagnosis proves even harder. Existing guard models transfer poorly to this setting. These findings establish intrinsic risk auditing as an open challenge for agent safety.
