# Compound Engineering vs gstack vs Karpathy Autoresearch vs Superpowers vs RSI

**Source:** Ken Huang, Substack ("Agentic AI" feed), 2026-05-23.
**Link:** [Compound Engineering vs gstack vs Karpathy's Autoresearch vs Superpowers vs Recursive Self-Improvement](https://kenhuangus.substack.com/p/compound-engineering-vs-gstack-vs)

## TL;DR

Five things that get lumped together as "agentic coding workflows" actually sit at five different layers. Compound Engineering (Kieran Klaassen / Every) is a philosophy and workflow with a reference Claude Code plugin, 80 percent planning and review and 20 percent coding, with a /workflows:compound step that codifies lessons into AGENTS.md and skills. gstack (Garry Tan) is a personal skill pack of 23 role personas (CEO, EM, Designer, Reviewer, Security Officer, Release Engineer, Doc Engineer), reportedly 10-20k LOC/day. Karpathy's Autoresearch is an autonomous ML research harness with three files (program.md, train.py, prepare.py), 12 experiments per hour and 100 overnight, producing a 0.8B model that beat a prior 1.6B by 19 percent overnight. Superpowers (obra) is an agentic skills framework that enforces TDD and spec-driven development with fresh sub-agent context windows per task. Recursive Self-Improvement is the theoretical capability; Compound Engineering is human-in-the-loop RSI at the workflow level, Autoresearch is bounded RSI at the model-weights level, gstack and Superpowers are not RSI at all.

## Why this matters

The agentic coding harness space has matured to the point that "use Claude Code" is the wrong-grained question. The right-grained question is which layer of the stack a problem lives at, and which harness is calibrated for that layer. Ken Huang's framing is the cleanest taxonomy of that distinction to date.

For Tier 1 research interests (efficiency, routing, KV cache): the Autoresearch harness is the only one of the five that closes a model-weights feedback loop. Karpathy reports 11 percent speedup on already-tuned nanochat after 700 experiments over two days. Tobi Lutke trained a 0.8B model overnight that beat his prior 1.6B by 19 percent. These are the kind of returns that move the research frontier when reproduced at scale.

For agent-routing research: Compound Engineering's /workflows:compound step is the closest analogue in the harness space to what [Maestro (today's HF paper on RL-driven model-skill orchestration)](../ai-routing/2026-05-23-maestro-rl-orchestrated-model-skill-ensemble.md) does at the model layer. Both convert experience into durable structure. Maestro learns a routing policy; Compound Engineering writes lessons into project knowledge files. They are the same idea expressed at different levels of the system.

## Connections to prior wiki state

This refines the agentic-coding taxonomy that has been accumulating across the past month. The Anthropic harness experiment from yesterday's Twitter morning ($9 unusable vs $200 playable on the same Opus 4.5) is the strongest single-experiment demonstration that the harness is part of the intelligence. Ken Huang's taxonomy explains why: gstack-style role delegation, Superpowers-style spec discipline, and Compound Engineering's lessons-back-into-files loop are doing different things, and stacking them all gives the harness more leverage than any single approach.

For research-engineering culture: Autoresearch's promise that "anything with one editable file and one measurable scalar" can be Autoresearched is the formalization of an idea that has been moving since [Claude Code architecture (04-17 and 04-19)](2026-04-17-claude-code-architecture.md) and [autoresearchclaw self-reinforcing autonomous research (05-20)](2026-05-20-autoresearchclaw-self-reinforcing-autonomous-research.md). The 0.8B-beats-1.6B result is the first independent reproduction of the Karpathy framing at non-trivial scale.

## Gaps

Huang's taxonomy is descriptive, not benchmarked. We have anecdotal numbers (Garry Tan's 10-20k LOC/day, Karpathy's 11 percent nanochat speedup, Tobi Lutke's 0.8B-beats-1.6B) but no controlled comparison across the five frameworks on the same task. The Anthropic harness experiment from yesterday's morning Twitter is the closest existing controlled measurement, and it only covered the no-harness vs full-harness binary, not the cross-framework comparison.

## Research angle

The natural follow-up: a benchmark suite that runs the same coding tasks under each of the five harnesses, measures cost, time, and quality, and reports the cross-framework cost-quality Pareto frontier. The closest existing thing is [saasbench (05-21)](2026-05-21-saasbench-enterprise-saas-coding-agents.md), but that runs across models, not across harnesses. A harness-axis benchmark is the missing measurement.

## Raw source

[raw/rss/2026-05-23-agentic-ai-compound-engineering-vs-gstack-vs-karpathys-autoresearc.md](../../raw/rss/2026-05-23-agentic-ai-compound-engineering-vs-gstack-vs-karpathys-autoresearc.md)
