---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.21359
url: https://huggingface.co/papers/2610.21359
arxiv_url: https://arxiv.org/abs/2610.21359
date: 2026-10-16
---

# SWE-at-Scale: Scalable Issue Synthesis from Historical Bug Fixes

As coding agents become increasingly capable, robust evaluation requires a broader and more diverse supply of verifiable software engineering (SWE) tasks. However, real-world tasks are constrained by the natural frequency of issue reporting and the substantial cost of manual curation. Furthermore, existing synthetic approaches rely primarily on the pretrained knowledge of large models coupled with heuristic prompting, often failing to capture the authentic, complex mechanics of software failures. To exponentially scale SWE task production, we introduce SWE-at-Scale, a framework that automatically synthesizes realistic issues by reverse-engineering real-world software fixes. Our key insight is that historical fixes encapsulate deep mechanistic knowledge of bug formation: inverting a fix transforms repair supervision into bug-induction supervision grounded in actual development scenarios. SWE-at-Scale transfers these learned bug patterns to novel code contexts, repeatedly sampling diverse bug typologies to construct executable SWE tasks. Extensive experiments show that SWE-at-Scale generates more diverse and realistic SWE tasks than current synthesis baselines while posing greater challenges to state-of-the-art coding agents. Notably, SWE-at-Scale can generate distinct bug types from a single code context, with bug diversity scaling robustly even up to 200 generations per file. Overall, SWE-at-Scale turns finite real-world fixes into reusable supervision for scalable synthesis of realistic, diverse, and challenging SWE tasks.
