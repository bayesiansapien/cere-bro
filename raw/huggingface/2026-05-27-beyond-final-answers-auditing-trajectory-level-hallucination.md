---
source: farmer/huggingface
farmed: 2026-05-27T07:52:03Z
arxiv_id: 2605.24219
url: https://huggingface.co/papers/2605.24219
arxiv_url: https://arxiv.org/abs/2605.24219
date: 2026-05-27
upvotes: 4
---

# Beyond Final Answers: Auditing Trajectory-Level Hallucinations in Multi-Agent Industrial Workflows

Large Language Models (LLMs) are increasingly deployed as autonomous agents that reason, use tools, and act over multiple steps. Yet most hallucination benchmarks still evaluate only the final output, missing failures that originate in intermediate Thought-Action-Observation steps. We present Trajel, a dataset and evaluation framework for auditing trajectory-level hallucinations in multi-agent industrial workflows. Trajel introduces a five-type hallucination taxonomy (factual, referential, logical, procedural, and scope-based) over expert-annotated agent traces from AssetOpsBench. We benchmark supervised detection models at the subtask, trajectory, and long-context levels. Our results show that the most common failure modes are missed by existing benchmarks, that nearly half of hallucinated trajectories involve multiple types at once, and that automated detectors with high binary accuracy still misclassify the subtlest types. Trajectory-aware detection significantly outperforms standard post-hoc verification, making taxonomy-grounded evaluation necessary for safer agentic deployment.
