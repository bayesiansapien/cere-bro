# Your Team's Agents Are All Shipping to the Same Code at Once

**Channel:** AI Engineer (Patrick Debois, Tessl)
**Published:** 2026-11-10
**Source:** https://www.youtube.com/watch?v=fTUinMqA1XQ

## TL;DR
The DevOps co-founder argues that "solo factories" (one dev, many local agents) are giving way to "multiplayer factories" where many humans and agents share one board and one main branch. PR volume rises about 10x, rebases and CI reruns pile up, and concurrency stops being the exception. The shift he names is **continuous delivery to concurrent delivery**: plan to avoid collisions, isolate each agent's world, merge semantically and by intent, use speculative merge trains, route review by risk, and keep a shared decision ledger.

## Key Takeaways
- **Pressure points:** about 10x PRs, agents undoing each other's changes, every merge forcing rebase plus test rerun (slower, costlier CI), plus agent incidents and factory maintenance (skills, loops) all competing for human approval.
- **Collision avoidance at plan time:** split work by domain or by AST graph down to file and function. Agents *claim* tickets and *announce* the files they will touch.
- **Isolation beyond worktrees:** per-agent machine, context slice, mocked API version, DB snapshot with test data, digital twins of external systems.
- **Collision strategies:** wait, requeue, or renegotiate the plan mid-execution. Merge by function, not by line. Agents fix conflicts and anticipate incoming changes.
- **Intent conflicts:** two PRs that merge cleanly and pass tests can still clash semantically (invoice totals switched to cents while reporting assumes dollars). Agents should check intent consistency across concurrent merges.
- **Speculative merge trains:** test compatible PR combinations in parallel so one failing PR does not stall the rest.
- **Human side:** agents join team chats and refine tickets from many people's input (shared plan mode). Non-engineers (sales, support) kick off features within the same pipeline and skills. Agents present decisions as options. Every decision goes to a queryable ledger. Hybrid escape hatch: Helix ML-style "drop into an IDE with the agent's exact context, then hand back."
- **Review by risk, not just quality:** docs auto-merge, auth gets human review, middle ground uses gradual rollout. Invest in cheap restore and rollback so failures are inexpensive.
- **New org unit:** a "factory team," analogous to a platform team, owns skills, context freshness, and factory monitoring.

## Architecture & Optimization Mechanics
- **Merge contention is a scheduling problem.** Speculative merge trains are branch prediction for CI: optimistically test likely-landing combinations in parallel and discard on misprediction. The cost trade-off is CI compute vs latency, and at 10x PR volume that compute bill dominates.
- **AST-graph partitioning** is graph partitioning to minimize cross-agent edges, the same objective as expert placement or tensor sharding to minimize communication.
- **Intent-level merge checks** need semantic diffing, which means an LLM pass over every concurrent PR pair (O(n²)). In practice this needs a cheap filter (shared symbols or data flow) before invoking a model.
- **Weak spots:** no metrics on conflict rates, CI cost, or merge latency before and after. Mostly a taxonomy and a pitch for Tessl and concurrent.cd.

## Grounded Context (Web Enrichment)
Speculative merge trains are not new. GitLab merge trains create temporary merged-result commits so each MR is tested on top of those ahead of it, running up to 20 pipelines in parallel (auto-merge GA in GitLab 17.7). OpenStack's Zuul pioneered "optimistically speculative parallelized testing" precisely because changes were approved faster than they could be tested, which is the same situation agents now create. GitHub Merge Queue offers a similar capability. The novel part of Debois's argument is applying these to agent-generated volume and adding intent-level checks, which no mainstream merge queue does yet.

The talk overlaps with Vorflux's "Merge Is the Bottleneck" from the same conference. Both converge on merge queues, multiplayer ownership, and human attention as the binding constraint.

## Real-World Application / Actionable Step
- If you run multiple research agents on one repo (e.g. kernel tweaks plus quant configs), add claim-and-announce: each agent writes intended files and functions to a shared lock file before editing. Reject overlapping claims.
- Turn on a merge queue (GitHub Merge Queue or GitLab merge trains) as soon as agents open more than a handful of PRs a day.
- Add an intent-check step for PRs touching shared numerics (dtype, scale factors, units). Have an agent diff the assumptions, not the lines.
- Tier auto-merge by risk: experiment scripts and docs auto-merge, while shared inference or kernel code requires human review plus benchmark evidence.
