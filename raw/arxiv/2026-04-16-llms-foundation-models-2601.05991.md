---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2601.05991
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2601.05991
published: 2026-04-16
authors: Jiayu Ding, Haoran Tang, Hongbo Jin
---

# 3D Instruction Ambiguity Detection

**arXiv:** https://arxiv.org/abs/2601.05991
**Authors:** Jiayu Ding, Haoran Tang, Hongbo Jin

## Abstract

arXiv:2601.05991v2 Announce Type: replace  Abstract: In safety-critical domains, linguistic ambiguity can have severe consequences; a vague command like "Pass me the vial" in a surgical setting could lead to catastrophic errors. Yet, most embodied AI research overlooks this, assuming instructions are clear and focusing on execution rather than confirmation. To address this critical safety gap, we are the first to define 3D Instruction Ambiguity Detection, a fundamental new task where a model must determine if a command has a single, unambiguous meaning within a given 3D scene. To support this research, we build Ambi3D, the large-scale benchmark for this task, featuring over 700 diverse 3D scenes and around 22k instructions. Our analysis reveals a surprising limitation: state-of-the-art 3D Large Language Models (LLMs) struggle to reliably determine if an instruction is ambiguous. To address this challenge, we propose AmbiVer, a two-stage framework that collects explicit visual evidence from multiple views and uses it to guide an vision-language model (VLM) in judging instruction ambiguity. Extensive experiments demonstrate the challenge of our task and the effectiveness of AmbiVer, paving the way for safer and more trustworthy embodied AI. Code and dataset available at https://jiayuding031020.github.io/ambi3d/.
