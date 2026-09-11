# The third shortage: CPUs, because agents run tools

**Source:** Gergely Orosz, The Pragmatic Engineer, *The Pulse #191* (2026-09-10) · [Post](https://newsletter.pragmaticengineer.com/p/the-pulse-191-a-new-trend-of-cpu) · [raw](../../raw/rss/2026-09-10-pragmatic-engineer-the-pulse-191-a-new-trend-of-cpu-shortages.md)

## TL;DR

Three compute shortages in sequence, each caused by AI and each hitting a different part: first GPUs, then memory, and now **CPUs**. The stated mechanism is specific and it is not "AI needs more compute" in general. It is that **agents use tools**, and tool use is CPU work. An agent that reads files, runs a build, executes a test suite, greps a repository and shells out to a linter is generating conventional x86 load, not accelerator load, and it does so at machine speed rather than human speed. Orosz's practical advice to engineering leaders is blunt: if you will need more compute in the future, secure it now.

## Key points

- **The demand is downstream of agent adoption, not of model training.** Every additional coding agent in a team's workflow multiplies CI runs, container starts, and test executions. The GPU cost of the model is visible on an invoice; the CPU cost of what the model *does* lands on a different budget line and nobody forecast it.
- **This is a second-order effect of a first-order product success**, which is why it caught procurement unprepared. The industry planned accelerator capacity for a world where humans write code and machines infer, not one where machines write code and machines run it.
- **It reframes agent efficiency work.** Token cost has been the whole conversation. Tool-call cost is a parallel meter that has been running unread.

## How this relates to prior wiki pages

**It completes a triple that this wiki assembled in a single day without meaning to.** [DeepSeek V4.1 Flash (09-10)](../llms-foundation-models/2026-09-10-deepseek-v41-flash-architecture.md) moves half a model's parameters off HBM onto host LPDDR because HBM is scarce. [Behind-the-meter power (09-10)](2026-09-10-behind-the-meter-power-datacenters.md) records 75 GW of binding orders for onsite generation because grid power is scarce. This says CPUs are scarce because agents run tools. **Memory, electricity and general-purpose compute are all binding at once**, and the only one of the three the research literature is actively optimizing is memory.

**It gives an economic reading to [T1 (09-10)](../agentic-systems/2026-09-10-t1-terminal-agent-rl.md), which trains a 122B mixture-of-experts model against a real cloud shell for 300+ tool-call turns per task with each task's own verifier executing the reward.** Every one of those 300 turns is a sandbox invocation. T1's unreported cost is not only GPU-hours for the policy, it is CPU-hours for the environment, and [WMRL (09-10)](../agentic-systems/2026-09-10-wmrl-world-model-rl-research-agents.md) makes exactly that point from the training side: environment execution occupies an exclusive sandbox and real machine time while generation batches, so execution dominates the bill as trajectories lengthen. **WMRL's 3-4x speedup from replacing the sandbox with a learned world model is, read through this lens, a CPU-shortage mitigation.** Two papers and a newsletter arrived at the same conclusion on the same day from research, systems and procurement angles respectively.

**It also puts a number-shaped constraint under the local-CI argument circulating in the practitioner feed the same day**, that personal machines have become capable enough to run a real share of verification locally rather than remotely. If shared CI CPU is the scarce resource, moving verification to the developer's laptop is arbitrage, not just latency optimization.

## Gaps

Most of the analysis is behind the paywall, so the free edition carries the claim and the advice without the sourcing. No quantification of how much CPU an agent-hour actually consumes, which is the number a capacity planner needs. And there is a plausible confound: 2026 has independent CPU supply pressure from fab capacity being reallocated toward accelerator and HBM production, which would produce the same shortage with a different cause.

## Related

- [Compute economics](compute-economics.md) · [Memory hierarchy](memory-hierarchy.md) · [Behind-the-meter power](2026-09-10-behind-the-meter-power-datacenters.md) · [Agent harness engineering](../agentic-systems/agent-harness-engineering.md)
