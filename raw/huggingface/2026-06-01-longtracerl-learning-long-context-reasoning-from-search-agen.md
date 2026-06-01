---
source: farmer/huggingface
farmed: 2026-06-01T09:02:45Z
arxiv_id: 2605.31584
url: https://huggingface.co/papers/2605.31584
arxiv_url: https://arxiv.org/abs/2605.31584
date: 2026-06-01
---

# LongTraceRL: Learning Long-Context Reasoning from Search Agent Trajectories with Rubric Rewards

Long-context reasoning remains a central challenge for large language models, which often fail to locate and integrate key information in extensive distracting content. Reinforcement learning with verifiable rewards (RLVR) has shown promise for this task, yet existing methods are limited by low-confusability distractors and sparse, outcome-only reward signals that cannot supervise intermediate reasoning steps. To address these issues, we introduce LongTraceRL. For data construction, we generate multi-hop questions via knowledge graph random walks and leverage search agent trajectories to build tiered distractors: documents the agent read but did not cite (high confusability) and documents that appeared in search results but were never opened (low confusability), producing training contexts that are far more challenging than those built by random sampling or one-shot search. For reward design, we propose a rubric reward that uses the gold entities along each reasoning chain as fine-grained, entity-level process supervision. This rubric reward is applied only to responses with correct final answers (positive-only strategy), distinguishing the reasoning quality among correct responses and preventing reward hacking. Experiments on three reasoning LLMs (4B--30B) across five long-context benchmarks demonstrate that LongTraceRL consistently outperforms strong baselines and encourages comprehensive, evidence-grounded reasoning.
