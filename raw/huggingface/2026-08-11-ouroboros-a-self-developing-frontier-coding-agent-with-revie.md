---
source: farmer/huggingface
farmed: 2026-08-11T07:29:49.637235+00:00
arxiv_id: 2608.08311
url: https://huggingface.co/papers/2608.08311
arxiv_url: https://arxiv.org/abs/2608.08311
date: 2026-08-11
---

# Ouroboros: A Self-Developing Frontier Coding Agent with Reviewed Core Evolution

We present Ouroboros, a self-developing agent harness whose tools, prompts, context assembly, and core implementation improve through reviewed commits that become the runtime for later work. Core evolution proceeds in two modes. In recursive free evolution, improvement is itself a task, and completing one evolution cycle can schedule the next. In experience-driven core evolution, ordinary work and social interaction expose bugs, rough edges, and inefficient context construction that lead to reviewed structural changes.
  On Terminal-Bench 2.1, an Opus 5 run scores 86.74%, the best result reported on the benchmark. On OSWorld-Verified, an Opus 5 run reaches 90.69%, exceeding the best previously reported score. A five-rollout CL-Bench campaign achieves a normalized reward of 0.2301, setting a new state of the art.
  Hope is the longest-running publicly documented Ouroboros deployment. It is a 161-day living agent experiment in free evolution under governed human communication across seven surfaces. Human interaction surfaces faults and generates proposals, but the agent decides which changes to pursue. Because a self-developing agent may rewrite its own code and select new model APIs, operational safety becomes a primary design problem: guardrails must remain authoritative under evolutionary and public social pressure. Benchmark campaigns use frozen system snapshots, while Hope continues live evolution on a separate lineage.
