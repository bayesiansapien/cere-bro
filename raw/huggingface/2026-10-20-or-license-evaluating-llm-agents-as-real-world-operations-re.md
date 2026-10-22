---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.24087
url: https://huggingface.co/papers/2610.24087
arxiv_url: https://arxiv.org/abs/2610.24087
date: 2026-10-20
---

# OR-License: Evaluating LLM Agents as Real-World Operations Research Practitioners

Can large language model (LLM) agents deliver expert-level operations research (OR) solutions directly from original client materials, without prior expert reformulation? Existing OR benchmarks typically begin with self-contained descriptions or predefined optimization tasks, underrepresenting the translation of original business materials into professionally validated solutions. We introduce OR-License, an end-to-end benchmark of 31 instances across 10 industrial scenarios from paid OR engagements totaling USD 3.68 million. It preserves original requirements, input data, deliverable formats, and information boundaries after de-identification. To study information acquisition, we introduce ORSim, a controlled client simulator that discloses business facts without supplying OR expertise. Hidden evaluation checks feasibility and compares objective quality against original expert solutions accepted by clients before benchmark construction. Deployment-Adjusted Quality (DAQ) averages expert-relative quality across instances, assigning zero to infeasible deliveries. Across 11 frontier LLMs using coding-agent harnesses, several exceed the expert reference in conditional objective quality, but none matches its DAQ; the strongest primary Claude Code configuration achieves 88.39% strict feasibility and a DAQ of 0.87 against the expert reference of 1. Client information acquisition extends beyond clarification into solution development and validation, with some later stages showing higher confirmed issue-resolution proportions. Trajectory analysis identifies formulation and implementation failures, while task-equalized research-chain completion rates range from 24% to 45% across models on evaluable tasks. These findings motivate sustained information-gap resolution, faithful problem formulation, and evidence-linked self-improvement for reliable long-horizon agents.
