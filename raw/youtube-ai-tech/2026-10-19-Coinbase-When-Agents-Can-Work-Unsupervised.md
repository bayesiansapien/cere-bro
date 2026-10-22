# How to Know When an AI Agent Can Work Unsupervised (Evan Kormos, Coinbase)

**Channel:** AI Engineer
**Published:** 2026-10-19
**Source:** https://www.youtube.com/watch?v=_4Ph2dhmUFI
**Domains:** ai-tech (primary)

## TL;DR
A Coinbase player-coach with 15 years in enterprise financial services lays out a graph-theoretic recipe for introducing agents into policy-driven workflows: keep the outer process a deterministic DAG (policy boundary, gated steps), make the inner node loops adaptive (agent plus human iterate until the check passes), and promote agents from supervised to sampled to exception-only based on measured confidence against a representative eval set. The loop is only as trustworthy as the check.

## Key Takeaways
- **Policy is the original system prompt.** Written institutional intent (must / may / should) defines the build state. The running system is the run state. Separate them; the policy changes rarely, the system changes constantly.
- **Agents cut across people, process, and technology.** The talk focuses on where agents meet process: what work they get, what boundaries they have, how outputs earn trust.
- **Outer flow = DAG, inner flow = DCG.** Workflows like commercial lending, token listing, or regulated software delivery are directed acyclic graphs (Airflow-style). Inside each node is a directed cyclic graph: do work, check it, feed back, repeat until good enough (LangGraph-style state).
- **Agents let you revisit parallelism.** Reviews that were too expensive to run in parallel (KYC, financials, risk) can now run concurrently and merge, while keeping the required gates.
- **Volume shifts expose bottlenecks.** Speed up code review and design or security scanning becomes the bottleneck. Operational visibility of the process matters more than the authoring tool.
- **Node selection questions:** Can we check it against policy easily? Can it run in a bounded loop? Can we trace it? Can we fall back to a human? Yes to all four means the node is an automation candidate. The final decision node (the policy check itself) stays human-driven longest.
- **Quality through evaluation, not feelings.** Agents are probabilistic, multiple answers may be acceptable, exact-match is insufficient. Build representative datasets, run evals in repeated series, treat it as statistics. Pair evals with runtime traces. This is the confidence mechanism that complements unit tests.
- **Hill-climb to autonomy:** Day 1 supervised (humans verify everything, refine datasets, define "good" with domain SMEs). When measured confidence hits a policy threshold, move to sampling (humans see a slice, traces cover the rest). Once past the confidence threshold, humans handle exceptions only, still refining datasets.
- **Inject DAG state into agent context** so the agent knows where it sits in the bigger process. Higher-quality inputs mean better outputs at lower compute.

## Architecture & Optimization Mechanics
- **The "check" is the cost center.** Kormos says explicitly that more passes do not mean better results unless the check is reliable, and that long-horizon goals force you to optimize the cost and efficiency of the inner loop. This is the verifier-bottleneck problem: inner-loop iterations are cheap tokens, but the verifier (LLM judge, test suite, human) sets both quality ceiling and cost floor. Cheap-model drafting with expensive-model checking is the natural split.
- **Supervised to sampled to exception is a routing cascade in time.** The promotion criterion (measured confidence against a policy threshold) is the same signal a router uses to pick a cheaper model. The difference is that the expensive fallback is a human and the threshold is set by compliance, not by latency budget.
- **Bounded loops are a compute budget.** "Can it run in a bounded loop?" translates to: can we cap tokens per node and still converge? Nodes that cannot be bounded are where runaway inference cost lives.

## Grounded Context (Web Enrichment)
I could not find external coverage of Kormos or this specific framework. The surrounding Coinbase context checks out: Coinbase launched "Coinbase for Agents" in June 2026, where users set rules on agent activity (trade size, service access) and agent transactions remain subject to existing compliance and transaction-monitoring systems. That is the "deterministic outside, adaptive inside" pattern applied to money. Coinbase also began testing internal Slack/email agents modeled on its founders in April 2026, and a ZenML case study describes its support and compliance stack as RAG plus guardrails plus human-in-the-loop, which matches the supervised-first posture here.

The talk's weakness is that "measured confidence reaches a policy threshold" is never quantified. No sample sizes, no agreement rates, no example threshold. The Microsoft ASSERT work (see the Pamela Fox workshop page) reports LLM-judge agreement with humans at 80 to 90% versus roughly 90% human-to-human, which gives a sense of the ceiling. A policy threshold set above judge-human agreement is unreachable without human review, so the sampling stage is structurally permanent for high-stakes nodes, not a transitional phase.

## Real-World Application / Actionable Step
- **Write the node-selection matrix for one of your own pipelines** (say, a pruning or quantization sweep). For each stage ask Kormos's four questions. Stages that pass all four get an automated check; stages that fail "can we check it against policy easily" are where you still need eyeballs.
- **Instrument the promotion signal.** Log per-node agreement between your automated check and a human-labeled slice. Promote a node from supervised to sampled only when agreement over N runs clears a pre-stated threshold. Make the threshold explicit in the pipeline config, not in someone's head.
- **Treat the verifier as the thing to optimize.** If you are using an LLM judge in a loop, benchmark a cheaper judge model against the expensive one on your labeled slice before you scale the loop. The judge is where cost multiplies.
