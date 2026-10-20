# How to Know When an AI Agent Can Work Unsupervised (Evan Kormos, Coinbase)

**Channel:** AI Engineer
**Published:** 2026-10-19
**Source:** https://www.youtube.com/watch?v=_4Ph2dhmUFI
**Domains:** ai-tech

## TL;DR
Kormos, a 20-year enterprise financial-services engineer now at Coinbase, gives a graph-theoretic recipe for putting agents into policy-driven workflows: keep the outer workflow a deterministic DAG bounded by written policy (must, may, should), make each node an adaptive inner loop (a cyclic graph of do, check, refine), and graduate agents from supervised to sampled to exception-only based on measured confidence rather than vibes. The loop is only as trustworthy as the check, so the real work is defining what "good" looks like with domain experts and measuring it statistically over representative datasets and runtime traces.

## Key Takeaways
- Policy is the "original system prompt" of an organization. Separate it (build state) from the running system (run state), which is constantly changing under product pressure.
- Agents cut across the people, process, technology triad. The talk focuses on agents meeting process: what work they get, what boundaries, and how trust in outputs is built.
- Outer workflow = DAG (Airflow-style). Agents make it worth revisiting what can run in parallel (KYC and financials simultaneously) while keeping required gates (credit memo, risk review, decision) in sequence.
- Inner node = directed cyclic graph (LangGraph-style): do work, check it, iterate on feedback until it passes. Keep it deterministic outside, adaptive inside.
- Adding agents shifts volume along the flow. Faster code review exposes bottlenecks in design or security scanning. Operational visibility into the process matters more than the workflow authoring tool.
- Higher quality inputs give better outputs at lower compute. One cheap trick: inject the DAG state into the agent's context so it knows where it sits in the larger process.
- Agents are probabilistic, so exact-match tests are insufficient. Build representative datasets, run evals in repeated series, treat it as statistics, and pair evals with runtime traces. This is the "confidence mechanism" that unit tests provide for traditional software.
- Node-selection questions for automation: can it be checked against policy easily, can it run in a bounded loop, can it be traced, can it fall back to a human? Yes on all four means a candidate for agent-driven. The final policy decision node stays human-driven and is the hardest to hill-climb.
- Graduation path: Day one supervised (humans verify all output, datasets refined with SMEs). When measured confidence crosses a policy threshold, move to sampling (humans see a slice, traces cover the rest). Then exception-only, with humans still curating datasets.

## Architecture & Optimization Mechanics
- **Deterministic shell, adaptive core.** This is the same separation as a compiled control plane around a stochastic inner solver. It maps cleanly onto routing: the DAG decides which node fires, the node decides how much compute to spend iterating.
- **Check quality bounds loop value.** More passes in a refine loop do not help if the verifier is weak. This is the same lesson as best-of-N and self-consistency: the reward model or verifier is the binding constraint, not the generator.
- **Bounded loops as a cost control.** "Can it run in a bounded loop" is both a safety and a budget question. Max-iteration caps per node are the natural place to put per-task token budgets.
- **DAG-state injection** is cheap context engineering that reduces wasted exploration tokens. Telling the agent its upstream inputs and downstream consumers constrains the output format and scope.
- **Confidence threshold as a router signal.** The supervised-to-sampling transition is literally a measured accuracy threshold. The same statistic can route individual tasks: high-confidence outputs skip human review, low-confidence ones get escalated.

## Grounded Context (Web Enrichment)
The talk's graduated model matches what the industry converged on in 2026. Practitioner frameworks describe autonomy as a spectrum (observe, advise, act-within-limits, fully autonomous) with exception handling as the common boundary and autonomy "earned" through demonstrated reliability under supervision, including automatic demotion when monitoring signals degrade. Meticulous Research's 2026 view of financial services is that agents are in production for tier-one routine servicing and reconciliations, in pilot for KYC refresh and dispute handling, and largely excluded from credit approval and trade execution. That lines up with Kormos keeping the lending "decision" node human-driven. Kognitos cites a Bank of England/FCA figure that fully autonomous decision-making is only about 2 percent of current finance use cases, which suggests the sampling and exception-only tiers are where most real value sits today.

No regulator has issued a formal framework for statistically sampled human review of agent outputs, so the "policy threshold" Kormos describes is still a per-institution choice. The weakest part of the talk is that it never specifies what the threshold or the sample size should be, which is exactly where model risk management teams will push back. The eval-plus-traces approach is standard (LangSmith, Braintrust, Arize style tooling), and the talk adds nothing new there beyond framing it as the agent equivalent of a unit test suite.

## Real-World Application / Actionable Step
- **Routing:** Implement the supervised-to-sampling graduation as a per-route confidence threshold. Log a correctness signal per task, compute a running accuracy per (node, model) pair, and let cheap models take nodes once their measured accuracy clears the bar. Demote automatically when the trace-based accuracy drops.
- **Verifier investment:** If you run any refine loop (self-correction, best-of-N, speculative drafting with a verify step), spend engineering time on the checker before the generator. Measure how often the check passes bad outputs; that number bounds everything downstream.
- **Cheap win:** add workflow position (upstream artifacts, downstream consumer, allowed output schema) to agent context. It cuts exploration tokens and makes outputs easier to verify automatically.
