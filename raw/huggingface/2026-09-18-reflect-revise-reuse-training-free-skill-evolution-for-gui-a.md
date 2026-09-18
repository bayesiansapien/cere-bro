---
source: farmer/huggingface
farmed: 2026-09-18T16:13:44.923131+00:00
arxiv_id: 2609.17653
url: https://huggingface.co/papers/2609.17653
arxiv_url: https://arxiv.org/abs/2609.17653
date: 2026-09-18
---

# Reflect, Revise, Reuse: Training-Free Skill Evolution for GUI Agents

GUI agents execute long-horizon tasks on dynamic graphical user interfaces, where pop-ups, delayed loads, and relocated widgets routinely invalidate plans fixed before execution. Recent agent-skill frameworks encapsulate reusable procedural knowledge to mitigate this, yet existing skill designs are largely developed without targeting GUI execution dynamics and treat skills as static artifacts produced before deployment rather than living procedural knowledge that improves through it. We argue that what GUI agents need is not better static skills, but skills that can be revised from execution feedback at deployment time, without additional training. We propose EvoSkill-GUI, a training-free framework in which each skill is a structured multi-file package containing retrieval metadata, executable plans, backup localization, failure-recovery rules, accessibility utilities, and failure cases. EvoSkill-GUI operates through a \emph{reflect-revise-reuse} loop: the executor performs instant in-rollout revisions, an isolated critic diagnoses failed trajectories under strict information isolation, and the executor edits specific skill files through a restricted tool interface. Across MobileWorld, AndroidWorld, and OSWorld, three mainstream GUI benchmarks spanning mobile and desktop platforms, EvoSkill-GUI consistently improves multiple base models without any training, with maximum gains of +16.2%, +6.0%, and +10.5% respectively, and evolved skill libraries continue to benefit related tasks rather than being rebuilt from scratch. Our code is available at https://github.com/ZJU-REAL/EvoSkill-GUI.
