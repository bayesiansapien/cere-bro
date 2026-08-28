---
source: farmer/huggingface
farmed: 2026-08-28T14:50:07.734667+05:30
arxiv_id: 2608.26238
url: https://huggingface.co/papers/2608.26238
arxiv_url: https://arxiv.org/abs/2608.26238
date: 2026-08-28
---

# Procedura: Agentic 3D Modeling with Procedural Control

Native 3D generators now recover impressive mesh geometry from a single image. However, a dense mesh stays soft where a machined object should be sharp, it carries no part decomposition, and it exposes no parameter a user could edit. To address this, we explore the paradigm of 3D shape as code, leveraging and scaling the coding ability of an LLM for 3D modeling. We introduce Procedura, a novel 3D modeling agent framework that writes an object as a procedural assembly, a parametric program whose named parts are joined by typed, machine-checkable mates. From a text prompt, the agent plans the object as an assembly graph and writes the program part by part, solving each placement from the mated frames rather than guessing it, and admitting a part only once compile, mate, and connectivity checks pass. A decoupled vision critic then refines the assembly one diagnosed fix at a time. Moreover, the same graph carries per-part materials and a simulator-validated articulation. We evaluate on P3D-Bench under its assembly judge, and with the same judge on MechBench-36, our hard-surface benchmark. On both, Procedura outperforms state-of-the-art native 3D generators and every prior 3D-code agent on judged quality, produces the sharpest edges of any method we evaluate, and is the only one whose output is an editable, part-structured program.
