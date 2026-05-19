---
source: farmer/huggingface
farmed: 2026-05-19T09:55:00.432604+00:00
arxiv_id: 2605.18401
url: https://huggingface.co/papers/2605.18401
arxiv_url: https://arxiv.org/abs/2605.18401
date: 2026-05-19
---

# SkillsVote: Lifecycle Governance of Agent Skills from Collection, Recommendation to Evolution

Long-horizon LLM agents leave traces that could become reusable experience, but raw trajectories are noisy and hard to govern. We treat Agent Skills as an experience schema that couples executable scripts, with non-executable guidance on procedures. Yet open skill ecosystems contain redundant, uneven, environment-sensitive artifacts, and indiscriminate updates can pollute future context. We present SkillsVote, a lifecycle-governance framework for Agent Skills from collection and recommendation to evolution. SkillsVote profiles a million-scale open-source corpus for environment requirements, quality, and verifiability, then synthesizes tasks for verifiable skills. Before execution, SkillsVote performs agentic library search over structured skill library to expose instructional skill context. After execution, it decomposes trajectories into skill-linked subtasks, attributes outcomes to skill use, agent exploration, environment, and result signals, and admits only successful reusable discoveries to evidence-gated updates. In our evaluation, offline evolution improves GPT-5.2 on Terminal-Bench 2.0 by up to 7.9 pp, while online evolution improves SWE-Bench Pro by up to 2.6 pp. Overall, governed external skill libraries can improve frozen agents without model updates when systems control exposure, credit, and preservation.
