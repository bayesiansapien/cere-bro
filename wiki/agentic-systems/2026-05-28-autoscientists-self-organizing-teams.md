# AutoScientists: Self-Organizing Agent Teams for Long-Running Scientific Experimentation

**Date ingested:** 2026-05-28
**Source:** HuggingFace Daily Papers
**Links:** [arxiv 2605.28655](https://arxiv.org/abs/2605.28655) · [HuggingFace](https://huggingface.co/papers/2605.28655) · [raw](../../raw/huggingface/2026-05-28-autoscientists-self-organizing-agent-teams-for-long-running.md)

## TL;DR

AutoScientists is a decentralized multi-agent system for long-running computational science. Agents interpret a shared experimental state, self-organize into teams around promising hypotheses, critique proposals before spending compute, and share both successes and failures so the swarm does not redo work. Under matched compute budgets it beats prior single-trajectory or central-planner agents across three different domains: 74.4% mean leaderboard percentile on BioML-Bench (24 tasks across imaging, protein engineering, single-cell omics, drug discovery), 1.9x faster to a target bits-per-byte on GPT training optimization (and finds 7 accepted improvements where the single-agent baseline finds zero from the same starting champion), and +12.5% Spearman on ACE2-Spike binding plus +6.5% across all 217 ProteinGym assays applying the same discovered method without modification.

```
Single-trajectory agent:        ●──►●──►●──►●  (one path, fixed plan)
Central planner + workers:      ┌─●─┐
                                │ ▼ │  (planner bottleneck, fixed objective)
                                ●─●─●

AutoScientists (decentralized):    ●───hyp_A
                                  ╱      ▲
                                 ●───────●  ← shared state, agents migrate to hot hypotheses,
                                  ╲      │     critique-before-compute, share failure traces
                                   ●───hyp_B
```

## Key findings

- BioML-Bench: 74.4% mean leaderboard percentile across 24 tasks, +8.33pp over the strongest single-agent baseline.
- GPT training optimization: 1.9x faster to target validation bits-per-byte; continues finding improvements from a starting champion where the single-agent baseline finds none (7 vs 0).
- ProteinGym: +12.5% Spearman on ACE2-Spike binding (a specific protein design task); +6.5% mean across all 217 assays with the same method applied without modification.
- The decentralized self-organizing structure is the explicit improvement over prior agent frameworks like Autoresearch.

## How this fits prior wiki state

There is an immediate tension with today's AI Research Agents Narrow Scientific Exploration ([[2026-05-28-ai-research-agents-narrow-exploration]]), which finds that AI research agents in aggregate concentrate ideas around the seed literature and produce lower-citation follow-ons than humans. AutoScientists makes the opposite-shaped claim, that a decentralized swarm broadens exploration enough to find genuinely SOTA-beating methods on hard scientific tasks.

The tension is real but might be reconcilable: AutoScientists works on tasks with executable verification (a benchmark score, a binding-affinity correlation, a training loss), where the swarm can keep what works and discard what does not. The Narrow Exploration study is about ideation in open-ended research areas where no immediate verifier exists, so the agent has no signal to push past the seed literature. The pattern that emerges across both papers: agent-driven research broadens or narrows depending on whether a credible task verifier is in the loop. Worth tracking.

The decentralized-vs-orchestrator framing also continues yesterday's Scaling the Harness ([[2026-05-27-scaling-the-harness]]) thesis that the substrate around the model is where quality lives now. AutoScientists is the most ambitious empirical evidence for that thesis to date.

## Related pages

- [[2026-05-28-ai-research-agents-narrow-exploration]] — opposite finding on aggregate exploration breadth
- [[2026-05-27-scaling-the-harness]] — the harness-as-first-class thesis
- [[2026-04-22-evaluation-driven-scaling-scientific]] — evaluation-driven scaling for scientific discovery
- [[multi-agent-systems]] — concept page

## Research angle

The most interesting result is the GPT training optimization line: 7 accepted improvements vs 0 for the single-agent baseline from the same starting champion. That is direct evidence that decentralized exploration finds local optima the orchestrator misses. The mechanism likely is that critique-before-compute and failure-sharing prevent the swarm from re-deriving dead ends, which is the same mechanism used in evolutionary algorithms but at the agent level. A formal connection to multi-objective evolutionary search would be the natural next paper.
