---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2603.20340
category: cs.AI
concept: agents-tool-use
url: https://arxiv.org/abs/2603.20340
published: 2026-04-16
authors: Zijian Lu, Yiping Zuo, Yupeng Nie
---

# ContractSkill: Repairable Contract-Based Skills for Multimodal Web Agents

**arXiv:** https://arxiv.org/abs/2603.20340
**Authors:** Zijian Lu, Yiping Zuo, Yupeng Nie

## Abstract

arXiv:2603.20340v3 Announce Type: replace-cross  Abstract: Self-generated skills for web agents are often unstable and can even hurt performance relative to direct acting. We argue that the key bottleneck is not only skill generation quality, but the fact that web skills remain implicit and therefore cannot be checked or locally repaired. To address this, we present ContractSkill, a framework that converts a draft skill into an executable artifact with explicit procedural structure, enabling deterministic verifica tion, fault localization, and minimal local repair. This turns skill refinement from full rewriting into localized editing of a single skill artifact. Experiments on VisualWebArena show that Contract Skill is effective in realistic web environments, while MiniWoB provides a controlled test of the mechanism behind the gain. Under matched transfer layers, repaired artifacts also remain reusable after removing the source model from the loop, providing evi dence of portability within the same benchmark family rather than full-benchmark generalization. These results suggest that the central challenge is not merely generating skills, but mak ing them explicit, executable, and repairable. Code is available at https://github.com/underfitting-lu/contractskill.git.
