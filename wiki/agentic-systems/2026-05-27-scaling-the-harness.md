# Scaling the Harness: System Scaling as the Next Bottleneck in Agentic AI

**Source:** Twitter curated retweet (@dair_ai / @omarsar0) · arxiv 2605.26112
**arxiv:** [2605.26112](https://arxiv.org/abs/2605.26112)
**Date:** 2026-05-27 (surfaced via Twitter)
**Raw:** [raw/twitter/2026-05-27-morning.md](../../raw/twitter/2026-05-27-morning.md)
**Tier:** 2 (agentic systems)

## TL;DR

A position paper arguing the next major bottleneck in agentic AI is *system* scaling, not model scaling: the design of auditable, persistent, modular, verifiable architecture *around* the foundation model. The authors name this the agent harness, the structured execution layer that turns model capability into long-horizon behavior, and argue it should be a first-class object of design, evaluation, and optimization rather than a bag of implementation details. Agent performance emerges from the interaction among six components: the foundation model, the memory substrate, the context constructor, the skill-routing layer, the orchestration loop, and the verification-and-governance layer. The paper studies three core bottlenecks (context governance, trustworthy memory, dynamic skill routing) and calls for harness-level benchmarks that measure trajectory quality, memory hygiene, and context efficiency instead of one-shot task success.

```
The agent harness (everything around the model):

  foundation model ── context constructor ── memory substrate
        │                    │                     │
        └──── skill-routing layer ── orchestration loop ────┐
                                          │                 │
                                 verification + governance layer
        evaluate the harness, not just final-task success:
        trajectory quality · memory hygiene · context efficiency
```

## Key points

- **Model-centric evaluation is inadequate.** Reducing agents to final-task success hides where behavior actually comes from: memory, retrieval, tool use, orchestration, verification, and governance.
- **Six interacting components.** Capability is translated into long-horizon behavior by the whole stack; the labs own the model, but the practitioner owns the harness, and that is increasingly where quality is won or lost (the same framing in @dair_ai's accompanying thread).
- **Three named bottlenecks.** Context governance, trustworthy memory, and dynamic skill routing, plus the orchestration and governance mechanisms that coordinate and constrain them.
- **New benchmark agenda.** Harness-level benchmarks beyond one-shot success: trajectory quality, memory hygiene, context efficiency, communication overhead.

## Relation to prior wiki state

This is the explicit thesis statement for the "substrate around the agent" pattern the [2026-05-26 digest](../daily-digest/2026-05/2026-05-26.md) named as the day's main story. That digest watched four substrate axes move at once: MemForest (memory as a temporal data structure), SEAL (co-evolved training environment), SkillEvolBench (skill abstraction), and the Foundation Protocol (coordination). Scaling the Harness is the umbrella: it argues those are not separate papers but components of one object that should be designed and benchmarked together. The six components it lists map almost one-to-one onto the wiki's recent agentic pages: memory substrate → MemForest/MeMo; skill-routing → SkillOpt/SkillEvolBench; verification-and-governance → the Foundation Protocol + Ken Huang's intent-based access control thread.

It also dovetails with the day's two cost papers. [How Do AI Agents Spend Your Money (05-27)](2026-05-27-agent-token-consumption.md) shows the 154:1 input:output blowup is a context-management failure; "context governance" is exactly the harness bottleneck this paper names. And the Gradient Flow enterprise-agent survey (RSS, 05-26) is the field evidence: Upwork's Uma, Meta's PARA-structured Second Brain, EY's audit agents all succeed or fail on harness machinery (access control, structured context, retries, cost discipline), not on the base model.

## Why it matters

If the harness is the real design surface, the competitive moat shifts from "who has the best model" to "who builds the best execution layer," which is good news for application builders and bad news for the assumption that a bigger model fixes agent reliability. The benchmark agenda (trajectory quality, memory hygiene) is the more consequential ask: until those exist, agent quality stays anecdotal.

## Gaps

A position paper, not an empirical result. The harness-level benchmarks it calls for do not yet exist, so the three named bottlenecks are framing, not measurement.

## Links

- [Paper](https://arxiv.org/abs/2605.26112)
- Raw: [raw/twitter/2026-05-27-morning.md](../../raw/twitter/2026-05-27-morning.md)
- Related: [MemForest 2026-05-26](2026-05-26-memforest-hierarchical-temporal-agent-memory.md), [SkillEvolBench 2026-05-26](2026-05-26-skillevolbench-episodic-to-procedural-skills.md), [Agent token consumption 2026-05-27](2026-05-27-agent-token-consumption.md)
