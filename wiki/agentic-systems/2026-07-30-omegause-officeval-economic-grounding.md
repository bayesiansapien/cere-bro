# OmegaUse-OfficeVal: Benchmarking LLM Agents on Long-Horizon Office-Suite Tasks with Economic Grounding

**arxiv:** [2607.27155](https://arxiv.org/abs/2607.27155) · **Source:** [HuggingFace Daily Papers 2026-07-30](../../raw/huggingface/2026-07-30-omegause-officeval-benchmarking-llm-agents-on-long-horizon-o.md) · **Site:** [omegause-officeval.github.io](https://omegause-officeval.github.io)

## TL;DR

Agent benchmarks report accuracy. Nobody buys accuracy, they buy work done at a price. OmegaUse-OfficeVal attaches two economic signals to every task: **how long the task takes a human** and **a task price proxy**, which makes it possible to compare an agent's inference cost against the human cost of the same deliverable and to weight the evaluation by task value rather than counting tasks equally. The 100 tasks come from real office-suite requests contributed by practitioners and adapted through a privacy-preserving process, and they are long: **2.32 hours of human labour on average**. Verification is code-based, generated from fine-grained rubrics, which keeps grading stable on deliverables that would otherwise need a judge. The result across several frontier LLMs plus a human baseline is unambiguous and two-sided: **all evaluated models are substantially cheaper and faster than human workers, and none approaches human-level deliverable quality.** Fully open-sourced.

## Why value-weighting changes what the score means

An unweighted benchmark implicitly says every task is worth the same, which is false in every real workflow and is the assumption that lets a model look good by clearing a pile of trivial items. Weighting by a price proxy makes the score answer a different question: not "what fraction of tasks did the agent complete" but "what fraction of the *value* on the table did it capture." Those two numbers come apart precisely when an agent is good at cheap work and bad at expensive work, which is the pattern most production deployments actually report.

The human-labour-time signal does something else useful. It gives the cost comparison a denominator. "Cheaper than a human" is meaningless without knowing how much human time the task consumed, and at 2.32 hours average these are real deliverables rather than the few-minute tasks most agent benchmarks use.

The code-based verifiers deserve a note too. Office-suite outputs (a spreadsheet, a formatted report, a deck) are exactly the artifacts people reach for an LLM judge to grade, and the wiki has repeatedly flagged judge unreliability. Compiling fine-grained rubrics into executable checks is the more expensive path and the correct one.

## Relation to prior wiki state

This is the sixth month of the [agent-benchmarks page](agent-benchmarks.md) accumulating the same finding from different angles, and OmegaUse-OfficeVal adds the axis that was missing. [Claw-Eval-Live (2026-05-01)](2026-05-01-claw-eval-live-agent-benchmark.md) found the best model at 66.7% with HR and management workflows persistently failing. [CEO-Bench (2026-06-18)](2026-06-18-ceo-bench-long-horizon-agents.md) ran a 500-simulated-day business and found most frontier models go bankrupt. [GTA-2 (2026-04-20)](2026-04-20-gta-2-tool-agent-benchmark.md) put top models at 14.39% on long-horizon workflows. All three measure capability. None of them prices it, and pricing is the whole reason anyone deploys.

The "cheaper and faster but not good enough" split is the most decision-relevant framing the cluster has produced, because it says the constraint is quality rather than cost, and cost is the axis everyone optimizes. It also cuts against the deployment narrative in today's industry signal: [The Information reported](https://www.theinformation.com/articles/data-labeling-startups-paying-hvac-companies-150-000-data) that data-labelling startups are paying HVAC companies up to $150,000 to have practitioners rank how models handle real business tasks like vendor invoices and payroll. That is the market buying exactly the signal this benchmark generates, at a price that suggests it is scarce.

Most importantly, this lands on the same day as Kurate cs.AI **#1**, [Do Agent Benchmarks Measure Capability? Protocol Validity in the Age of Agentic AI](http://arxiv.org/abs/2607.22368) (score 1573, 87.5% win rate), which argues agent benchmarks have a protocol-validity problem rather than a difficulty problem. OmegaUse-OfficeVal is a partial answer rather than a target: derived from real practitioner requests, verified by executable code rather than a judge, and grounded in an external unit (money, hours) rather than a self-defined score. Those are three of the properties a validity critique asks for.

## Gaps

100 tasks is small, and value-weighting a small task set makes the aggregate sensitive to a handful of high-price items. The price proxy's construction is the load-bearing detail and is not described in the abstract, which matters because the whole value-weighted result inherits its biases. Office-suite work is also the domain where the privacy-preserving adaptation is most likely to have removed the messy context that makes real tasks hard, so there is a plausible direction in which the benchmark is easier than the job. The human baseline size is unstated. And inference cost is a moving target that will make the economic comparison stale within a quarter, which is an argument for the benchmark reporting cost-per-quality-point rather than a fixed comparison.

## Industrial implication

This is the benchmark shape that procurement actually needs, and its immediate use is as a template rather than a leaderboard. Any enterprise evaluating agents on internal workflows should be attaching human-hours and a price proxy to its own task set, because the resulting number answers the buying question directly and the accuracy number does not. The finding that quality rather than cost is binding also has a clear consequence: the ROI case for office-suite agents currently depends on human review, so the deployment that works is agent-drafts-human-approves, and the economics of that are a review-time reduction rather than a labour replacement.

## Related

- [Agent Evaluation & Benchmarks](agent-benchmarks.md)
- [CEO-Bench: long-horizon agents](2026-06-18-ceo-bench-long-horizon-agents.md)
- [Claw-Eval-Live](2026-05-01-claw-eval-live-agent-benchmark.md)
- [Daily digest 2026-07-30](../daily-digest/2026-07/2026-07-30.md)
