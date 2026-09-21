---
source: farmer/huggingface
farmed: 2026-09-21T05:24:18.050611+00:00
arxiv_id: 2609.05571
url: https://huggingface.co/papers/2609.05571
arxiv_url: https://arxiv.org/abs/2609.05571
date: 2026-09-21
---

# Grounded Skill Synthesis from Code at Scale for Agentic Intelligence

Reusable skills give agents transferable procedural knowledge, making scalable acquisition essential for extending agents beyond prior experience. Existing methods face two limitations: trajectory-based synthesis requires interactions with specific environments, while document-derived skills may lack executable evidence and verification. Source code offers a complementary path: it requires no prior agent experience yet provides executable evidence for grounding abstractions. We present Code2Skill, a fully automated pipeline that transforms selected code units into implementation-anchored records of atomic operations, composite workflows, and recurring patterns, then verifies each record through source-body-blind reconstruction and source-aware comparison. Applied to 19,769 popular, actively maintained GitHub repositories, Code2Skill produces CodeSkillBank, a grounded bank of 1,006,822 accepted records with workflow, boundary, provenance, and source-evidence metadata. Across 72 protocol-matched evaluations covering nine model settings and eight benchmarks, models augmented with retrieved CodeSkillBank skills improve by 11.7% on average over matched baselines and outperform them in 57 cases. Under a unified downstream interface, Code2Skill also outperforms trajectory-derived skill banks on all seven shared benchmarks, showing that repository-derived skills can provide useful procedural knowledge before agents accumulate sufficient interaction experience. Skills synthesized from tested AI-generated code achieve a 93.50% pass rate, compared with 93.00% for human-written code, providing initial evidence that the pipeline can expand with the growing volume of AI-generated software. Overall, Code2Skill transforms procedural knowledge embedded in repositories into grounded, verifiable, and transferable agent skills.
